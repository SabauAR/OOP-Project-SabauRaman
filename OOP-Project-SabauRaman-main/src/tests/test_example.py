import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.analytics import RentalAnalytics
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
import pytest 


    
    



company = RentalCompany()







def test_property_initialization():
    property1 = Property("123 Beach Ave", 2000.0, 500000.0, ["pool", "gym"], "vacant")
    assert property1.address == "123 Beach Ave"
    assert property1.size == 2000.0
    assert property1.price == 500000.0
    assert property1.facilities == ["pool", "gym"]
    assert property1.status == "vacant"
    assert property1.history == []

# Test initialization of specific property types (House, Apartment, Shop, Land)
def test_house_initialization():
    house = House("456 Garden Rd", 3000.0, 750000.0, ["garage", "garden"], 4, 3, True,"occupied")
    assert house.address == "456 Garden Rd"
    assert house.num_bedrooms == 4
    assert house.num_bathrooms == 3
    assert house.has_garden is True
    assert house.status == "occupied"

def test_apartment_initialization():
    apartment = Apartment("789 City Blvd", 1200.0, 350000.0, ["elevator", "balcony"], 5, True, True,"occupied")
    assert apartment.address == "789 City Blvd"
    assert apartment.floor_number == 5
    assert apartment.has_elevator is True
    assert apartment.has_balcony is True
    assert apartment.status == "occupied"

def test_shop_initialization():
    shop = Shop("123 Market St", 1500.0, 200000.0, ["wifi", "air conditioning"], "grocery", True,"occupied")
    assert shop.address == "123 Market St"
    assert shop.business_type == "grocery"
    assert shop.parking_available is True
    assert shop.status == "occupied"

def test_land_initialization():
    land = Land("456 Rural Ln", 5000.0, 1000000.0, [], "commercial", 3500.0,"occupied")
    assert land.address == "456 Rural Ln"
    assert land.zoning_type == "commercial"
    assert land.buildable_area == 3500.0
    assert land.status == "occupied"


def test_mark_occupied_and_vacant():
    property1 = Property("123 Beach Ave", 2000.0, 500000.0, ["pool", "gym"], "occupied")
    property1.mark_occupied()  
    assert property1.status == "occupied"
    assert len(property1.history) == 1
    assert property1.history[0] == ("occupied", datetime.now().date())  
    
    property1.mark_vacant()  
    assert property1.status == "vacant"
    assert len(property1.history) == 2
    assert property1.history[1] == ("vacant", datetime.now().date())


def test_rental_company_income():
    
    company = RentalCompany()

    
    property1 = House("123 Beach Ave", 2000.0, 500000.0, ["pool", "gym"], 4, 3, True,"vacant")
    property2 = Apartment("789 City Blvd", 1200.0, 350000.0, ["elevator", "balcony"], 5, True, True, "occupied")
    property3 = Shop("456 Market St", 1500.0, 200000.0, ["wifi", "air conditioning"], "grocery", True, "occupied")
    
    
    company.add_property(property1)
    company.add_property(property2)
    company.add_property(property3)
    
    
    property1.mark_occupied()
    
    
    assert company.get_income() == 1050000.0  
    
    property3.mark_vacant()

   
    assert company.get_income() == 850000.0  

# Test occupancy rate in RentalCompany
def test_analyze_occupancy():
    company = RentalCompany()

    property4 = House("123 Beach Ave", 2000.0, 500000.0, ["pool", "gym"], 4, 3, True,"vacant")
    property5 = Apartment("789 City Blvd", 1200.0, 350000.0, ["elevator", "balcony"], 5, True, True, "vacant")
    
    company.add_property(property4)
    company.add_property(property5)

    
    property4.mark_occupied()
    
    

    # Analyze occupancy rate
    assert company.analyze_occupancy() == 60.0  
    assert company.get_income() == 1350000.0
    
    
    
    
    
    
def test_late_payment_calculation():
    
    test_property = House(
        address="101 Mockingbird Lane",
        size=1000.0,
        price=2000.0,  
        facilities=["garden"],
        num_bedrooms=2,
        num_bathrooms=1,
        has_garden=True,
        status="occupied"
    )

    
    test_resident = Resident(resident_id=50409,name="John Doe", contact_info="john@example.com")

    
    lease = LeaseAgreement(
        lease_id=1,
        property=test_property,
        resident=test_resident,
        start_date=date(2025, 1, 1),
        end_date=date(2025, 12, 31),
        rent_amount=1000.0,
        security_deposit= 4000
    )

    # Create a late payment
    late_payment = LatePayment(
        payment_id=101,
        lease=lease,
        amount=1000.0,
        date_=date(2025, 4, 1),
        status="unpaid"
    )

    # Check penalty fee and total due
    assert late_payment.penalty_fee == 0.2 * 2000.0  # 400.0
    assert late_payment.calculate_penalty() == 1400.0
    
    
    
    
    def test_maintenance_request_approval_and_rejection():
    
     property_test = House(
        address="42 Galaxy Road",
        size=1500.0,
        price=1800.0,
        facilities=["AC", "WiFi"],
        bedrooms=3,
        bathrooms=2,
        has_garage=True,
        status="occupied"
    )
     property_test.history = []  

     event_log = EventLog()
    request = MaintenanceRequest(
        request_id=1,
        property=property,
        request_date=date(2025, 4, 15),
        description="Fix broken heater"
    )
     

    
    
    
    
    
    
    
    
    def test_user_authentication():
     user = User(user_id=1, username="testuser", password_hash="abc123", role="admin")
     assert user.authenticate("abc123") is True
     assert user.authenticate("wrongpass") is False

