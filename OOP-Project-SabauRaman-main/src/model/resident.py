from datetime import date
from .lease_agreement import LeaseAgreement
from .payment import Payment
from .event import Event, EventLog
from .property import Property
from .user import User

class Resident(User):
    def __init__(self, resident_id: int, name: str, contact_info: str, password_hash: str = ""):
        uname = name.replace(" ", "_")
        super().__init__(resident_id, uname, password_hash, "renter")
        self.resident_id = resident_id
        self.name = name
        self.contact_info = contact_info
        self.lease_agreements = []

    def get_active_lease(self) -> LeaseAgreement:
        return next((lease for lease in self.lease_agreements if lease.is_active()), None)

    def pay_rent(self, amount: float, event_log: EventLog) -> Payment | None:
        lease = self.get_active_lease()
        if lease and amount >= lease.rent_amount:
            payment = Payment(
                payment_id=1,
                lease=lease,
                amount=amount,
                date=date.today(),
                status="paid"
            )
            print(f'{self.name} paid rent:{payment.amount}')
            
            event = Event(
                opened=False,
                type="RentPaid",
                data=f"{self.name} paid {payment.amount} on {payment.date}"
            )
            event_log.record_event(event)

            lease.property.history.append(f"Rent paid:{payment.amount} on {payment.date}")
            return payment

        print(f"{self.name} has no active lease or insufficient payment.")
        return None


class RentalApplication:
    def __init__(self, application_id: int, applicant: Resident, property: Property):
        self.application_id = application_id
        self.applicant = applicant
        self.property = property
        self.status = "pending"

    def approve(self):
        self.status = "approved"
        print(f"Application {self.application_id} has been approved for {self.applicant.name}.")

    def reject(self):
        self.status = "rejected"
        print(f"Application {self.application_id} has been rejected for {self.applicant.name}.")
