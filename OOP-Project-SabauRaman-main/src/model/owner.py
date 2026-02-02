class Owner:
     def __init__(self, owner_id: int, name: str, contact_info: str):
         self.owner_id = owner_id
         self.name = name
         self.contact_info = contact_info
         self.properties_owned = list()
 
     def get_properties(self) -> list:
         return self.properties_owned.copy()