def test_admin_add_and_remove_property():
    admin = Admin(user_id=2, username="admin1", password_hash="pass", role="admin")
    company = RentalCompany()
    prop = House("12 Elm St", 1200.0, 300000.0, [], 3, 2, True, "vacant")

    admin.add_property(company, prop)
    assert prop in company.property_list

    admin.remove_property(company, prop)
    assert prop not in company.property_list

def test_admin_add_and_remove_property():
    admin = Admin(user_id=2, username="admin1", password_hash="pass", role="admin")
    company = RentalCompany()
    prop = House("12 Elm St", 1200.0, 300000.0, [], 3, 2, True, "vacant")

    admin.add_property(company, prop)
    assert prop in company.property_list

    admin.remove_property(company, prop)
    assert prop not in company.property_list

def test_renter_get_lease_info():
    renter = Renter(user_id=3, username="renter", password_hash="rentpass", role="renter")
    mock_property = House("99 Maple Dr", 1300.0, 400000.0, [], 2, 1, True, "occupied")
    resident = Resident(2324, "Bob", "bob@example.com", password_hash="test121" )

    lease = LeaseAgreement(lease_id=10, property=mock_property, resident=resident,
                           start_date=date(2025, 1, 1), end_date=date(2025, 12, 31), rent_amount=1300.0, security_deposit=6900)
    assert renter.get_lease_info(lease) == str(lease)




def test_notification_send(capsys):
    recipient = User(user_id=1, username="testuser", password_hash="hash123", role="renter")
    message = "Your rent is overdue."
    notification = Notification(notification_id=101, message=message, recipient=recipient)

   
    notification.send()
    captured = capsys.readouterr()
    expected_output = f"Message for testuser: {message}\n"

    assert captured.out == expected_output
    

def test_search_by_location():
    properties = [
        House("123 Ocean View", 1000.0, 1500.0, [], 2, 1, True, "vacant"),
        Apartment("456 Mountain Rd", 800.0, 1200.0, [], 3, True, True, "occupied"),
        House("789 Ocean Blvd", 1100.0, 1600.0, [], 3, 2, False, "vacant")
    ]

    result = PropertySearch.search_by_location(properties, "ocean")
    addresses = [p.address for p in result]

    assert len(result) == 2
    assert "123 Ocean View" in addresses
    assert "789 Ocean Blvd" in addresses

def test_search_by_price():
    properties = [
        House("123 Oak St", 1000.0, 1500.0, [], 2, 1, True, "vacant"),
        House("456 Pine St", 1200.0, 2000.0, [], 3, 2, False, "vacant"),
        House("789 Birch St", 1100.0, 1000.0, [], 2, 2, True, "vacant")
    ]

    result = PropertySearch.search_by_price(properties, 1500.0)
    prices = [p.price for p in result]

    assert len(result) == 2
    assert all(p.price <= 1500.0 for p in result)

def test_search_by_availability():
    properties = [
        House("101 Elm St", 900.0, 1300.0, [], 2, 1, True, "vacant"),
        Apartment("202 Maple Ave", 700.0, 1100.0, [], 1, True, False, "occupied"),
        Apartment("303 Cedar Blvd", 800.0, 1000.0, [], 2, False, True, "vacant")
    ]

    result = PropertySearch.search_by_availability(properties)
    assert len(result) == 2
    assert all(p.status == "vacant" for p in result)





def test_review_average_rating():
    
    prop = House("321 Forest Rd", 900.0, 1400.0, [], 2, 1, False, "vacant")

    
    

    
    Review(1, prop, 4.0, "Nice place")
    Review(2, prop, 5.0, "Excellent location")
    Review(3, prop, 3.0, "Could use some repairs")

   
    average = Review.get_average_rating(prop)
    assert average == pytest.approx(4.0)

def test_complaint_resolution():
    prop = House("654 Riverbank Dr", 1000.0, 1500.0, [], 3, 2, True, "occupied")

    complaint = Complaint(complaint_id=1, property=prop, description="Water leakage in the kitchen")
    
    assert complaint.status == "open"
    
    complaint.resolve()
    assert complaint.status == "resolved"