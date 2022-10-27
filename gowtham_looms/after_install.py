from gowtham_looms.gowtham_looms.custom.py.designation import create_designation
from gowtham_looms.utils.stock.item import custom_fields
from gowtham_looms.utils.manufacture.production_plan import production_plan_custom_fields
from gowtham_looms.utils.property_setter import create_property_setter
from gowtham_looms.utils.manufacture.jobcard import jobcard_custom_fields
from gowtham_looms.utils.stock.item_group import item_group_custom_fields
from gowtham_looms.utils.stock.item_price import item_price_custom_fields
from gowtham_looms.utils.sales.sales_order import sales_order_custom_fields
from gowtham_looms.utils.hr.hr import employee_custom_fields
from gowtham_looms.utils.hr.salary_slip import salary_slip
from gowtham_looms.utils.sales.sales_invoice import sales_invoice_custom_fields
from gowtham_looms.utils.Accounting.bank_account import bank_account_custom_fields
from gowtham_looms.utils.hr.employee_advance import employee_advance_custom_fields
from gowtham_looms.utils.hr.payroll_entry import payroll
from gowtham_looms.gowtham_looms.custom.py.item_group import create_service_item_group
from gowtham_looms.gowtham_looms.custom.py.item import create_service_item
from gowtham_looms.utils.service.mainteance_visit import maintenance_visit_fields
from gowtham_looms.utils.hr.vehicle import batch_customizations
from gowtham_looms.utils.hr.vehicle_log import batch_customization
from gowtham_looms.utils.hr.driver import driver_custom_fields
def after_install():
    create_designation()
    custom_fields()
    production_plan_custom_fields()
    create_property_setter()
    jobcard_custom_fields()
    item_group_custom_fields()
    item_price_custom_fields()
    sales_order_custom_fields()
    employee_custom_fields()
    bank_account_custom_fields()
    salary_slip()
    sales_invoice_custom_fields()
    employee_advance_custom_fields()
    payroll()
    create_service_item_group()
    create_service_item()
    maintenance_visit_fields()
    batch_customizations()
    batch_customization()
    driver_custom_fields()

def execute():
    after_install()
    
    
