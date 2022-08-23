import frappe 
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def create_property_setter():
    make_property_setter('Production Plan', 'get_sub_assembly_items', 'hidden', 1, 'Check')
    make_property_setter('Production Plan', 'sub_assembly_items', 'hidden', 1, 'Check')
    make_property_setter('Work Order','production_plan_item','hidden', 1, 'Check')



def execute():
    create_property_setter()