import frappe
from erpnext.manufacturing.doctype.job_card.job_card import JobCard, OverlapError
from frappe.utils.data import flt, get_datetime, time_diff_in_hours

class jobcard(JobCard):
    @frappe.whitelist()
    def validate_time_logs(doc):
        doc.total_time_in_mins = 0.0
        doc.total_completed_qty = 0.0

        if doc.get("time_logs"):
            for d in doc.get("time_logs"):
                if d.to_time and get_datetime(d.from_time) > get_datetime(d.to_time):
                    frappe.throw(frappe._("Row {0}: From time must be less than to time").format(d.idx))

                if d.from_time and d.to_time:
                    d.time_in_mins = time_diff_in_hours(d.to_time, d.from_time) * 60
                    doc.total_time_in_mins += d.time_in_mins

                if d.completed_qty and not doc.sub_operations:
                    doc.total_completed_qty += d.completed_qty

            doc.total_completed_qty = flt(doc.total_completed_qty, doc.precision("total_completed_qty"))

        for row in doc.sub_operations:
            doc.total_completed_qty += row.completed_qty