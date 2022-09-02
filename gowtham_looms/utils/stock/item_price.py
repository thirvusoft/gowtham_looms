from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def item_price_custom_fields():
    item_price_custom_fields = {
        "Item Price": [
            dict(
                fieldname= "ts_item_group",
                fieldtype= "Data",
                insert_after= "item_code",
                label= "Item Group",
                fetch_from="item_code.item_group"
            ),
           
        ]
    }
    create_custom_fields(item_price_custom_fields)

def execute():
    item_price_custom_fields()
