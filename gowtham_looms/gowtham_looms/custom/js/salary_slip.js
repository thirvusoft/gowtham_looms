frappe.ui.form.on('Salary Slip',{
    employee:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
            
            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = frm.add_child('earnings');
                    child.salary_component = "Basic"
                    child.amount = r.message
                    cur_frm.refresh()
                }
                
            })
        }
        else{
            frm.set_value("earnings",[])
        }
      
    },
    start_date:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){

            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = frm.add_child('earnings');
                    child.salary_component = "Basic"
                    child.amount = r.message
                    cur_frm.refresh()
                }
            })
        }
        else{
            frm.set_value("earnings",[])
        }
      
    },
    end_date:function(frm,cdn,cdt){
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
    
            frappe.call({
                method : "gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_salary",
                args :{
                    employee:frm.doc.employee,
                    start_date:frm.doc.start_date,
                    end_date:frm.doc.end_date,   
                },
                callback:function(r){
                    var child = frm.add_child('earnings');
                    child.salary_component = "Basic"
                    child.amount = r.message
                    cur_frm.refresh()
                }
            })
        }
        else{
            frm.set_value("earnings",[])
        }
      
    }
})