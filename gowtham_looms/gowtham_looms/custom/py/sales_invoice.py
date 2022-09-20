import frappe
import json

from gowtham_looms.gowtham_looms.custom.py.item import create_service_item

@frappe.whitelist()
def create_sales_invoice(doc):
    create_service_item()
    
    doc = json.loads(doc)
    si = frappe.new_doc("Sales Invoice")
    si.customer = doc.get('customer')
    si.due_date = frappe.utils.nowdate()
    si.update_stock = 1
    si.maintenance_visit = doc.get('name')
    default_company = frappe.db.get_single_value("Global Defaults", "default_company")
    items=[{
            'item_code':frappe.get_value('Item', {'item_name':'Service Cost'}, 'item_code'),
            'item_name':'Service Cost',
            'qty':1,
            'rate':doc.get('ts_service_cost'),
            'amount':doc.get('ts_service_cost'),
            'description': frappe.get_value('Item',{'item_name':'Service Cost'}, 'description'),
            'uom': frappe.get_value('Item', {'item_name':'Service Cost'}, 'stock_uom'),
            'income_account' : frappe.get_value('Company', default_company, 'default_income_account'),
            'cost_center' : frappe.get_value('Company', default_company, 'cost_center')  
    }]
    
    for i in doc.get('ts_table'):
        items.append({
            'item_code':i.get('item_code'),
            'item_name':i.get('item_name'),
            'qty':i.get('qty'),
            'rate':i.get('rate'),
            'amount':i.get('amount'),
            'description': frappe.get_value('Item', i.get('item_code'), 'description'),
            'uom': frappe.get_value('Item', i.get('item_code'), 'stock_uom'),
            'income_account' : frappe.get_value('Company', default_company, 'default_income_account'),
            'cost_center' : frappe.get_value('Company', default_company, 'cost_center')
        })
    si.update({
        'items':items
        })
    return si.as_dict()

def change_mv_status(doc, action):
    for i in doc.references:
        if(i.reference_doctype == 'Sales Invoice'):
            si = frappe.get_doc('Sales Invoice', i.reference_name)
            status = ''
            if(si.maintenance_visit):
                if(si.outstanding_amount == 0):
                    status = 'Paid'
                elif(si.outstanding_amount == si.rounded_total):
                    status = 'Unpaid'
                elif(si.outstanding_amount <= si.rounded_total and si.outstanding_amount >= 0):
                    status = 'Partially Paid'
                frappe.db.set_value('Maintenance Visit', si.maintenance_visit, 'payment_status', status)