frappe.ui.form.on("Item", {
    refresh: function(frm){
        frm.set_df_property('item_code','reqd',0);
        frm.set_df_property('delivered_by_supplier',1);
        frm.set_df_property('item_code','hidden',1);
        frm.set_df_property('naming_series','hidden',1)
        frm.set_df_property('inventory_section','collapsible',1)
        setTimeout(() => {
            frm.remove_custom_button('Duplicate');
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
            frm.set_value('is_purchase_item',0)
            frm.set_value('include_item_in_manufacturing',0)
            frm.refresh()
           
        }
        else{
            frm.set_value('is_purchase_item',1)
            frm.set_value('include_item_in_manufacturing',1)
            frm.refresh()
        }
    },
    abbr: function(frm) {
        frm.set_value('abbr',frm.doc.abbr.toUpperCase())
        frm.refresh()
    },
})
