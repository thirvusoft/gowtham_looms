frappe.ui.form.on("Job Card", {
    refresh: function(frm){
        setTimeout(() => {
			frm.remove_custom_button('Corrective Job Card','Make');
		},100);  
    },
    onload: function(frm){
        if(frm.doc.doc_onload == 0){
        frm.set_value('time_logs',[])
        frm.set_value('doc_onload',1)
        frm.refresh()
        }}
})
