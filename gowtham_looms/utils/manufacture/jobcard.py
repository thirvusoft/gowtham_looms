from email.policy import default
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def jobcard_custom_fields():
    jobcard_custom_fields={
        "Job Card":[
          dict(
          fieldname = "doc_onload",
          fieldtype = "Check",
          insert_after = "operation",
          hidden = 1,
          default = 0
          ),
        ],
    }
    create_custom_fields(jobcard_custom_fields)
    
def execute():
  jobcard_custom_fields()