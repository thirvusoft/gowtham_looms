from erpnext.payroll.doctype.salary_slip.salary_slip import SalarySlip
import frappe
import json


@frappe.whitelist()
def emp_salary(employee,start_date,end_date,designation):
        if designation == "Contractor":
                total_wrk_amt = 0
                qty = {}
                jobcard = frappe.get_all("Job Card Time Log",filters={'docstatus':1,'employee':employee,'from_time': ['between',(start_date,end_date)]}, fields = ['parent', 'completed_qty as qty'])
                jc_names = [i['parent'] for i in jobcard]
                job_card_name = list(set(jc_names))
                wrk_order = frappe.get_all("Job Card",filters={'docstatus':1,'status':'Completed','name': ['in',job_card_name]}, fields = ['work_order', 'name'])
                for child in jobcard:
                        for parent in wrk_order:
                                if(parent['name'] == child['parent']):
                                        if(parent['work_order'] in qty.keys()):
                                                qty[parent['work_order']].append(child['qty'])
                                        else:
                                                qty[parent['work_order']] = [child['qty']]
                wo_names = [i['work_order'] for i in wrk_order]
                wrk_order_name = list(set(wo_names))
                item_qty = frappe.get_all("Work Order",filters={'docstatus':1,'status':'Completed','name': ['in',wrk_order_name]}, fields = ['production_item','name'])
                for i in range(len(item_qty)):
                        manufacture_cost = frappe.get_value("Item",item_qty[i]['production_item'] ,"ts_cost_per_manufacturing")
                        total_amt = manufacture_cost * (sum(qty[item_qty[i]['name']])/ len(qty[item_qty[i]['name']]) or 1)
                        total_wrk_amt +=total_amt
                return total_wrk_amt

def paid_amount(doc,action):
        tot_deduction = 0
        doc.gross_pay = doc.total_paid_amount or 0
        for i in doc.deductions:
                tot_deduction = i.amount or 0 + tot_deduction
        doc.net_pay = doc.gross_pay-tot_deduction
        doc.rounded_total = round(doc.net_pay)
        SalarySlip.compute_year_to_date(doc)
        #Calculation of Month to date
        SalarySlip.compute_month_to_date(doc)
        SalarySlip.compute_component_wise_year_to_date(doc)
        SalarySlip.set_net_total_in_words(doc)
        
def adv_amount(doc,action):
        update_employee_advance(doc)
        emp = frappe.get_value("Employee",doc.employee,"advance1_salary")
        emps = doc.total_unpaid_amount + emp
        if(doc.pay_the_balace):
                emps = doc.total_unpaid_amount
        frappe.db.set_value("Employee",doc.employee,"advance1_salary",emps)

def emp_balance_amt(doc,action):
        emp = frappe.get_value("Employee",doc.employee,"advance1_salary")
        emps = emp - doc.total_unpaid_amount
        if(doc.pay_the_balace):
                emps += doc.balance1_amount
        frappe.db.set_value("Employee",doc.employee,"advance1_salary",emps)
        for i in doc.deductions:
                if(i.employee_advance):
                        amt = frappe.db.get_value('Employee Advance', i.employee_advance, 'remaining_amount')
                        frappe.db.set_value('Employee Advance', i.employee_advance, 'remaining_amount', amt+i.amount)     
        
@frappe.whitelist()
def get_employee_advance_amount(name, start_date, end_date):
    deduct = sum(frappe.get_all("Employee Advance", filters={'employee':name, 'purpose':'Deduct from Salary'}, pluck='remaining_amount')) or 0
    return_ = sum(frappe.get_all("Employee Advance", filters={'employee':name, 'purpose':'Return Advance'}, pluck='advance_amount')) or 0
    return deduct-return_  
    
