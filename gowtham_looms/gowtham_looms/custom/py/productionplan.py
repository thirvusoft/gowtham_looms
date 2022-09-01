from email.utils import formatdate
import frappe
from erpnext.manufacturing.doctype.production_plan.production_plan import ProductionPlan
from frappe.utils.data import cint, flt, format_time
from erpnext.stock.stock_ledger import NegativeStockError, get_previous_sle, get_valuation_rate
          
class productionplan(ProductionPlan):
            
    def get_production_items(self):
        item_dict = {}

        for d in self.po_items:
            item_details = {
                "production_item": d.item_code,
                "use_multi_level_bom": d.include_exploded_items,
                "sales_order": d.sales_order,
                "sales_order_item": d.sales_order_item,
                "material_request": d.material_request,
                "material_request_item": d.material_request_item,
                "bom_no": d.bom_no,
                "description": d.description,
                "stock_uom": d.stock_uom,
                "company": self.company,
                "fg_warehouse": d.warehouse,
                "production_plan": self.name,
                "production_plan_item": d.name,
                "product_bundle_item": d.product_bundle_item,
                "planned_start_date": d.planned_start_date,
                "project": self.project,
            }

            if not item_details["project"] and d.sales_order:
                item_details["project"] = frappe.get_cached_value("Sales Order", d.sales_order, "project")

            if self.get_items_from == "Material Request":
                item_details.update({"qty": d.planned_qty})
                item_dict[(d.item_code, d.material_request_item, d.warehouse)] = item_details
            else:
                item_details.update(
                    {
                        "qty": flt(item_dict.get((d.item_code, d.sales_order, d.warehouse), {}).get("qty"))
                        + (flt(d.planned_qty) - flt(d.ordered_qty))
                    }
                )
                if item_details.get("qty"):
                    item_dict[(d.item_code, d.sales_order, d.warehouse)] = item_details
                else:
                   frappe.throw("Planned Qty is Already Taken for Work Order")

        return item_dict
            
