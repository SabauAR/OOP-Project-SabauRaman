from .property import Property
class utility_provider:
     def __init__(self, provider_id, name, service_type, monthly_cost):
         self.provider_id= provider_id
         self.name= name
         self.service_type= service_type
         self.monthly_cost= monthly_cost
     def calculate_utility_cost(self, property:Property):
         rate_per_squaremetre= 0.75
         return property.size * rate_per_squaremetre