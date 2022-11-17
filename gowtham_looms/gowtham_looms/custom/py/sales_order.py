import frappe

def validate(doc,actions):
    so_item = frappe.get_all("Sales Order",{'customer':doc.customer,'docstatus':1},['name'])
    for i in so_item:
        s =[]
        d =[]
        get_doc = frappe.get_doc('Sales Order',i.name)
        for j in get_doc.items:
            s.append(j.item_code)
        for j in doc.items:
            d.append(j.item_code)
        if sorted(s) == sorted(d):
            doc.gl_item_check = 1
