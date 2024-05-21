import frappe
from frappe.model.document import Document

class Candidate(Document):
	pass



def before_insert(doc, method):
    # Fetch the current counter value
    counter = frappe.db.get_single_value('Auto Increment Counter', 'candidate_counter')
    if not counter:
        counter = 1
    else:
        counter += 1

    # Save the new counter value back to the database
    frappe.db.set_value('Auto Increment Counter', None, 'candidate_counter', counter)

    # Set the candidate_id field with the new counter value
    doc.candidateid = f"CAND-{str(counter).zfill(3)}"