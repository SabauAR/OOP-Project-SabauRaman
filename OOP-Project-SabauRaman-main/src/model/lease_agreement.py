from datetime import date, timedelta
from .property import Property
class LeaseAgreement:
    def __init__(self, lease_id: int, property, resident,
                 start_date: date, end_date: date,
                 rent_amount: float, security_deposit: float):
        self.lease_id = lease_id
        self.property = property
        self.resident = resident
        self.start_date = start_date
        self.end_date = end_date
        self.rent_amount = rent_amount
        self.security_deposit = security_deposit

    def is_active(self) -> bool:
        today = date.today()
        return self.start_date <= today <= self.end_date

    def renew_lease(self) -> bool:
        if self.is_active():
            one_year = timedelta(days=365)
            self.end_date += one_year
            return True
        return False