from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def sales_order_custom_fields():
    sales_order_custom_fields = {
        "Sales Order": [
            dict(
                fieldname= "ts_column_break",
                fieldtype= "Column Break",
                insert_after= "total_qty"
            ),
           
        ]
    }
    create_custom_fields(sales_order_custom_fields)

def execute():
    sales_order_custom_fields()