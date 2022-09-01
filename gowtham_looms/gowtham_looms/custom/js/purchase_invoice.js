frappe.ui.form.on("Purchase Invoice", {
    refresh: function(frm){
        cur_frm.set_df_property('tax_id','hidden',1);

    }
  
})
