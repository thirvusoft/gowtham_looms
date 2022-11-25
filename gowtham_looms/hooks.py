from . import __version__ as app_version

app_name = "gowtham_looms"
app_title = "Gowtham Looms"
app_publisher = "Thirvusoft"
app_description = "Manufacturing Looms"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "thirvusoft@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gowtham_looms/css/gowtham_looms.css"
# app_include_js = "/assets/gowtham_looms/js/gowtham_looms.js"

# include js, css files in header of web template
# web_include_css = "/assets/gowtham_looms/css/gowtham_looms.css"
# web_include_js = "/assets/gowtham_looms/js/gowtham_looms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gowtham_looms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"Maintenance Visit" : "/gowtham_looms/custom/js/list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gowtham_looms.install.before_install"
after_install = "gowtham_looms.after_install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gowtham_looms.uninstall.before_uninstall"
# after_uninstall = "gowtham_looms.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gowtham_looms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Production Plan": "gowtham_looms.gowtham_looms.custom.py.productionplan.productionplan",
	"Job Card": "gowtham_looms.gowtham_looms.custom.py.jobcard.jobcard"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	'Item Group':{
		"validate":"gowtham_looms.gowtham_looms.custom.py.item_group.validate",
		
	},
	'Salary Slip':{
		"validate":["gowtham_looms.gowtham_looms.custom.py.salary_slip.paid_amount",
					"gowtham_looms.gowtham_looms.custom.py.salary_slip.payroll"],
		"on_submit":"gowtham_looms.gowtham_looms.custom.py.salary_slip.adv_amount",
		"on_cancel":"gowtham_looms.gowtham_looms.custom.py.salary_slip.emp_balance_amt"	
	},
	'Payroll Entry':{
		"validate" : "gowtham_looms.gowtham_looms.custom.py.payroll_entry.payroll_advance_amount"
	},
	# 'Maintenance Visit' :{
	# 	"validate" : "gowtham_looms.gowtham_looms.custom.py.sales_invoice.create_sales_invoice"
	# },
	'Payment Entry' :{
		"on_submit" : "gowtham_looms.gowtham_looms.custom.py.sales_invoice.change_mv_status",
		"on_cancel" : "gowtham_looms.gowtham_looms.custom.py.sales_invoice.change_mv_status"
	},
	'Item Price' : {
		'after_insert' : "gowtham_looms.gowtham_looms.custom.py.item_price.delete_price_list"
	},
	'Driver' :{
		"validate":"gowtham_looms.gowtham_looms.custom.py.driver.validate_phone"
	},
	"Vehicle Log":{
		"on_update_after_submit": "gowtham_looms.gowtham_looms.custom.py.vehicle_log.onsubmit",
		"on_submit": ["gowtham_looms.gowtham_looms.custom.py.vehicle_log.onsubmit",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.onsubmit_hours",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.update_transport_cost",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.vehicle_log_draft",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.vehicle_log_mileage",
		],
		"on_cancel" :["gowtham_looms.gowtham_looms.custom.py.vehicle_log.onsubmit",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.update_transport_cost"
			],
		"validate" :["gowtham_looms.gowtham_looms.custom.py.vehicle_log.validate",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.validate_distance",
						"gowtham_looms.gowtham_looms.custom.py.vehicle_log.total_cost"

		]

	},
    "Sales Order":{
    	"validate" :"gowtham_looms.gowtham_looms.custom.py.sales_order.validate"
	},
	'Item':{"autoname": "gowtham_looms.gowtham_looms.custom.py.item.validate",
			# "after_insert":"gowtham_looms.gowtham_looms.custom.py.item.after_install"	
			}
	
	
}
doctype_js = {
	"Salary Slip" : "/gowtham_looms/custom/js/salary_slip.js",
	"Job Card" : "/gowtham_looms/custom/js/jobcard.js",
	"Item" : "/gowtham_looms/custom/js/item.js",
	"Material Request" : "/gowtham_looms/custom/js/material_request.js",
	"Purchase Order" : "/gowtham_looms/custom/js/purchase_order.js",
	"Item Group" : "/gowtham_looms/custom/js/item_group.js",
	"Stock Entry" : "/gowtham_looms/custom/js/stock_entry.js",
	"Purchase Receipt" : "/gowtham_looms/custom/js/purchase_receipt.js",
	"Purchase Invoice" : "/gowtham_looms/custom/js/purchase_invoice.js",
	"Sales Order" : "/gowtham_looms/custom/js/sales_order.js",
	"Sales Invoice" : "/gowtham_looms/custom/js/sales_invoice.js",
	"Payroll Entry" : "/gowtham_looms/custom/js/payroll_entry.js",
	"Maintenance Visit" : "/gowtham_looms/custom/js/maintenance_visit.js",
	"Vehicle": "/gowtham_looms/custom/js/vehicle.js",
	"Vehicle Log" :["/gowtham_looms/custom/js/vehicle_log.js",
					"/gowtham_looms/custom/js/vehicle_log_service.js",],
    "Stock Reconciliation" :"/gowtham_looms/custom/js/stock_reconciliation_item.js",
    "Quotation":"/gowtham_looms/custom/js/quotation_item.js"
	
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gowtham_looms.tasks.all"
# 	],
# 	"daily": [
# 		"gowtham_looms.tasks.daily"
# 	],
# 	"hourly": [
# 		"gowtham_looms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gowtham_looms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gowtham_looms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gowtham_looms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.manufacturing.doctype.production_plan.production_plan": "gowtham_looms.gowtham_looms.custom.py.workorder.work_order"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gowtham_looms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"gowtham_looms.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
