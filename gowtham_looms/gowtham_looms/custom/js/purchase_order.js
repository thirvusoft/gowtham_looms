frappe.ui.form.on("Purchase Order", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Supplier Quotation','Get Items From');
            frm.remove_custom_button('Product Bundle','Get Items From');
            frm.remove_custom_button('Update Rate as per Last Purchase','Tools')
		},100);  
    },
    supplier: function(frm){
        frappe.call({
            method: "gowtham_looms.gowtham_looms.custom.py.purchase_order.item_supplier",
            args:{
                supplier:frm.doc.supplier,
            },
            callback: function(r) {
                if(frm.doc.supplier!= ""){
                    frm.set_value('items',r.message);
                    frm.refresh()}
                else{
                    frm.set_value('items',"");
                    frm.refresh()                   
                }
            }
        })
    }
  
})
