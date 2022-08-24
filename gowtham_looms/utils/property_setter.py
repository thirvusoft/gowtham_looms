import frappe 
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def create_property_setter():
    make_property_setter('Production Plan', 'get_sub_assembly_items', 'hidden', 1, 'Check')
    make_property_setter('Production Plan', 'sub_assembly_items', 'hidden', 1, 'Check')
    make_property_setter('Work Order','production_plan_item','hidden', 1, 'Check')
    make_property_setter('Item','section_break_11','hidden', 1, 'Check')
    make_property_setter('Item','sb_barcodes','hidden', 1, 'Check')
    make_property_setter('Item','unit_of_measure_conversion','hidden', 1, 'Check')
    make_property_setter('Item','serial_nos_and_batches','hidden', 1, 'Check')
    make_property_setter('Item','variants_section','hidden', 1, 'Check')
    make_property_setter('Item','purchase_details','hidden', 1, 'Check')
    make_property_setter('Item','supplier_details','hidden', 1, 'Check')
    make_property_setter('Item','foreign_trade_details','hidden', 1, 'Check')
    make_property_setter('Item','sales_details','hidden', 1, 'Check')
    make_property_setter('Item','deferred_revenue','hidden', 1, 'Check')
    make_property_setter('Item','deferred_expense_section','hidden', 1, 'Check')
    make_property_setter('Item','customer_details','hidden', 1, 'Check')
    make_property_setter('Item','item_tax_section_break','hidden', 1, 'Check')
    make_property_setter('Item','inspection_criteria','hidden', 1, 'Check')
    make_property_setter('Item','manufacturing','hidden', 1, 'Check')
    make_property_setter('Item','hub_publishing_sb','hidden', 1, 'Check')
    make_property_setter('Item','more_information_section','hidden', 1, 'Check')
    make_property_setter('Item','defaults','hidden', 1, 'Check')



def execute():
    create_property_setter()