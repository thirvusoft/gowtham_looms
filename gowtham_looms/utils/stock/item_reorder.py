from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def item_reorder_custom_fields():
    item_reorder_custom_fields = {
        "Item Reorder": [
            dict(
                fieldname= "ts_max_qty",
                fieldtype= "Float",
                insert_after= "warehouse_reorder_level",
                label= "Max Qty",
                reqd=1,
                in_list_view=1
            ),
           
        ]
    }
    create_custom_fields(item_reorder_custom_fields)

def execute():
    item_reorder_custom_fields()
