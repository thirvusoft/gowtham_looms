import frappe

@frappe.whitelist()

def item_supplier(supplier):
    supplier = frappe.get_all("Item Supplier",{'supplier':supplier},["parent as item_code"])
    return supplier

