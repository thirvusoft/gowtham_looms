from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def maintenance_visit_fields():
    maintenance_visit_fields = {
        "Maintenance Visit": [
             dict(
                fieldname= "ts_section_break",
                fieldtype= "Section Break",
                insert_after= "purposes",
            ),
            dict(
                fieldname= "ts_table",
                fieldtype= "Table",
                insert_after= "ts_section_break",
                label = "Item Consumed During Service",
                options = "Item for Services"
            ),
            dict(
                fieldname= "ts_section_break1",
                fieldtype= "Section Break",
                insert_after= "ts_table",
            ),
            dict(
                fieldname= "ts_service_cost",
                fieldtype= "Currency",
                insert_after= "ts_section_break1",
                label = "Service Cost",
                reqd = 1

            ),
            dict(
                fieldname= "ts_column_break",
                fieldtype= "Column Break",
                insert_after= "ts_service_cost",
            ),
            dict(
                fieldname= "ts_item_for_service_cost",
                fieldtype= "Currency",
                insert_after= "ts_column_break",
                label = "Total Item Cost Consumed",
            ),
            dict(
                fieldname= "payment_status",
                fieldtype= "Select",
                label = "Status",
                in_list_view = 1,
                options = 'Unpaid\nPaid\nPartially Paid',
                hidden=1
            ),
        ],
        'Sales Invoice':[
            dict(
                fieldname= "maintenance_visit",
                fieldtype= "Link",
                label = "Maintenance Visit",
                options = "Maintenance Visit",
                hidden=1,
                no_copy=1
            ),
        ]
    }
    create_custom_fields(maintenance_visit_fields)

def execute():
    maintenance_visit_fields()