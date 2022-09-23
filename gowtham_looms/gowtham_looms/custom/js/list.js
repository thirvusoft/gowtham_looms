// frappe.listview_settings['Maintenance Visit'] = {
//     get_indicator: function(doc) {
//         var colors = {
//             "Unpaid": "red",
//             "Paid": "green",
//             "Partially Paid": "yellow",
//         }
//         return [__(doc.payment_status), colors[doc.payment_status], "payment_status,=," + doc.payment_status];
//     },
// } 