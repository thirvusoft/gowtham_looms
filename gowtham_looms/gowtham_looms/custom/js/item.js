frappe.ui.form.on("Item", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Publish in Website','Actions');
		},100);  
        if(frm.doc.__islocal == 1){
            setTimeout(() => {
                frm.remove_custom_button('Add / Edit Prices','Actions');
                frm.remove_custom_button('Stock Balance','View');
                frm.remove_custom_button('Stock Ledger','View');
                frm.remove_custom_button('Stock Projected Qty','View');
            },100); 
    }
    },
    item_group: function(frm){
        if(frm.doc.item_group == "Looms"){
            cur_frm.set_value('is_purchase_item',0)
        }
        else{
            cur_frm.set_value('is_purchase_item',1)
        }
    },
    abbr: function(frm) {
        cur_frm.set_value('abbr',frm.doc.abbr.toUpperCase())
        cur_frm.refresh()
    },
    
    
    
    
})
