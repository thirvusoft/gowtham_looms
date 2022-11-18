from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def sales_order_custom_fields():
    sales_order_custom_fields = {
        "Sales Order": [
            dict(
                fieldname= "ts_column_break",
                fieldtype= "Column Break",
                insert_after= "total_qty"
            ),
            dict(
                fieldname= "gl_item_check",
                fieldtype= "Check",
                insert_after= "order_type",
                hidden=1
            ),    
            dict(
                fieldname= "ts_phone_no",
                fieldtype= "Data",
                insert_after= "company_address",
                label="Phone Number",
                fetch_from = "company_address.phone"
            ), 
        ]
    }
    create_custom_fields(sales_order_custom_fields)

def execute():
    sales_order_custom_fields()