from email.policy import default
from frappe import read_only
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def salary_slip():
    salary_details_custom_fields()
    salary_slip_custom_fields()

def salary_details_custom_fields():
    salary_details_custom_fields={
        "Salary Detail":[
          dict(
          fieldname = "amount_to_pay",
          fieldtype = "Currency",
          insert_after = "amount",
          label = "Amount to Pay"
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
          read_only =1
          ),
          dict(
          fieldname = "total_paid_amount",
          fieldtype = "Currency",
          insert_after = "total_amt",
          label = "Total Paid Amount"
          ),
          dict(
          fieldname = "total_unpaid_amount",
          fieldtype = "Currency",
          insert_after = "total_paid_amount",
          label = "Total unpaid Amount"
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
          read_only = 1
          ),
          dict(
          fieldname = "balance1_amount",
          fieldtype = "Currency",
          insert_after = "balance_amount",
          label = "Balance Amount",
          fetch_from = "employee.advance1_salary",
          read_only = 1,
          hidden =1
          ),
          dict(
          fieldname = "pay_the_balace",
          fieldtype = "Check",
          insert_after = "balance1_amount",
          label = "Pay the Balance"
          ),
        ],
    }
    create_custom_fields(salary_slip_custom_fields)
    
    
    
def execute():
  salary_slip()