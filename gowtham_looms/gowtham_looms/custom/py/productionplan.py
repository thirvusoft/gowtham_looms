from email.utils import formatdate
import frappe
from erpnext.manufacturing.doctype.production_plan.production_plan import ProductionPlan
from frappe.utils.data import cint, flt, format_time
from erpnext.stock.stock_ledger import NegativeStockError, get_previous_sle, get_valuation_rate


class productionplan(ProductionPlan):
    @frappe.whitelist()
    def make_work_order(doc,event):
        valid = frappe.get_all("Work Order",filters={"production_plan":doc.name,"docstatus":["!=",2]},pluck="name")
        if len(valid) >= 1:
            frappe.throw("Already ("+valid[0]+") Created For Work Order")
        else:
            from erpnext.manufacturing.doctype.work_order.work_order import get_default_warehouse

            wo_list, po_list = [], []
            subcontracted_po = {}
            default_warehouses = get_default_warehouse()

            doc.make_work_order_for_finished_goods(wo_list, default_warehouses)
            doc.make_work_order_for_subassembly_items(wo_list, subcontracted_po, default_warehouses)
            doc.make_subcontracted_purchase_order(subcontracted_po, po_list)
            doc.show_list_created_message("Work Order", wo_list)
            doc.show_list_created_message("Purchase Order", po_list)