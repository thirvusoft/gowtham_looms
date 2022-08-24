from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def production_plan_custom_fields():
    production_plan_custom_fields={
        "Production Plan":[
          dict(
          fieldname = "end_date",
          fieldtype = "Date",
          insert_after = "posting_date",
          label = "End Date"
          ),
        ],
    }
    create_custom_fields(production_plan_custom_fields)
    
def execute():
    production_plan_custom_fields()