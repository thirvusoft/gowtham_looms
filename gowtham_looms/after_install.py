from gowtham_looms.gowtham_looms.custom.py.designation import create_designation
from gowtham_looms.utils.stock.item import custom_fields
from gowtham_looms.utils.manufacture.production_plan import production_plan_custom_fields
from gowtham_looms.utils.property_setter import create_property_setter
from gowtham_looms.utils.manufacture.jobcard import jobcard_custom_fields
def after_install():
    create_designation()
    custom_fields()
    production_plan_custom_fields()
    create_property_setter()
    jobcard_custom_fields()
    
    
def execute():
    after_install()
    
    
