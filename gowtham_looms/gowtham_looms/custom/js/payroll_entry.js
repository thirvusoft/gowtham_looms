frappe.ui.form.on("Payroll Employee Detail",{
    emp_repay_amt: function(frm, cdt, cdn){
        var row = locals[cdt][cdn]
        if(row.emp_repay_amt > row.emp_adv_amt){
            frappe.model.set_value(cdt, cdn, 'emp_repay_amt', 0)
            frappe.throw("Total Balance Amount cannot be greater than Amount Taken.")
        }
    }
})