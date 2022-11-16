frappe.ui.form.on("Stock Reconciliation Item", {
    item_code: function(frm, cdt, cdn){
        var row = locals[cdt][cdn]
        frappe.db.get_list('Item Default', {filters:{'parent':row.item_code}, fields:['default_warehouse']}).then((message) => {
            frappe.model.set_value(cdt, cdn,'warehouse',message[0].default_warehouse);
        })
        
    }, 
    
})
frappe.ui.form.on("Stock Reconciliation",{
    company: function(frm){
        frappe.call({
            method: "gowtham_looms.gowtham_looms.custom.py.stock_reconciliation.stock_reconciliation_item",
            args:{
                company:frm.doc.company,
            },
            callback: function(r) {
                frm.set_value('items',r.message);
                frm.refresh()
            }
        })
    }
})