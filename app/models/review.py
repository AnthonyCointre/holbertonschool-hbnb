#!/usr/bin/python3

from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, rating, comment, user, place):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.user = user
        self.place = place

    def to_dict(self):
        review_dict = super().to_dict()
        review_dict.update({
            "rating": self.rating,
            "comment": self.comment,
            "user": self.user.id,
            "place": self.place.id
        })
        return review_dict

    def __repr__(self):
        return f"<Review {self.rating} - {self.place.name}>"
