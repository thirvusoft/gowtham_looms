frappe.ui.form.on("Stock Entry", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Material Request','Create');
		},100);  
    },
  
})
