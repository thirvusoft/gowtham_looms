import frappe

def create_designation():    
    if(not frappe.db.exists("Designation", "Contractor")):
        doc = frappe.new_doc("Designation")
        doc.designation_name = "Contractor"
        doc.save(ignore_permissions=True)
    frappe.db.commit()
    