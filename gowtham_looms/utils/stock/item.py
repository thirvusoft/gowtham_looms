from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def custom_fields():
    item_custom_fields = {
        "Item": [
            dict(
                fieldname= "ts_cost_per_manufacturing",
                fieldtype= "Currency",
                insert_after= "stock_uom",
                label= "Manufacturing Cost",
            ),
        ]
    }
    create_custom_fields(item_custom_fields)

def execute():
    custom_fields()
