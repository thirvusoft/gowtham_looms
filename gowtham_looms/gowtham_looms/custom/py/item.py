from frappe.model.naming import make_autoname
def validate(self,action):
    self.name = make_autoname('GL -'+self.abbrevation + ".####", "", self)
    self.item_code = make_autoname('GL -'+self.abbrevation + ".####", "", self)