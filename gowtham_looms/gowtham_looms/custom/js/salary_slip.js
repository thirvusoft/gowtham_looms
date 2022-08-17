frappe.ui.form.on('Salary Slip',{
    employee:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
            console.log("Mani")
            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = cur_frm.add_child('earnings');
                    child.salary_component = "Basic"
                    child.amount = r.message
                    console.log(r.message)

                }
                
            })
        }
      
    },
    start_date:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
            console.log("Mani")
            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = cur_frm.add_child('earnings');
                    child.salary_component = "Basic"
                    child.amount = r.message
                }
            })
        }
      
    },
    end_date:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
            console.log("Mani")
            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = cur_frm.add_child('earnings');
                    child.amount = r.message
                }
            })
        }
      
    }
})