console.log("===========")
frappe.ui.form.on("Sales Order Item", {
    item_code: function(frm, cdt, cdn){
        var row = locals[cdt][cdn]
        frappe.db.get_list('Item Variant Attribute', {filters:{parentfield:"attributes",parenttype:"Item",parent:row.item_code,attribute:"Width"}, fields:['attribute_value']}).then((message) => {
            frappe.model.set_value(cdt, cdn,'ts_size',message[0].attribute_value);
            
        })
        
    },
})