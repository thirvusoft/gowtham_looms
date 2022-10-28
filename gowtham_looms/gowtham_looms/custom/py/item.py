import json
from erpnext.erpnext.controllers.item_variant import copy_attributes_to_variant
import frappe
from frappe.utils.data import cstr
from gowtham_looms.gowtham_looms.custom.py.item_group import validate
from six import string_types

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
    
