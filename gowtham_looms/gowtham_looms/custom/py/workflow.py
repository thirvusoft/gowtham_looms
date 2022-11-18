import frappe

def workflow_document_creation():
    create_state()
    create_action()
    create_quotation_flow()

def create_quotation_flow():
    if frappe.db.exists('Workflow', 'Sales Order Flow'):
        frappe.delete_doc('Workflow', 'Sales Order Flow')
    workflow = frappe.new_doc('Workflow')
    workflow.workflow_name = 'Sales Order Flow'
    workflow.document_type = 'Sales Order'
    workflow.workflow_state_field = 'workflow_state'
    workflow.is_active = 1
    workflow.send_email_alert = 1
    workflow.append('states', dict(
        state = 'Draft', allow_edit = 'Administrator',doc_status = 1,
    ))
    workflow.append('states', dict(
        state = 'Draft', allow_edit = 'All',doc_status = 0,
    ))
    workflow.append('states', dict(
        state = 'Approved', allow_edit = 'All',doc_status = 1,
    ))
    workflow.append('states', dict(
        state = 'Waiting for Approval', allow_edit = 'Administrator',doc_status = 1,
    ))
    workflow.append('states', dict(
        state = 'To Deliver and Bill', allow_edit = 'Administrator',doc_status = 1,
    ))
    
    
    workflow.append('transitions', dict(
        state = 'Draft', action='Send to Approval', next_state = 'Waiting for Approval',
        allowed='Administrator', allow_self_approval= 1,condition="doc.gl_item_check == 1",
    ))
    workflow.append('transitions', dict(
        state = 'Waiting for Approval', action='Approve', next_state = 'To Deliver and Bill',
        allowed='Administrator', allow_self_approval= 1,
    ))
    workflow.append('transitions', dict(
        state = 'Draft', action='Approve', next_state = 'To Deliver and Bill',
        allowed='All', allow_self_approval= 1,condition="doc.gl_item_check == 0"
    ))
    workflow.insert(ignore_permissions=True)
    return workflow
def create_state():
    list={"Draft":"Warning", "Waiting for Approval":"Primary", "Approved":"Success", "To Deliver and Bill":"Sucess"}
    for row in list:
        if not frappe.db.exists('Workflow State', row):
            new_doc = frappe.new_doc('Workflow State')
            new_doc.workflow_state_name = row
            new_doc.style=list[row]
            new_doc.save()
    list=['Send to Approval', 'Approve']
    for i in list:
        if not frappe.db.exists('Workflow Action Master', i):
            new_doc = frappe.new_doc('Workflow Action Master')
            new_doc.workflow_action_name = i
            new_doc.save()
def create_action():
    pass