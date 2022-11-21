import frappe 
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def create_property_setter():
    company = frappe.db.get_single_value("Global Defaults","default_company")
    abbr = frappe.db.get_value("Company",company,"abbr")
    # Item Property Setter
    make_property_setter('Item','section_break_11','hidden', 1, 'Check')
    make_property_setter('Item','sb_barcodes','hidden', 1, 'Check')
    make_property_setter('Item','weight_uom','hidden', 1, 'Check')
    make_property_setter('Item','valuation_method','hidden', 1, 'Check')
    make_property_setter('Item','unit_of_measure_conversion','hidden', 1, 'Check')
    make_property_setter('Item','serial_nos_and_batches','hidden', 0, 'Check')
    make_property_setter('Item','has_batch_no','hidden', 1, 'Check')
    make_property_setter('Item','is_item_from_hub','hidden', 1, 'Check')
    make_property_setter('Item','image','hidden', 0, 'Check')
    make_property_setter('Item','defaults','collapsible', 1, 'Check')
    make_property_setter('Item','variants_section','hidden', 0, 'Check')
    make_property_setter('Item','supplier_details','hidden', 0, 'Check')
    make_property_setter('Item','delivered_by_supplier','hidden', 0, 'Check')
    make_property_setter('Item','column_break2','hidden', 1, 'Check')
    make_property_setter('Item','foreign_trade_details','hidden', 1, 'Check')
    make_property_setter('Item','deferred_revenue','hidden', 1, 'Check')
    make_property_setter('Item','shelf_life_in_days','hidden', 1, 'Check')
    make_property_setter('Item','end_of_life','hidden', 1, 'Check')
    make_property_setter('Item','deferred_expense_section','hidden', 1, 'Check')
    make_property_setter('Item','customer_details','hidden', 1, 'Check')
    make_property_setter('Item','min_order_qty','hidden', 1, 'Check')
    make_property_setter('Item','safety_stock','hidden', 1, 'Check')
    make_property_setter('Item','lead_time_days','hidden', 0, 'Check')
    make_property_setter('Item','is_customer_provided_item','hidden', 1, 'Check')
    make_property_setter('Item','grant_commission','hidden', 1, 'Check')
    make_property_setter('Item','max_discount','hidden', 1, 'Check')
    make_property_setter('Item','item_tax_section_break','hidden', 1, 'Check')
    make_property_setter('Item','inspection_criteria','hidden', 1, 'Check')
    make_property_setter('Item','manufacturing','hidden', 1, 'Check')
    make_property_setter('Item','weight_per_unit','hidden', 1, 'Check')
    make_property_setter('Item','hub_publishing_sb','hidden', 1, 'Check')
    make_property_setter('Item','more_information_section','hidden', 1, 'Check')
    make_property_setter('Item','item_code','reqd',0,'Check')
    make_property_setter('Item','ts_cmpy_abbr','hidden', 1, 'Check')
    make_property_setter('Item','inventory_section','collapsible_depends_on', "", 'Text Editor')
    make_property_setter('Item','naming_series','read_only', 1, 'Check')
    make_property_setter('Item','naming_series','default','','Text Editor')
    make_property_setter('Item','naming_series','options',f'\nSTO-ITEM-.YYYY.-\n{{abbrevation}}.##.-.{{ts_type}}','Text Editor')
    make_property_setter('Item','naming_series','default',f'{{abbrevation}}.##.-.{{ts_type}}','Text Editor')
    make_property_setter('Item','allow_alternative_item','depends_on', "eval:doc.is_purchase_item=='1'", 'Text Editor')
    make_property_setter('Item','reorder_section','depends_on', "eval:doc.is_purchase_item=='1'", 'Text Editor')
    make_property_setter('Item','standard_rate','depends_on', "eval:doc.is_sales_item=='1'", 'Text Editor')
    make_property_setter('Item','warranty_period','depends_on', "eval:doc.is_sales_item=='1'", 'Text Editor')
    make_property_setter('Item','over_delivery_receipt_allowance','hidden', 1, 'Check')
    make_property_setter('Item','over_billing_allowance','hidden', 1, 'Check')
    make_property_setter('Item','purchase_details','hidden',1,'Check')
    make_property_setter('Item','is_nil_exempt','hidden',1,'Check')
    make_property_setter('Item','gl_old_group','hidden',1,'Check')
    make_property_setter('Item','allow_alternative_item','hidden',1,'check')
    make_property_setter('Item',"",'autoname',"naming_series:",'Text',for_doctype=1)
    make_property_setter('Item Reorder','warehouse_reorder_qty','default',1,'Text Editor') 
    # Item Group Property Setter
    make_property_setter('Item Group','sb9','hidden', 1, 'Check')
    make_property_setter('Item Group','defaults','hidden', 1, 'Check')
    make_property_setter('Item Group','sec_break_taxes','collapsible', 1, 'Check')
    # Item Price Property Setter
    make_property_setter('Item Price','packing_unit','hidden', 1, 'Check')
    make_property_setter('Item Price','customer','hidden', 1, 'Check')
    make_property_setter('Item Price','batch_no','hidden', 1, 'Check')
    make_property_setter('Item Price','currency','hidden', 1, 'Check')
    make_property_setter('Item Price','valid_from','hidden', 1, 'Check')
    make_property_setter('Item Price','valid_upto','hidden', 1, 'Check')
    make_property_setter('Item Price','lead_time_days','hidden', 1, 'Check')
    make_property_setter('Item Price','note','hidden', 1, 'Check')
    make_property_setter('Item Price','reference','hidden', 1, 'Check')
    make_property_setter('Item Price','price_list_details','collapsible', 1, 'Check')
    make_property_setter('Item Price','supplier','hidden', 1, 'Check')
    # Stock Reconsoliation
    make_property_setter('Stock Reconciliation','expense_account','depends_on', '!company', 'Text Editor')
    make_property_setter('Stock Reconciliation','cost_center','hidden',1,'Check')
    make_property_setter('Stock Reconciliation','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Stock Reconciliation','cost_center','depends_on', '!company', 'Text Editor')
    make_property_setter('Salary Structure Assignment','base','hidden', 1, 'Check')
    make_property_setter('Salary Structure Assignment','variable','hidden', 1, 'Check')
    make_property_setter('Salary Component','condition_and_formula','hidden', 1, 'Check')
    # BOM Property Setter
    make_property_setter('BOM','project','hidden', 1, 'Check')
    make_property_setter('BOM','currency_detail','hidden', 0, 'Check')
    make_property_setter('BOM','materials_section','hidden', 1, 'Check')
    make_property_setter('BOM','scrap_section','hidden', 1, 'Check')
    make_property_setter('BOM','website_section','hidden', 1, 'Check')
    make_property_setter('BOM','routing','hidden', 1, 'Check')
    make_property_setter('BOM','section_break_25','hidden', 1, 'Check')
    make_property_setter('BOM','with_operations','default', 1, 'Check')
    make_property_setter('BOM','with_operations','hidden', 1, 'Check')
    make_property_setter('BOM','transfer_material_against','hidden', 1, 'Check')
    make_property_setter('BOM','currency','reqd', 0, 'Check')
    make_property_setter('BOM','currency','hidden', 1, 'Check')
    make_property_setter('BOM','is_active','hidden', 1, 'Check')
    make_property_setter('BOM','is_default','hidden', 1, 'Check')
    make_property_setter('BOM','set_rate_of_sub_assembly_item_based_on_bom','hidden', 1, 'Check')
    #BOM Operation
    make_property_setter('BOM Operation','time_in_mins','default', 5, 'Text Editor')
    # Production Plan Property Setter
    make_property_setter('Production Plan', 'get_sub_assembly_items', 'hidden', 0, 'Check')
    make_property_setter('Production Plan', 'sub_assembly_items', 'hidden', 0, 'Check')
    make_property_setter('Production Plan','get_items_from','options','\nSales Order','Text Editor')
    make_property_setter('Production Plan', 'item_code', 'hidden', 1, 'Check')
    make_property_setter('Production Plan', 'customer', 'hidden', 1, 'Check')
    make_property_setter('Production Plan', 'project', 'hidden', 1, 'Check')
    make_property_setter('Production Plan','select_items_to_manufacture_section','collapsible', 1, 'Check')
    make_property_setter('Production Plan','material_request_planning','collapsible', 1, 'Check')
    # Workorder Property Setter
    make_property_setter('Work Order','production_plan_item','hidden', 1, 'Check')
    make_property_setter('Work Order','project','hidden', 1, 'Check')
    make_property_setter('Work Order','scrap_warehouse','hidden', 1, 'Check')
    make_property_setter('Work Order','use_multi_level_bom','hidden', 1, 'Check')
    make_property_setter('Work Order','update_consumed_material_cost_in_project','hidden', 1, 'Check')
    make_property_setter('Work Order','settings_section','collapsible', 1, 'Check')
    make_property_setter('Work Order','warehouses','collapsible', 1, 'Check')
    make_property_setter('Work Order','required_items_section','collapsible', 1, 'Check')
    make_property_setter('Work Order','time','collapsible', 1, 'Check')
    
    # Job Card Property Setter
    make_property_setter('Job Card','quality_inspection_template','hidden', 1, 'Check')
    make_property_setter('Job Card','quality_inspection','hidden', 1, 'Check')
    make_property_setter('Job Card','project','hidden', 1, 'Check')
    make_property_setter('Job Card','batch_no','hidden', 1, 'Check')
    make_property_setter('Job Card','serial_no','hidden', 1, 'Check')
    make_property_setter('Job Card','scrap_items_section','hidden', 1, 'Check')
    make_property_setter('Job Card','more_information','hidden', 1, 'Check')
    make_property_setter('Job Card','employee','hidden', 1, 'Check')
    make_property_setter('Job Card','operation_section_section','collapsible', 1, 'Check')
    make_property_setter('Job Card','timing_detail','collapsible', 1, 'Check')
    make_property_setter('Job Card','section_break_8','collapsible', 1, 'Check')
    make_property_setter('Job Card','production_section','collapsible', 1, 'Check')
    # Sales Order Property Setter
    make_property_setter('Sales Order','scan_barcode','hidden', 1, 'Check')
    make_property_setter('Sales Order','terms_section_break','hidden', 1, 'Check')
    make_property_setter('Sales Order','more_info','hidden', 1, 'Check')
    make_property_setter('Sales Order','printing_details','hidden', 1, 'Check')
    make_property_setter('Sales Order','section_break_78','hidden', 1, 'Check')
    make_property_setter('Sales Order','sales_team_section_break','hidden', 1, 'Check')
    make_property_setter('Sales Order','section_break1','hidden', 1, 'Check')
    make_property_setter('Sales Order','subscription_section','hidden', 1, 'Check')
    # Stock Entry Property Setter
    make_property_setter('Stock Entry','inspection_required','hidden', 1, 'Check')
    make_property_setter('Stock Entry','project','hidden',1,'Check')
    make_property_setter('Stock Entry','printing_settings','hidden', 1, 'Check')
    make_property_setter('Stock Entry','scan_barcode','hidden', 1, 'Check')
    make_property_setter('Stock Entry','apply_putaway_rule','hidden',1,'Check')
    make_property_setter('Stock Entry','target_warehouse_address','hidden',1,'Check')
    make_property_setter('Stock Entry','source_warehouse_address','hidden',1,'Check')
    make_property_setter('Stock Entry','remarks','hidden',1,'Check')
    # make_property_setter('Stock Entry','additional_costs_section','depends_on','eval:doc.total_additional_costs','Text Editor') 
    # Purchase Order Property Setter
    make_property_setter('Purchase Order','column_break5','hidden', 1, 'Check')
    make_property_setter('Purchase Order','subscription_section','hidden', 1, 'Check')
    make_property_setter('Purchase Order','more_info','hidden', 1, 'Check')
    make_property_setter('Purchase Order','scan_barcode','hidden', 1, 'Check')
    make_property_setter('Purchase Order','terms_section_break','hidden',0,'Check')
    make_property_setter('Purchase Order','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Purchase Order','project','hidden',1,'Check')
    make_property_setter('Purchase Order','currency_and_price_list','hidden',1,'Check')
    make_property_setter('Purchase Order','sec_warehouse','hidden',0,'Check')
    make_property_setter('Purchase Order','total_net_weight','hidden',1,'Check')
    make_property_setter('Purchase Order','shipping_rule','hidden',1,'Check')
    make_property_setter('Purchase Order','discount_section','hidden',1,'Check')
    make_property_setter('Purchase Order','naming_series','read_only',1,'Check')
    make_property_setter('Purchase Order','cost_center','hidden',1,'Check')
    make_property_setter('Purchase Order','totals_section','collapsible',1,'Check')
    make_property_setter('Purchase Order','schedule_date','label','Required Date','Data')
    # Purchase Receipt Property Setter
    make_property_setter('Purchase Receipt','more_info','hidden', 1, 'Check')
    make_property_setter('Purchase Receipt','scan_barcode','hidden', 1, 'Check')
    make_property_setter('Purchase Receipt','subscription_detail','hidden',1,'Check')
    make_property_setter('Purchase Receipt','printing_settings','hidden',1,'Check')
    make_property_setter('Purchase Receipt','terms_section_break','hidden',1,'Check')
    make_property_setter('Purchase Receipt','is_return','depends_on','eval:!doc.__islocal','Text Editor')
    make_property_setter('Purchase Receipt','apply_putaway_rule','hidden',1,'Check')
    make_property_setter('Purchase Receipt','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Purchase Receipt','project','hidden',1,'Check')
    make_property_setter('Purchase Receipt','currency_and_price_list','hidden',1,'Check')
    make_property_setter('Purchase Receipt','shipping_rule','hidden',1,'Check')
    make_property_setter('Purchase Receipt','section_break_42','hidden',0,'Check')
    make_property_setter('Purchase Receipt','is_subcontracted','hidden',0,'Check')
    make_property_setter('Purchase Receipt','raw_material_details','hidden',1,'Check')
    make_property_setter('Purchase Receipt','lr_date','hidden',1,'Check')
    make_property_setter('Purchase Receipt','total_net_weight','hidden',1,'Check')
    make_property_setter('Purchase Receipt','cost_center','hidden',1,'Check')
    # Purchase Invoice Property Setter
    make_property_setter('Purchase Invoice','scan_barcode','hidden', 1, 'Check')
    make_property_setter('Purchase Invoice','terms_section_break','hidden',1,'Check')
    make_property_setter('Purchase Invoice','printing_settings','hidden',1,'Check')
    make_property_setter('Purchase Invoice','more_info','hidden',1,'Check')
    make_property_setter('Purchase Invoice','tax_id','hidden',1,'Check')
    make_property_setter('Purchase Invoice','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Purchase Invoice','currency_and_price_list','hidden',1,'Check')
    make_property_setter('Purchase Invoice','project','hidden',1,'Check')
    make_property_setter('Purchase Invoice','is_subcontracted','hidden',0,'Check')
    make_property_setter('Purchase Invoice','shipping_rule','hidden',1,'Check')
    make_property_setter('Purchase Invoice','gst_section','hidden',1,'Check')
    make_property_setter('Purchase Invoice','section_break_44','depends_on','eval:doc.discount_amount','Text Editor')
    make_property_setter('Purchase Invoice','cost_center','hidden',1,'Check')
    make_property_setter('Purchase Invoice','is_return','depends_on','eval:!doc.__islocal','Text Editor')
    make_property_setter('Purchase Invoice','total_net_weight','hidden',1,'Check')
    make_property_setter('Purchase Invoice','subscription_section','hidden',1,'Check')
    make_property_setter('Purchase Invoice','accounting_details_section','hidden',1,'Check')
    # Sales Invoice Property Setter
    make_property_setter('Sales Invoice','terms_section_break','hidden',1,'Check')
    make_property_setter('Sales Invoice','edit_printing_settings','hidden',1,'Check')
    make_property_setter('Sales Invoice','more_information','hidden',1,'Check')
    make_property_setter('Sales Invoice','sales_team_section_break','hidden',1,'Check')
    make_property_setter('Sales Invoice','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Sales Invoice','project','hidden',1,'Check')
    make_property_setter('Sales Invoice','shipping_rule','hidden',1,'Check')
    make_property_setter('Sales Invoice','section_break_49','depends_on','eval:doc.discount_amount','Text Editor')
    make_property_setter('Sales Invoice','gst_section','hidden',1,'Check')
    make_property_setter('Sales Invoice','cost_center','hidden',1,'Check')
    make_property_setter('Sales Invoice','scan_barcode','hidden',1,'Check')
    make_property_setter('Sales Invoice','time_sheet_list','hidden',1,'Check')
    make_property_setter('Sales Invoice','total_taxes_and_charges','hidden',1,'Check')
    make_property_setter('Sales Invoice','loyalty_points_redemption','hidden',1,'Check')
    make_property_setter('Sales Invoice','section_break2','hidden',1,'Check')   
    make_property_setter('Sales Invoice','more_info','hidden',1,'Check')
    make_property_setter('Sales Invoice','items_section','collapsible',1,'Check')
    make_property_setter('Sales Invoice','is_pos','hidden',1,'Check')
    # Material Request Property Setter
    make_property_setter('Material Request','schedule_date','label','Required Date','Data')
    make_property_setter('Material Request','scan_barcode','hidden',1,'Check')
    make_property_setter('Material Request','printing_details','hidden',1,'Check')
    make_property_setter('Material Request','terms_section_break','hidden',1,'Check')
    make_property_setter('Material Request','naming_series','read_only',1,'Check')
    make_property_setter('Material Request','material_request_type','options','Purchase\nMaterial Transfer\nMaterial Issue\nManufacture','Text Editor')
    # Sales Order Property Setter
    make_property_setter('Sales Order','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Sales Order','project','hidden',1,'Check')
    make_property_setter('Sales Order','currency_and_price_list','hidden',1,'Check')
    make_property_setter('Sales Order','shipping_rule','hidden',1,'Check')
    make_property_setter('Sales Order','set_warehouse','default',f'Finished Goods - {abbr}','Text Editor')
    make_property_setter('Sales Order','set_warehouse','hidden',0,'Check')
    make_property_setter('Sales Order','cost_center','hidden',1,'Check')
    make_property_setter('Sales Order','section_break_48','label','Additional Discount','Data')
    make_property_setter('Sales Order','order_type','options','\nSales\nMaintenance','Text Editor')
    make_property_setter('Sales Order','total_net_weight','hidden',1,'Check')
    make_property_setter('Sales Order','total_taxes_and_charges','hidden',1,'Check')
    make_property_setter('Sales Order','payment_schedule_section','collapsible',1,'Check')
    # Delivery Note Property Setter
    make_property_setter('Delivery Note','is_return','depends_on','eval:!doc.__islocal','Text Editor')
    make_property_setter('Delivery Note','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Delivery Note','project','hidden',1,'Check')
    make_property_setter('Delivery Note','currency_and_price_list','hidden',1,'Check')
    make_property_setter('Delivery Note','scan_barcode','hidden',1,'Check')
    make_property_setter('Delivery Note','shipping_rule','hidden',1,'Check')
    make_property_setter('Delivery Note','section_break_49','hidden',1,'Check')
    make_property_setter('Delivery Note','terms_section_break','hidden',1,'Check')
    make_property_setter('Delivery Note','printing_details','hidden',1,'Check')
    # Journal Entry Property Setter
    make_property_setter('Journal Entry','printing_details','hidden',1,'Check')
    make_property_setter('Journal Entry','user_remark','hidden',1,'Check')
    # Payment Terms Property Setter
    make_property_setter('Payment Term','description','hidden',1,'Check')
    make_property_setter('Payment Term','section_break_8','collapsible',1,'Check')
    #salary slip property setter
    make_property_setter('Salary Slip','total_principal_amount','hidden',1,'Check')
    make_property_setter('Salary Slip','total_loan_repayment','hidden',1,'Check')
    make_property_setter('Salary Slip','total_interest_amount','hidden',1,'Check')
    make_property_setter('Salary Slip','deduct_tax_for_unclaimed_employee_benefits','hidden',1,'Check')
    make_property_setter('Salary Slip','deduct_tax_for_unsubmitted_tax_exemption_proof','hidden',1,'Check')
    make_property_setter('Salary Slip','salary_slip_based_on_timesheet','hidden',1,'Check')
    make_property_setter('Salary Detail','amount','label','Amount To Pay','Data')
    make_property_setter('Salary Slip','letter_head','hidden',1,'Check')
    # Salary Structure Property Setter
    make_property_setter('Salary Structure','salary_slip_based_on_timesheet','hidden',1,'Check')
    make_property_setter('Salary Structure','conditions_and_formula_variable_and_example','hidden',1,'Check')
    make_property_setter('Salary Structure','letter_head','hidden',1,'Check')
    # Employee Property Setter
    make_property_setter('Employee','exit','hidden',0,'Check')
    make_property_setter('Employee','history_in_company','hidden',1,'Check')
    make_property_setter('Employee','previous_work_experience','hidden',1,'Check')
    make_property_setter('Employee','educational_qualification','hidden',1,'Check')
    make_property_setter('Employee','health_insurance_section','hidden',1,'Check')
    make_property_setter('Employee','erpnext_user','label','Thirvusoft User','Data')
    make_property_setter('Employee','approvers_section','collapsible',1,'Check')
    make_property_setter('Employee','holiday_list','reqd',1,'Check')
    make_property_setter('Employee','emergency_contact_details','collapsible',1,'Check')
    make_property_setter('Employee','resignation_letter_date','hidden',1,'Check')
    make_property_setter('Employee','leave_encashed','hidden',1,'Check')
    make_property_setter('Employee','encashment_date','hidden',1,'Check')
    make_property_setter('Employee','exit_interview_details','hidden',1,'Check')
    make_property_setter('Employee','held_on','hidden',1,'Check')
    make_property_setter('Employee','new_workplace','hidden',1,'Check')
    make_property_setter('Employee','feedback','hidden',1,'Check')
    make_property_setter('Employee','passport_number','hidden',1,'Check')
    make_property_setter('Employee','date_of_issue','hidden',1,'Check')
    make_property_setter('Employee','valid_upto','hidden',1,'Check')
    make_property_setter('Employee','place_of_issue','hidden',1,'Check')
    make_property_setter('Employee','default_shift','hidden',1,'Check')
    make_property_setter('Employee','shift_request_approver','hidden',1,'Check')
    make_property_setter('Employee','grade','hidden',1,'Check')
    make_property_setter('Employee','employment_details','hidden',1,'Check')
    make_property_setter('Employee','middle_name','hidden',1,'Check')
    make_property_setter('Employee','unsubscribed','hidden',1,'Check')
    make_property_setter('Employee','sb53','hidden',1,'Check')
    # Attendance Property Setter
    make_property_setter('Attendance','details_section','hidden',1,'Check')
    # Customer Property Setter
    make_property_setter('Customer','primary_address_and_contact_detail','collapsible',1,'Check')
    make_property_setter('Customer','default_receivable_accounts','hidden',1,'Check')
    make_property_setter('Customer','default_receivable_accounts','hidden',1,'Check')
    make_property_setter('Customer','more_info','hidden',1,'Check')
    make_property_setter('Customer','column_break_38','hidden',1,'Check')
    make_property_setter('Customer','sales_team_section_break','hidden',0,'Check')
    make_property_setter('Customer','sales_team_section','hidden',1,'Check')
    # Supplier Property Setter
    make_property_setter('Supplier','primary_address_and_contact_detail_section','collapsible',1,'Check')
    make_property_setter('Supplier','column_break2','hidden',1,'Check')
    make_property_setter('Supplier','warn_rfqs','hidden',1,'Check')
    make_property_setter('Supplier','warn_pos','hidden',1,'Check')
    make_property_setter('Supplier','prevent_rfqs','hidden',1,'Check')
    make_property_setter('Supplier','prevent_pos','hidden',1,'Check')
    # Address Property Setter
    make_property_setter('Address','linked_with','collapsible',1,'Check')
    # Contact Property Setter
    make_property_setter('Contact','more_info','hidden',1,'Check')
    make_property_setter('Contact','contact_details','collapsible',1,'Check')
    make_property_setter('Contact','sb_01','collapsible',1,'Check')
    make_property_setter('Contact','middle_name','hidden',1,'Check')
    # Maintenance Visit Property Setter
    make_property_setter('Maintenance Visit','status','reqd',0,'Check')
    make_property_setter('Maintenance Visit','status','hidden',1,'Check')
    make_property_setter('Maintenance Visit','contact_info_section','collapsible',1,'Check')
    make_property_setter('Maintenance Visit','more_info','collapsible',1,'Check')
    make_property_setter('Maintenance Schedule','contact_info','collapsible',1,'Check')
    make_property_setter('Warranty Claim','issue_details','collapsible',1,'Check')
    make_property_setter('Warranty Claim','resolution_section','collapsible',1,'Check')
    make_property_setter('Warranty Claim','serial_no','hidden',0,'Check')
    # Payroll Entry Property Setter
    make_property_setter('Payroll Entry','cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Payroll Entry','project','hidden',1,'Check')
    make_property_setter('Payroll Entry','cost_center','hidden',1,'Check')
    make_property_setter('Payroll Entry','salary_slip_based_on_timesheet','hidden',1,'Check')
    make_property_setter('Payroll Entry','section_break_8','collapsible',1,'Check')
    make_property_setter('Payroll Entry','select_payroll_period','collapsible',1,'Check')
    make_property_setter('Payroll Entry','account','collapsible',1,'Check')
    # Payment Entry Property Setter
    make_property_setter("Payment Entry","payment_amounts_section",'collapsible',1,'Check')
    make_property_setter("Payment Entry","party_section",'collapsible',1,'Check')
    make_property_setter("Payment Entry","section_break_14",'collapsible',1,'Check')
    make_property_setter("Payment Entry","section_break_34",'collapsible',1,'Check')
    make_property_setter("Payment Entry",'cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Payment Entry','cost_center','hidden',1,'Check')
    make_property_setter("Payment Entry","subscription_section",'collapsible',1,'Check')
    # Assets Property Setter
    make_property_setter("Asset",'cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Asset','cost_center','hidden',1,'Check')
    make_property_setter("Asset Repair",'cost_center','fetch_from','company.cost_center','Text Editor')
    make_property_setter('Asset Repair','cost_center','hidden',1,'Check')
    make_property_setter('Asset Repair','project','hidden',1,'Check')
    # Driver Property Setter
    make_property_setter('Driver','transporter','hidden',1,'Check')
    
def execute():
    create_property_setter()