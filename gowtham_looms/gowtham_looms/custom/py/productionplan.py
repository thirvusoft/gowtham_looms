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
            
# def available_qty(doc,event):
#     for i in doc.mr_items:
#        if i.actual_qty >= i.quantity:
#             doc.append('mr_items', dict(
#                 item_code = "GL-BA1",
#                 item_name = "2X1 SHELLER FLAT(BOX SIDE)",
#                 warehouse = "Stores - Ls",
#                 material_request_type = "Material Transfer",
#                 from_warehouse = "Goods In Transit - Ls",
#                 quantity = 1  
#             ))
    
    # for i in doc.mr_items:
    #     if i.actual_qty <= i.quantity:
    #             frappe.throw(
    #                     frappe._(
    #                         "Quantity not available for {1} in warehouse {0}"
    #                     ).format(
    #                         frappe.bold(i.warehouse),
    #                         frappe.bold(i.item_code),
    #                     )
    #                     + "<br><br>"
    #                     + frappe._("Available quantity is {0}, you need {1}").format(
    #                         frappe.bold(flt(i.actual_qty)),
    #                         frappe.bold(i.quantity)
    #                     ),
                        
    #                 ),
    # #         doc.append('mr_items', dict(
    #             item_code = i.item_code,
    #             item_name = i.item_name,
    #             warehouse = i.warehouse,
    #             material = "Purchase",
    #             quantity = i.quantity-i.actual_qty   
    #         ))
    
            # elif i.actual_qty <= i.quantity:
            # 
       