def payroll(doc,action):
        tot_amt = emp_salary(doc.employee,doc.start_date,doc.end_date,doc.designation)
        bal_salary = frappe.get_value("Employee",{"name":doc.employee,"company":doc.company},"advance1_salary")
        deduct = sum(frappe.get_all("Employee Advance", {'employee':doc.employee, 'purpose':'Deduct from Salary'},pluck='remaining_amount'))
        if(not doc.get('payroll_entry')):return
        emp_adv_amount = frappe.get_doc("Payroll Entry",doc.payroll_entry)
        if doc.employee:
                for i in emp_adv_amount.employees:
                        if i.employee == doc.employee:
                                if doc.deductions:
                                        com = [j.salary_component for j in doc.deductions]
                                        if "Advance" not in com:
                                                if i.emp_repay_amt:
                                                        doc.append('deductions',{'salary_component':'Advance', 'amount':float(i.emp_repay_amt),'amount_to_pay':float(i.emp_repay_amt)})
                                else:
                                        if i.emp_repay_amt:
                                                doc.update({
                                                        "deductions" : [{'salary_component':'Advance', 'amount':float(i.emp_repay_amt), 'amount_to_pay':float(i.emp_repay_amt)}]})
                                if doc.designation != "Contractor":
                                        tot_earnings = 0
                                        for i in doc.earnings:
                                                tot_earnings = i.amount or 0 + tot_earnings
                                                doc.gross_pay = tot_earnings
                                                tott_deduction = 0
                                                for i in doc.deductions:
                                                        tott_deduction = i.amount or 0 + tott_deduction
                                                        doc.total_deduction = tott_deduction
                                                doc.net_pay = doc.gross_pay-tott_deduction
                                                doc.rounded_total = round(doc.net_pay)
                                                SalarySlip.compute_year_to_date(doc)
                                                #Calculation of Month to date
                                                SalarySlip.compute_month_to_date(doc)
                                                SalarySlip.compute_component_wise_year_to_date(doc)
                                                SalarySlip.set_net_total_in_words(doc)
                com = [i.salary_component for i in doc.earnings]
                if "Basic" not in com:
                        doc.append('earnings',{'salary_component':'Basic', 'amount_to_pay':tot_amt})
                total_amt = 0
                for i in doc.earnings:   
                        total_amt = i.amount_to_pay or 0 + total_amt
                
                doc.total_amt = total_amt
                doc.total_advance_amount = deduct
                doc.total_amt =  doc.total_amt - doc.total_advance_amount 
                
                if doc.is_new():
                        doc.balance_amount = bal_salary 
                        doc.balance1_amount = bal_salary 
                
                        
                                
                                
        
                
                   

@frappe.whitelist()
def get_advance_amounts(employee):
    adv = frappe.get_all(
            "Employee Advance",
            filters=
                {'employee':employee, 'purpose':'Deduct from Salary', 'remaining_amount': ['>', 0]}, 
            fields=['name', 'remaining_amount'])
    fields = []
    for i in range(len(adv)):
        fields.append({'label':'Name','fieldname':f'name{i}', 'fieldtype':'Link', 'options':'Employee Advance', 'default':adv[i]['name'], 'read_only':1})
        fields.append({'fieldname':f'col_brk1{i}', 'fieldtype':'Column Break'})
        fields.append({'fieldname':f'adv_amt{i}', 'label':'Advance Amount', 'fieldtype':'Currency', 'default':adv[i]['remaining_amount'], 'read_only':1})
        fields.append({'fieldname':f'col_brk2{i}', 'fieldtype':'Column Break'})
        fields.append({'fieldname':f'amt_take{i}', 'label':'Amount Taken', 'fieldtype':'Currency'})
        fields.append({'fieldname':f'sec_brk1{i}', 'fieldtype':'Section Break'})
    
    fields.append({'fieldname':'dataaa', 'fieldtype':'Data', 'hidden':1})   
    fields.append({'fieldname':'col_brk', 'fieldtype':'Column Break'})
    fields.append({'fieldname':'total_amount', 'label':'Total Amount', 'fieldtype':'Currency', 'read_only':1})
    return fields, len(adv)

@frappe.whitelist()
def change_remaining_amount(data, length):
    from gowtham_looms.utils.hr.salary_slip import create_defaults
    create_defaults()
    data = json.loads(data)
    amount = 0 
    deductions = []
    for i in range(int(length)):
        amount += data[f'amt_take{i}']
        if(data[f'amt_take{i}'] > 0):
                if(data[f'amt_take{i}'] > data[f'adv_amt{i}']):
                       frappe.throw('Amount Taken should not be greater than Advance amount.')
                deductions.append({'salary_component':'Advance','amount':  data[f'amt_take{i}'], 'employee_advance': data[f'name{i}']})
        # frappe.db.set_value('Employee Advance', data[f'name{i}'], 'remaining_amount', data[f'adv_amt{i}'] - data[f'amt_take{i}'])
    return deductions

def update_employee_advance(doc):
    for i in doc.deductions:
        if(i.employee_advance):
            amt = frappe.db.get_value('Employee Advance', i.employee_advance, 'remaining_amount')
            frappe.db.set_value('Employee Advance', i.employee_advance, 'remaining_amount', amt-i.amount)