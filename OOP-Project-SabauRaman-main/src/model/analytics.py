from .property import Property
from .rentalcompany import RentalCompany
from .contract import Contract
 
class RentalAnalytics:
     def __init__(self, company: RentalCompany):
         self.company = company
 
     def vacancy_rate(self) -> float:
         properties = self.company.property_list
         if not properties:
             return 0.0
         vacant_count = sum(1 for p in properties if p.status == "vacant")
         return round((vacant_count / len(properties)) * 100, 2)
 
     def average_rent(self) -> float:
         properties = self.company.property_list
         if not properties:
             return 0.0
         total = sum(p.price for p in properties)
         return round(total / len(properties), 2)
 
     def revenue_analysis(self) -> dict:
         properties = self.company.property_list
         income = sum(p.price for p in properties if p.status == "occupied")
         loss = sum(p.price for p in properties if p.status == "vacant")
         return {
             "total_properties": len(properties),
             "current_income": income,
             "potential_loss_from_vacancy": loss
         }
 
class MonthlyReport:
     def __init__(self, report_id: int, company: RentalCompany, month: int, year: int):
         self.report_id = report_id
         self.month = month
         self.year = year
         self.company = company
 
         # Use analytics to generate values
         analytics = RentalAnalytics(company)
         self.vacancy_percentage = analytics.vacancy_rate()
         self.income = analytics.revenue_analysis()["current_income"]
         self.loss_due_to_vacancy = analytics.revenue_analysis()["potential_loss_from_vacancy"]
 
     def generate_report(self) -> dict:
         return {
             "report_id": self.report_id,
             "month": self.month,
             "year": self.year,
             "vacancy_percentage": self.vacancy_percentage,
             "income": self.income,
             "loss_due_to_vacancy": self.loss_due_to_vacancy
         }