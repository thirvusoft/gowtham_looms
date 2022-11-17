from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def buyiing_settings_custom_fields():
    buyiing_settings_custom_fields={
        "Buying Settings":[
          dict(
          fieldname = "lead_day",
          fieldtype = "Data",
          insert_after = "bill_for_rejected_quantity_in_purchase_invoice",
          label = "Lead Days",
          ),
        ],
    }
    create_custom_fields(buyiing_settings_custom_fields)
    
def execute():
  buyiing_settings_custom_fields()