
class User:
     def __init__(self, user_id: int, username: str, password_hash: str, role: str):
         self.user_id = user_id
         self.username = username
         self.password_hash = password_hash
         self.role = role
 
     def authenticate(self, password_hash: str) -> bool:
         return self.password_hash == password_hash
 
 
class Admin(User):
     def add_property(self, company, prop):
         company.add_property(prop)
 
     def remove_property(self, company, prop):
         company.remove_property(prop)
 
 
class PropertyManager(User):
     def assign_property_to_resident(self, prop, resident):
         prop.assign_to_resident(resident)
 
 
class Renter(User):
     def get_lease_info(self, lease):
         return str(lease)
