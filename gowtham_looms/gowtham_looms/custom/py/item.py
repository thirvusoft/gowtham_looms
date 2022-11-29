import json
import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from gowtham_looms.gowtham_looms.custom.py.item_group import validate
from frappe.model.naming import make_autoname

def create_service_item():
    if(not frappe.db.exists("Item", {'item_group':'Service', 'item_name':'Service Item'})):
        doc = frappe.new_doc("Item")
        doc.item_name = "Service Item"
        doc.item_group = "Service"
        doc.abbr = "SE"
        doc.is_stock_item = 0
        doc = validate(doc,"")
        doc.save(ignore_permissions=True)
    if(not frappe.db.exists("Item", {'item_group':'Service', 'item_name':'Service Cost'})):
        doc = frappe.new_doc("Item")
        doc.item_name = "Service Cost"
        doc.item_group = "Service"
        doc.abbr = "SE"
        doc.is_stock_item = 0
        doc = validate(doc,"")
        doc.save(ignore_permissions=True)
    frappe.db.commit()

def validate(doc, actions):
        abbr = f'{doc.abbrevation}.##.-.{doc.ts_type}'
        old_series = frappe.get_meta('Item').get_field("naming_series").options.split()
        if(doc.ts_type not in ["",None]):
            if(abbr not in old_series):
                update_query = frappe.db.sql(f""" INSERT INTO tabSeries VALUES ("{abbr}",0) """)
                old_series = frappe.get_meta('Item').get_field("naming_series").options
                defaults = frappe.get_meta('Item').get_field("naming_series").default
                make_property_setter('Item', 'naming_series', 'options', f'{old_series}\n{abbr}', 'Text Editor')
                make_property_setter('Item', 'naming_series', 'default', defaults, 'Text Editor')
        elif(doc.item_group != "Looms"):
            doc.name = make_autoname("R"+'-'+ doc.abbrevation + '.##')
        else:
            doc.name = make_autoname(doc.item_name)