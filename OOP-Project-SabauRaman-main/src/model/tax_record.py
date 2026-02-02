from .property import Property
 
class TaxRecord:
     def __init__(self, tax_id:int, property:Property ,year:int, ammount:int ):
         self.tax_id= tax_id
         self.property= property
         self.year= year
         self.ammount= ammount
 
        
     def calculate_tax(self):
         return self.ammount