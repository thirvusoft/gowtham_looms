from gowtham_looms.gowtham_looms.custom.py.designation import create_designation
from gowtham_looms.utils.stock.item import custom_fields

def after_install():
    create_designation()
    custom_fields()