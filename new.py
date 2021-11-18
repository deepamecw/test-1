class nokia:
    company = "nokia"
    website = "www.noia.com"
    def contact_details(self):
        print("cherry road,near salem")

class nokia1100(nokia):
    def __init__(self):
        self.name = "nokia 1100"
        self.year = 1991
    def product_details(self):
        print("company name: ",self.name)
        print("year: ",self.year)
        print("company name: ",self.company )
        print("website: ",self.website )

mobile = nokia1100()
mobile.product_details()
