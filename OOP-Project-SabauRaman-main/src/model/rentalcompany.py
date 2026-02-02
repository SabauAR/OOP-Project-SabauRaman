from .property import Property
from datetime import datetime

class RentalCompany:
    company_name = "Sabiko"
    property_list: list = []
    contract: list = []

    
    def add_property(self, property_obj: Property):
        RentalCompany.property_list.append(property_obj)
    
   
    def remove_property(self, property_obj: Property):
        try:
            RentalCompany.property_list.remove(property_obj)
        except ValueError:
            pass  
    
    
    def get_income(self) -> float:
        income = 0
        for prop in RentalCompany.property_list:
            if prop.status == 'occupied':
                income += prop.price
        return income
    
    
    def analyze_occupancy(self) -> float:
        if not RentalCompany.property_list:
            return 0.0
        occupied = sum(1 for p in RentalCompany.property_list if p.status == 'occupied')
        return round((occupied / len(RentalCompany.property_list)) * 100, 2)
