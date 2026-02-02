from .property import Property

class Review:
    all_reviews = []

    def __init__(self, review_id: int, property: Property, rating: float, comment: str):
        self.review_id = review_id
        self.property = property
        self.rating = rating
        self.comment = comment
        Review.all_reviews.append(self)

    @staticmethod
    def get_average_rating(property: Property) -> float:
        relevant_reviews = [r.rating for r in Review.all_reviews if r.property == property]
        if not relevant_reviews:
            return 0.0
        return sum(relevant_reviews) / len(relevant_reviews)


class Complaint:
    def __init__(self, complaint_id: int, property: Property, description: str):
        self.complaint_id = complaint_id
        self.property = property
        self.description = description
        self.status = "open"

    def resolve(self):
        self.status = "resolved"
        
        
