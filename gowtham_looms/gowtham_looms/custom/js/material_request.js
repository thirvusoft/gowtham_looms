frappe.ui.form.on("Material Request", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Bill of Materials','Get Items From');
            frm.remove_custom_button('Sales Order','Get Items From');
            frm.remove_custom_button('Product Bundle','Get Items From');
            frm.remove_custom_button('Purchase Order','Create');
            frm.remove_custom_button('Request for Quotation','Create');
            frm.remove_custom_button('Supplier Quotation','Create');
		},100);  
    },
  
})
