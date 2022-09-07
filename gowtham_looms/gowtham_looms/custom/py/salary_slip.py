from erpnext.payroll.doctype.salary_slip.salary_slip import SalarySlip
import frappe

@frappe.whitelist()
def emp_salary(employee,start_date,end_date):
        total_wrk_amt = 0
        jobcard = frappe.get_all("Job Card Time Log",filters={'docstatus':1,'employee':employee,'from_time': ['between',(start_date,end_date)],'to_time':['between',(start_date,end_date)]}, pluck = 'parent')
        job_card_name = list(set(jobcard))
        wrk_order = frappe.get_all("Job Card",filters={'docstatus':1,'status':'Completed','name': ['in',job_card_name]}, pluck = 'work_order')
        wrk_order_name = list(set(wrk_order))
        item_qty = frappe.get_all("Work Order",filters={'docstatus':1,'status':'Completed','name': ['in',wrk_order_name]}, fields = ['production_item','qty'])
        for i in range(len(item_qty)):
            manufacture_qty = frappe.get_value("Item",item_qty[i]['production_item'] ,"ts_cost_per_manufacturing")
            total_amt = manufacture_qty * item_qty[i]['qty']
            total_wrk_amt +=total_amt
        return total_wrk_amt

def paid_amount(doc,action):
        doc.gross_pay = doc.total_paid_amount
        doc.net_pay = (doc.gross_pay-doc.total_deduction)
        doc.rounded_total = round(doc.net_pay)
        SalarySlip.compute_year_to_date(doc)
        #Calculation of Month to date
        SalarySlip.compute_month_to_date(doc)
        SalarySlip.compute_component_wise_year_to_date(doc)
        SalarySlip.set_net_total_in_words(doc)
        
def adv_amount(doc,action):
        emp = frappe.get_value("Employee",doc.employee,"advance1_salary")
        emps = doc.total_unpaid_amount + emp
        frappe.db.set_value("Employee",doc.employee,"advance1_salary",emps)

def emp_balance_amt(doc,action):
        emp = frappe.get_value("Employee",doc.employee,"advance1_salary")
        emps = emp - doc.total_unpaid_amount
        frappe.db.set_value("Employee",doc.employee,"advance1_salary",emps)     
        
@frappe.whitelist()
def get_employee_advance_amount(name, start_date, end_date):
    deduct = sum(frappe.get_all("Employee Advance", filters={'posting_date': ['between',(start_date, end_date)], 'employee':name, 'purpose':'Deduct from Salary'}, pluck='advance_amount')) or 0
    return_ = sum(frappe.get_all("Employee Advance", filters={'posting_date': ['between',(start_date, end_date)], 'employee':name, 'purpose':'Return Advance'}, pluck='advance_amount')) or 0
    return deduct-return_  
    
  
