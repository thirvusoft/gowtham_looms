from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def item_group_custom_fields():
    item_group_custom_fields = {
        "Item Group": [
            dict(
                fieldname= "abbr",
                fieldtype= "Data",
                insert_after= "item_group_name",
                label= "Abbr",
            ),
        ]
    }
    create_custom_fields(item_group_custom_fields)

def execute():
    item_group_custom_fields()
