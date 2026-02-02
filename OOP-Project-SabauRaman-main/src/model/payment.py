from datetime import date, datetime
from .lease_agreement import LeaseAgreement
from .property import Property
class Payment:
     def __init__(self, payment_id: int, lease: LeaseAgreement, amount: float, date_: date, status: str):
         self.payment_id = payment_id
         self.lease = lease
         self.amount = amount
         self.date = date_
         self.status = status  
 
     def is_late(self) -> bool:
         
         return self.date > self.lease.end_date
 
 
class LatePayment(Payment):
     def __init__(self, payment_id: int, lease: LeaseAgreement, amount: float, date_: date, status: str):
         super().__init__(payment_id, lease, amount, date_, status)
         self.penalty_fee = 0.2 * lease.property.price  # 20% of property price
 
     def calculate_penalty(self) -> float:
         return self.amount + self.penalty_fee
     
     
     
     
     
     
     
    