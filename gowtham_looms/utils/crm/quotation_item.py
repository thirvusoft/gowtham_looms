from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def quotation_item_custom_fields():
    quotation_item_custom_fields = {
        "Quotation Item": [
            dict(
                fieldname= "ts_size",
                fieldtype= "Data",
                insert_after= "item_code",
                label="Size",
            ),
           
        ]
    }
    create_custom_fields(quotation_item_custom_fields)

def execute():
    quotation_item_custom_fields()