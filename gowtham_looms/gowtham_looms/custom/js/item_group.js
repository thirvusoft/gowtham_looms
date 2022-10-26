frappe.ui.form.on("Item Group", { 
    abbr: function(frm) {
        frm.set_value('abbr',frm.doc.abbr.toUpperCase())
        frm.refresh()
    },
})