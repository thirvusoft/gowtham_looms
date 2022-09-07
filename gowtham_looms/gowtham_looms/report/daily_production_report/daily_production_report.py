# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
    columns = [
        {
            "label": _("Posting Date"),
            "fieldtype": "Date",
            "fieldname": "posting_date",
            "width": 200
        },
        {
            "label": _("Job Card"),
            "fieldtype": "Data",
            "fieldname": "name",
            "options": "Job Card",
            "width": 200
        },
        {
            "label": _("Item Code"),
            "fieldtype": "Data",
            "fieldname": "production_item",
            "options": "Item",
            "width": 200
        },
        {
            "label": _("Item Name"),
            "fieldtype": "Data",
            "fieldname": "item_name",
            "options": "Item",
            "width": 200
        },
        {
            "label": _("Operation"),
            "fieldtype": "Data",
            "fieldname": "operation",
            "options": "Operation",
            "width": 200
        },
        {
            "label": _("Status"),
            "fieldtype": "HTML",
            "fieldname": "status",
            "width": 200
        },
      
    ]
    return columns


def get_data(filters):
    filter={"docstatus":1}
    keys = list(filters.keys())
    if("item_name" in keys):
        filter["production_item"] = filters["item_name"]
    if("from_date" in keys and "to_date" in keys):
        filter["posting_date"] = ["between",
                                  (filters["from_date"], filters["to_date"])]
    elif("from_date" in keys):
        filter["posting_date"] = [">=", filters["from_date"]]
    elif("to_date" in keys):
        filter["posting_date"] = [
            "<=", filters["to_date"]]
    result = frappe.db.get_all(
        "Job Card", filters=filter, fields=["posting_date","name", "production_item","item_name","operation","status"])
    return result
