from datetime import date
from .property import Property
from .owner import Owner
class Contract:
     def __init__(self, contract_id: int, owner, property_obj, start_date: date, end_date: date, commission_rate: float):
         self.contract_id = contract_id
         self.owner = owner
         self.property = property_obj
         self.start_date = start_date
         self.end_date = end_date
         self.commission_rate = commission_rate
 
     def is_active(self) -> bool:
         return self.start_date <= date.today() <= self.end_date
 
     def calculate_commission(self) -> float:
         return self.property.price * self.commission_rate