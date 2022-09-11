from email.policy import default
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def bank_account_custom_fields():
    bank_account_custom_fields={
        "Bank Account":[
          dict(
          fieldname = "ifsc_code",
          fieldtype = "Data",
          insert_after = "iban",
          label = "IFSC Code",
          ),
          dict(
          fieldname = "branch_name",
          fieldtype = "Data",
          insert_after = "ifsc_code",
          label = "Branch Name",
          ),
        ],
    }
    create_custom_fields(bank_account_custom_fields)
    
def execute():
  bank_account_custom_fields()