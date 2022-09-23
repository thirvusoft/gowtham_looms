frappe.ui.form.on("Item for Services", {
    item_code: function(frm,cdt,cdn){
        var row = locals[cdt][cdn]
        frappe.db.get_list("Item Price",{filters:{'price_list':'Standard Selling','item_code':row.item_code},fields:["price_list_rate"]}).then((data)=>{
            if(data.length){
                frappe.model.set_value(cdt,cdn,"rate",data[0].price_list_rate)
                cur_frm.refresh()
            }
            else{
                frappe.model.set_value(cdt,cdn,"rate",0)
                cur_frm.refresh()
            }
            calculate_amt(frm,cdt,cdn)
        })
     },
    qty: function(frm,cdt,cdn){
        calculate_amt(frm,cdt,cdn)
    },
    rate: function(frm,cdt,cdn){
        calculate_amt(frm,cdt,cdn)
    }
})

function calculate_amt(frm,cdt,cdn){
    var cal = locals[cdt][cdn]
    frappe.model.set_value(cdt,cdn,"amount",(cal.qty * cal.rate))
    var tot_item_price = 0;
    for(let i=0;i<frm.doc.ts_table.length;i++){
        if(frm.doc.ts_table[i].amount){
            tot_item_price = frm.doc.ts_table[i].amount + tot_item_price
            cur_frm.set_value("ts_item_for_service_cost",tot_item_price) 
        }

        
    }
}
frappe.ui.form.on("Maintenance Visit", {
    validate: function(frm){
        if(frm.doc.ts_table){ 
            if(frm.doc.ts_table.length) {
                calculate_amt(frm,frm.doc.ts_table[0].doctype,frm.doc.ts_table[0].name)
            }} 
    },
    on_submit(frm){
        frappe.call({
            method:"gowtham_looms.gowtham_looms.custom.py.sales_invoice.create_sales_invoice",
            args:{
                    doc : frm.doc
                },
            callback(si){
                frappe.model.sync(si.message);
				frappe.set_route('Form', si.message.doctype, si.message.name);
            }
        }) 
    }

}
)