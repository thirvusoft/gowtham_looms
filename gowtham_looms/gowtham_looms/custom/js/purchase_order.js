frappe.ui.form.on("Purchase Order", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Supplier Quotation','Get Items From');
            frm.remove_custom_button('Product Bundle','Get Items From');
		},100);  
    },
  
})
