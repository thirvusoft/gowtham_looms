import frappe

def create_service_item():
    if(not frappe.db.exists("Item", {'item_group':'Service', 'item_name':'Service Item'})):
        doc = frappe.new_doc("Item")
        doc.item_name = "Service Item"
        doc.item_group = "Service"
        doc.is_stock_item = 0
        doc.save(ignore_permissions=True)
    if(not frappe.db.exists("Item", {'item_group':'Service', 'item_name':'Service Cost'})):
        doc = frappe.new_doc("Item")
        doc.item_name = "Service Cost"
        doc.item_group = "Service"
        doc.is_stock_item = 0
        doc.save(ignore_permissions=True)
    frappe.db.commit()
    