from .property import Property
from .contract import Contract
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
 
 
class PropertySearch:
     @staticmethod
     def search_by_location(properties: list, location: str) -> list:
         location = location.lower()
         matching_properties = []
         for prop in properties:
             if location in prop.address.lower():
                 matching_properties.append(prop)
         return matching_properties
 
     @staticmethod
     def search_by_price(properties: list, max_price: float) -> list:
         return list(filter(lambda prop: prop.price <= max_price, properties))
 
     @staticmethod
     def search_by_availability(properties: list) -> list:
         return [prop for prop in properties if prop.status == "vacant"]
 
 
class Navigation:
     def __init__(self, company, current_location: str):
         self.company = company
         self.current_location = current_location
 
     def get_nearest_available_property(self) -> Property | None:
         available_properties = [
             prop for prop in self.company.properties_list if prop.status == "vacant"
         ]
 
         if not available_properties:
             return None
 
         geolocator = Nominatim(user_agent="rental_system_locator")
         origin = geolocator.geocode(self.current_location)
 
         if not origin:
             return None
 
         origin_coords = (origin.latitude, origin.longitude)
 
         def calculate_distance(prop):
             destination = geolocator.geocode(prop.address)
             if destination:
                 return geodesic(origin_coords, (destination.latitude, destination.longitude)).km
             return float("inf")
 
         return min(available_properties, key=calculate_distance)
