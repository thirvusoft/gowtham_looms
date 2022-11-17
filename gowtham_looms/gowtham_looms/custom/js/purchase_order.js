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
                    var count =0
                    frm.set_value('items',[]);
                    r.message.forEach(element => {
                        var row = cur_frm.add_child('items')
                        frappe.model.set_value(row.doctype,row.name,'item_code',element.item_code)
                    });
                           
                } else{
                var count =0
                frm.set_value('items',[]);
            }
        }
        })
    },
    refresh: function(frm) {
		if (frm.doc.transaction_date && !frm.doc.schedule_date) {
            frappe.db.get_single_value('Buying Settings','lead_day').then((message) => {
            
            var a_year_from_start = frappe.datetime.add_days(frm.doc.transaction_date, message);
			frm.set_value("schedule_date", frappe.datetime.add_days(a_year_from_start, -1));
        
            });
		}
	}
  
})
