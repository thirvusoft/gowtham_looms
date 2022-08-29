frappe.ui.form.on("Sales Invoice", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Delivery Note','Get Items From');
            frm.remove_custom_button('Invoice Discounting','Create');
            frm.remove_custom_button('Subscription','Create');
            frm.remove_custom_button('Fetch Timesheet');
		},1000);  
    },
  
})
