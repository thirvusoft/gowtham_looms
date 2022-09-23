import frappe

def delete_price_list(doc, action):
    
    if doc.item_name == "Service Cost":
        print("Test-------------")
        frappe.delete_doc("Item Price", doc.name)