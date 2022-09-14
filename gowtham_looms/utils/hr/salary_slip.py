from email.policy import default
from frappe import read_only
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def salary_slip():
    salary_details_custom_fields()
    salary_slip_custom_fields()
    create_defaults()
    

def salary_details_custom_fields():
    salary_details_custom_fields={
        "Salary Detail":[
          dict(
          fieldname = "amount_to_pay",
          fieldtype = "Currency",
          insert_after = "amount",
          label = "Amount"
          ),
          dict(
          fieldname = "employee_advance",
          fieldtype = "Link",
          insert_after = "amount_to_pay",
          label = "Employee Advance",
          read_only =1,
          options = "Employee Advance"
          ),
        ],
    }
    create_custom_fields(salary_details_custom_fields)


def salary_slip_custom_fields():
    salary_slip_custom_fields={
        "Salary Slip":[
          dict(
          fieldname = "total_amt",
          fieldtype = "Currency",
          insert_after = "deduction",
          label = "Total Amount",
          read_only =1,
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "total_paid_amount",
          fieldtype = "Currency",
          insert_after = "total_amt",
          label = "Total Paid Amount",
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "total_unpaid_amount",
          fieldtype = "Currency",
          insert_after = "total_paid_amount",
          label = "Total unpaid Amount",
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "sectionbreak1",
          fieldtype = "Section Break",
          insert_after = "total_unpaid_amount",
          ),
          dict(
          fieldname = "balance_amount",
          fieldtype = "Currency",
          insert_after = "payroll_frequency",
          label = "Balance Amount",
          read_only = 1,
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "balance1_amount",
          fieldtype = "Currency",
          insert_after = "balance_amount",
          label = "Balance Amount",
          fetch_from = "employee.advance1_salary",
          read_only = 1,
          hidden =1,
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "pay_the_balace",
          fieldtype = "Check",
          insert_after = "balance1_amount",
          label = "Pay the Balance",
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "total_advance_amount",
          fieldtype = "Data",
          insert_after = "get_emp_advance",
          label = "Total Advance Amount",
          description = "Employee Advance Created from <a href = /app/employee-advance-tools>Employee Advance Tools<a>",
          read_only =1,
          depends_on = "eval:doc.designation == 'Contractor'"
          ),
          dict(
          fieldname = "get_emp_advance",
          fieldtype = "Button",
          insert_after = "earnings",
          label = "Get Employee Advance",
          ),
        ],
    }
    create_custom_fields(salary_slip_custom_fields)
    
    
    
def execute():
  salary_slip()

def create_defaults():
  if(not frappe.db.exists("Salary Component", "Advance")):
          doc = frappe.new_doc("Salary Component")
          doc.salary_component = "Advance"
          doc.salary_component_abbr = 'ADV'
          doc.type = 'Deduction'
          doc.save(ignore_permissions=True)

