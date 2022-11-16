import frappe

@frappe.whitelist()
def stock_reconciliation_item(company):
    stock_item = frappe.get_all("Item Default",{'company':company},['parent as item_code','default_warehouse as warehouse'])
    return stock_item


