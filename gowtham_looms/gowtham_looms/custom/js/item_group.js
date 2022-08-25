frappe.ui.form.on("Item Group", { 
    abbr: function(frm) {
        cur_frm.set_value('abbr',frm.doc.abbr.toUpperCase())
        cur_frm.refresh()
    },
})