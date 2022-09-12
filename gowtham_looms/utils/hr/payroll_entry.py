from frappe import read_only
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def payroll():
    payroll_employee_custom_fields()

    
def payroll_employee_custom_fields():
    payroll_employee_custom_fields={
        "Payroll Employee Detail":[
          dict(
          fieldname = "emp_adv_amt",
          fieldtype = "Data",
          insert_after = "employee_name",
          label = "Employee Advance Amount",
          ),
          dict(
          fieldname = "emp_repay_amt",
          fieldtype = "Data",
          insert_after = "emp_adv_amt",
          label = "Employee Repayment Amount",
          ),
        ],
    }
    create_custom_fields(payroll_employee_custom_fields)    
    

def execute():
    payroll()
    
    