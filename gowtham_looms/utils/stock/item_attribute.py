from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def item_attribute_custom_fields():
    item_attribute_custom_fields = {
        "Item Attribute": [
            dict(
                fieldname= "not_include_in_name",
                fieldtype= "Check",
                insert_after= "numeric_values",
                label= "Not Include in Name",
            ),


        ]
    }
    create_custom_fields(item_attribute_custom_fields)

def execute():
    item_attribute_custom_fields()
