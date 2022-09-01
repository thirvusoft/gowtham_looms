frappe.ui.form.on("Purchase Receipt", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Quality Inspection(s)','Create');
		},100);  
    },
    onload: function(frm){
        cur_frm.set_df_property('tax_id','hidden',1);

    }
  
})
