frappe.ui.form.on("Sales Order", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Project','Create');
            frm.remove_custom_button('Pick List','Create');
            frm.remove_custom_button('Subscription','Create');
		},100);  
    },
  
})
