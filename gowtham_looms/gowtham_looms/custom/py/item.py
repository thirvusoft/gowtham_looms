import json
import frappe
from gowtham_looms.gowtham_looms.custom.py.item_group import validate

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
    
