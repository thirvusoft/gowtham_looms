frappe.ui.form.on("Employee Advance Tools",{
	designation:function(frm,cdt,cdn){
		var advance=locals[cdt][cdn]
		var advance1=advance.designation
		frm.call({
			method:"employee_finder",
			args:{advance1},
			callback(r){
				frm.clear_table("employee_advance_details");
				for(var i=0;i<r.message.length;i++){
					var child = cur_frm.add_child("employee_advance_details");
					frappe.model.set_value(child.doctype, child.name, "employee", r.message[i]["name"])
					frappe.model.set_value(child.doctype, child.name, "employee_name", r.message[i]["employee_name"])
					frappe.model.set_value(child.doctype, child.name, "designation", advance1)
					if (frm.doc.designation == "Labour Worker"){
						frappe.model.set_value(child.doctype, child.name, "payment_method",'Deduct from Salary')
					}
				}
				cur_frm.refresh_field("employee_advance_details")
			}
		})

	},
	
	before_submit:function(frm,cdt,cdn){
		var advance=locals[cdt][cdn]
		for(var i=0;i<advance.employee_advance_details.length;i++){
			frm.call({
				async:false,
				freeze: true,
				freeze_message: "Creating Employee Advance .... ",
				method:"create_employee_advance",
				args:{amount:advance.employee_advance_details[i].current_advance,
					name:advance.employee_advance_details[i].employee,
					date:frm.doc.date,
					payment_type:advance.employee_advance_details[i].payment_method,
					doc_name: frm.doc.name},
				callback(r){
					if(r.message){
						frappe.validated=false
						frappe.throw(r.message)
					}
					else{
						frappe.validated=true
					}
				}
			})
		}
	},
	before_save:function(frm, cdt, cdn) {

		var table = frm.doc.employee_advance_details;
		var total = 0;
		for(var i in table) {
			total = total + table[i].current_advance;
		 }
		 frm.set_value("total_advance_amount",total);
		}
	
})