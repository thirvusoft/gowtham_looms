from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def sales_order_item_custom_fields():
    sales_order_item_custom_fields = {
        "Sales Order Item": [
            dict(
                fieldname= "ts_size",
                fieldtype= "Data",
                insert_after= "item_code",
                label="Size",
            ),
           
        ]
    }
    create_custom_fields(sales_order_item_custom_fields)

def execute():
    sales_order_item_custom_fields()