from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def quotation_custom_fields():
    quotation_custom_fields = {
        "Quotation": [
            dict(
                fieldname= "ts_phone_no",
                fieldtype= "Data",
                insert_after= "company_address",
                label="Phone Number",
                fetch_from = "company_address.phone"
            ),
           
        ]
    }
    create_custom_fields(quotation_custom_fields)

def execute():
    quotation_custom_fields()