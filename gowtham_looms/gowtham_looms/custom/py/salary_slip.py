import frappe
import json

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
        