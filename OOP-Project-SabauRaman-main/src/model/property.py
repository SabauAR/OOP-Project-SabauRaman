from datetime import datetime
class Property:
     def __init__(self, address: str, size: float, price: float, facilities: list, status: str):
         self.address = address
         self.size = size
         self.price = price
         self.facilities = facilities
         self.status =   status
         self.history = []  
         
 
     def mark_occupied(self):
         self.status = "occupied"
         self.history.append(("occupied", datetime.now().date()))
 
     def mark_vacant(self):
         self.status = "vacant"
         self.history.append(("vacant", datetime.now().date()))
 
 
class House(Property):
     def __init__(self, address: str, size: float, price: float, facilities: list,
                  num_bedrooms: int, num_bathrooms: int, has_garden: bool,status: str):
         super().__init__(address, size, price, facilities,status)
         self.num_bedrooms = num_bedrooms
         self.num_bathrooms = num_bathrooms
         self.has_garden = has_garden
 
 
class Apartment(Property):
     def __init__(self, address: str, size: float, price: float, facilities: list,
                  floor_number: int, has_elevator: bool, has_balcony: bool,status: str):
         super().__init__(address, size, price, facilities,status)
         self.floor_number = floor_number
         self.has_elevator = has_elevator
         self.has_balcony = has_balcony
 
 
class Shop(Property):
     def __init__(self, address: str, size: float, price: float, facilities: list,
                  business_type: str, parking_available: bool,status: str):
         super().__init__(address, size, price, facilities,status)
         self.business_type = business_type
         self.parking_available = parking_available
 
 
class Land(Property):
     def __init__(self, address: str, size: float, price: float, facilities: list,
                  zoning_type: str, buildable_area: float,status: str):
         super().__init__(address, size, price, facilities,status)
         self.zoning_type = zoning_type
         self.buildable_area = buildable_area
