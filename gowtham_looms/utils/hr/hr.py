from email.policy import default
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def employee_custom_fields():
    employee_custom_fields={
        "Employee":[
          dict(
          fieldname = "advance1_salary",
          fieldtype = "Currency",
          insert_after = "date_of_joining",
          label = "Balance Salary",
          read_only = 1
          ),
        ],
    }
    create_custom_fields(employee_custom_fields)
    
def execute():
  employee_custom_fields()