import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def validate(self,action):
    company = frappe.db.get_single_value("Global Defaults","default_company")
    abbr = frappe.db.get_value("Company",company,"abbr")
    naming_series = abbr+"-"+self.abbr
    name = frappe.db.get_single_value("Naming Series","select_doc_for_series")
    doc = frappe.db.sql (f""" select * from tabSeries where name = "{naming_series}" """)
    if len(doc)==0:
        update_query = frappe.db.sql(f""" INSERT INTO tabSeries VALUES ("{naming_series}",0) """)
        old_series = frappe.get_meta('Item').get_field("naming_series").options
        make_property_setter('Item', 'naming_series', 'options', f'{old_series}\n{naming_series}', 'Text Editor')