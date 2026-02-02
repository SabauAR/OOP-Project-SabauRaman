import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.analytics import RentalAnalytics,MonthlyReport
from model.rentalcompany import RentalCompany
from model.contract import Contract
from model.event import EventLog
from model.lease_agreement import LeaseAgreement
from model.maintenance import MaintenanceRequest
from model.notifications import Notification
from model.owner import Owner
from model.payment import Payment
from model.payment import LatePayment
from model.property import Property,House,Apartment,Shop,Land
from model.property_search import PropertySearch
from model.property_search import Navigation
from model.resident import Resident
from model.resident import RentalApplication
from model.tax_record import TaxRecord
from datetime import datetime,date,timedelta
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from model.user import User,Admin,Renter
from model.review import Review,Complaint

company = RentalCompany()

house = House(
    address="1 Ocean Drive",
    size=1800.0,
    price=3000.0,
    facilities=["Pool", "Garage"],
    num_bedrooms=4,
    num_bathrooms=3,
    has_garden=True,
    status="vacant"
)

apartment = Apartment(
    address="22 City Heights",
    size=850.0,
    price=1800.0,
    facilities=["Elevator", "Balcony"],
    floor_number=5,
    has_elevator=True,
    has_balcony=True,
    status="vacant"
)

shop = Shop(
    address="88 Market Street",
    size=1200.0,
    price=2500.0,
    facilities=["Parking", "Loading Dock"],
    business_type="Retail",
    parking_available=True,
    status="vacant"
)

land = Land(
    address="50 Country Road",
    size=5000.0,
    price=1500.0,
    facilities=["Fenced"],
    zoning_type="Residential",
    buildable_area=4000.0,
    status="vacant"
)

####################################################

owner = Owner(
    owner_id=101,
    name="Michael Carter",
    contact_info="michael.carter@realestate.com"
)

# Create an admin
admin = Admin(
    user_id=1,
    username="admin_user",
    password_hash="hashed_pass_123",
    role="admin"
)

# Create a resident
resident = Resident(
    resident_id=201,
    name="Alice Johnson",
    contact_info="alice.johnson@example.com",
    password_hash="renter_secure"
)


####################################################



admin.add_property(company, house)
admin.add_property(company, apartment)
admin.add_property(company, shop)
admin.add_property(company, land)


house.mark_occupied()
apartment.mark_occupied()

print(house.status, house.history)
print(apartment.status, apartment.history)


analytics = RentalAnalytics(company)

print("📊 Rental Analytics Summary")
print(f"Vacancy Rate: {analytics.vacancy_rate()}%")
print(f"Average Rent: ${analytics.average_rent()}")
revenue_data = analytics.revenue_analysis()
print(f"Current Income from Occupied Properties: ${revenue_data['current_income']}")
print(f"Potential Loss from Vacant Properties: ${revenue_data['potential_loss_from_vacancy']}")
print(f"Total Properties Tracked: {revenue_data['total_properties']}")


today = datetime.today()


report = MonthlyReport(
    report_id=1,
    company=company,   
    month=today.month,
    year=today.year
)


report_data = report.generate_report()

print("\n📅 Monthly Report")
for key, value in report_data.items():
    print(f"{key.replace('_', ' ').capitalize()}: {value}")





event_log = EventLog()


request = MaintenanceRequest(
    request_id=1,
    property=house,
    request_date=date.today(),
    description="Leaky kitchen faucet needs repair."
)


request.approve(event_log)



print("\n📘 Event Log:")
for event in event_log.events:
    print(f"- [{event.opened}] {event.text}")

print("\n🏡 Property History:")
for note in house.history:
    print(f"- {note}")
    
    
    
    
    
    
    
resident = Resident(resident_id=1, name="Late Payer", contact_info="late@example.com")


lease = LeaseAgreement(
    lease_id=1,
    property=house,
    resident=resident,
    start_date=date(2025, 1, 1),
    end_date=date(2025, 12, 31),
    rent_amount=1000.0,
    security_deposit=5000.0
)


late_payment = LatePayment(
    payment_id=101,
    lease=lease,
    amount=1000.0,  
    date_=date.today(),
    status="unpaid"
)


total_due = late_payment.calculate_penalty()

print(f"💰 Total amount due (including penalty): ${total_due}")


total_due = late_payment.calculate_penalty()


notification = Notification(
    notification_id=1,
    message=f"You have a late rent payment. Total due (including penalty): ${total_due:.2f}",
    recipient=resident  
)


notification.send()