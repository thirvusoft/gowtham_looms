from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def sales_invoice_custom_fields():
    sales_invoice_custom_fields = {
        "Sales Invoice": [
            dict(
                fieldname= "ts_transport_name",
                fieldtype= "Data",
                insert_after= "transporter",
                label="Transportation Mode",
            ),
            dict(
                fieldname= "ts_vehicle_no",
                fieldtype= "Data",
                insert_after= "ts_transport_name",
                label="Vehicle No",
            ),
            dict(
                fieldname= "ts_column_break",
                fieldtype= "Column Break",
                insert_after= "ts_vehicle_no",
                
            ),
            dict(
                fieldname= "ts_date",
                fieldtype= "Date",
                insert_after= "ts_column_break",
                label="Date of Supply",
            ),
            dict(
                fieldname= "ts_place",
                fieldtype= "Data",
                insert_after= "ts_date",
                label="Place of Supply",
            ),
           
        ]
    }
    create_custom_fields(sales_invoice_custom_fields)

def execute():
    sales_invoice_custom_fields()