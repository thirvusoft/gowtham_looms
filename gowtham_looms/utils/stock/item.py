from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def custom_fields():
    item_custom_fields = {
        "Item": [
            dict(
                fieldname= "ts_cost_per_manufacturing",
                fieldtype= "Currency",
                insert_after= "stock_uom",
                label= "Manufacturing Expense",
                depends_on="eval:doc.item_group=='Looms'"
            ),
            dict(
                fieldname= "ts_cmpy_abbr",
                fieldtype= "Data",
                insert_after= "abbrevation",
                label= "Company Abbr",
                fetch_from='item_group.abbr'
            ),
            dict(
                fieldname= "gl_old_group",
                fieldtype= "Data",
                insert_after= "item_group",
                label= "Old Item Code",
            ),
            dict(
                fieldname= "abbrevation",
                fieldtype= "Data",
                insert_after= "item_code",
                label= "Abbr",
                hidden=1,
                fetch_from='item_group.abbr'
            ),
        ]
    }
    create_custom_fields(item_custom_fields)

def execute():
    custom_fields()
