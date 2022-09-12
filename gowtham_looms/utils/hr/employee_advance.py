from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def employee_advance_custom_fields():
    employee_advance_custom_fields={
        "Employee Advance":[
            dict(fieldname='remaining_amount', 
                label='Remaining Amount', 
                fieldtype='Currency', 
                insert_after='return_amount', 
                read_only=1, 
                allow_on_submit=1
                )
        ],
    }
    create_custom_fields(employee_advance_custom_fields)
    
def execute():
  employee_advance_custom_fields()