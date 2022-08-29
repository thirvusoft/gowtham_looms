from frappe.model.naming import make_autoname
def validate(self,action):
    if self.item_code == "":    
        self.name = make_autoname('GL-'+self.abbrevation + ".#", "", self)
        self.item_code = self.name
        