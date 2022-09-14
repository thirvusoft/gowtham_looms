import json
import frappe

def payroll_advance_amount(doc,action):
    for i in doc.employees:
        employee_advance = sum(frappe.db.get_all("Employee Advance",{"company":doc.company,"employee":i.employee},pluck="remaining_amount"))
        i.emp_adv_amt = employee_advance
