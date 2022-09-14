var balance_amount = 0;
frappe.ui.form.on('Salary Slip',{
    employee:function(frm,cdn,cdt){
        frappe.db.get_value("Employee", {"name": frm.doc.employee}, "advance1_salary", (r) => {
            balance_amount=r.advance1_salary 
            frm.set_value('balance_amount',r.advance1_salary) 
            
        });
        
        if(frm.doc.employee && frm.doc.start_date && frm.doc.end_date && frm.doc.designation){
            
            get_employee_advance(frm)
            
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
                    child.amount_to_pay = r.message
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
            get_employee_advance(frm)
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
                    child.amount_to_pay = r.message
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
            get_employee_advance(frm)
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
                    child.amount_to_pay = r.message
                    cur_frm.refresh()
                }
            })
        }
        else{
            frm.set_value("earnings",[])
        }
        
    },
    pay_the_balace: function(frm){
        
            for(let i=0;i<frm.doc.earnings.length;i++){
                if(frm.doc.pay_the_balace == 1){
                frm.doc.earnings[i].amount_to_pay  += frm.doc.balance1_amount
                frm.doc.earnings[i].amount  += frm.doc.balance1_amount
                frm.doc.total_paid_amount += frm.doc.balance1_amount
                cur_frm.set_value("balance_amount",0)
                }
                else{
                    frm.doc.earnings[i].amount_to_pay  -= frm.doc.balance1_amount
                    frm.doc.earnings[i].amount  -= frm.doc.balance1_amount
                    frm.doc.total_paid_amount -= frm.doc.balance1_amount
                    cur_frm.set_value("balance_amount",frm.doc.balance1_amount)
                }
            frm.refresh_field("earnings")
            }
        
      
        
    },
    refresh: function(frm){
        var tot_amt = 0;
        if(frm.doc.__unsaved == 1){
        if(frm.doc.pay_the_balace == 1){
            tot_amt = frm.doc.balance1_amount
        }
        if(frm.doc.earnings){
        for(let i=0;i<frm.doc.earnings.length;i++){
            tot_amt = frm.doc.earnings[i].amount_to_pay + tot_amt
        }
        cur_frm.set_value("total_amt",tot_amt)
        frm.set_value('total_amt',frm.doc.total_amt-frm.doc.total_advance_amount)
    }
}
    },

    get_emp_advance: function(frm){
        
        frappe.call({
            method: 'gowtham_looms.gowtham_looms.custom.py.salary_slip.get_advance_amounts',
            args:{employee:frm.doc.employee},
            callback(r){
                if (r.message[0]) {
                    let count = 0
                    var func = function () {
                        var tot_amt = 0;
                        for (let i = 0; i < r.message[1]; i++) {
                            tot_amt += d.fields_dict['amt_take' + i].value
                        }
                        d.fields_dict['total_amount'].value = tot_amt
                        d.fields_dict['total_amount'].refresh()

                    }
                    r.message[0].forEach((data) => {
                        if (data['fieldname'].indexOf('amt_take') >= 0) {
                            r.message[0][count]['onchange'] = func
                        }
                        count += 1
                    })
                var d = new frappe.ui.Dialog({
                    title:'Employee Advance',
                    fields:r.message[0],
                    primary_action(data){
                        frappe.call({
                            method: 'gowtham_looms.gowtham_looms.custom.py.salary_slip.change_remaining_amount',
                            args: {data: data, length: r.message[1]},
                            callback(r1){
                                r1.message.forEach((data)=>{
                                    var adv = frm.add_child('deductions')
                                    adv.salary_component = data.salary_component
                                    adv.amount = data.amount
                                    adv.employee_advance = data.employee_advance
                                })
                                
                                frm.refresh_field('deductions')
                                d.hide()
                            }
                        })
                    }
                })
                d.show()
            }
        }
        })
    },
})

frappe.ui.form.on('Salary Detail',{
    amount:function(frm){
        var balance_amount = 0;
        var amount_pay = 0;
        for(let i=0;i<frm.doc.earnings.length;i++){
            amount_pay = frm.doc.earnings[i].amount + amount_pay 
            balance_amount = (frm.doc.earnings[i].amount_to_pay - frm.doc.earnings[i].amount) + balance_amount
            cur_frm.set_value("total_paid_amount",amount_pay) 
            cur_frm.set_value("total_unpaid_amount",balance_amount) 
            
             
        
        }
    },

})

function get_employee_advance(frm){
    frappe.call({
        method:"gowtham_looms.gowtham_looms.custom.py.salary_slip.get_employee_advance_amount",
        args:{
            name: frm.doc.employee,
            start_date:frm.doc.start_date,
            end_date: frm.doc.end_date
        },
        callback(r){
            frm.set_value('total_advance_amount', r.message)
            frm.refresh_field('total_advance_amount')
        }
    })
}

