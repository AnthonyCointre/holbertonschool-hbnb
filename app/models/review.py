#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class Review(BaseModel):

    def __init__(self, place_id, user_id, rating, comment, data_manager):
        super().__init__()
        self._place_id = place_id
        self._user_id = user_id
        self._rating = rating
        self._comment = comment
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        review = Review(
            place_id=data['place_id'],
            user_id=data['user_id'],
            rating=data['rating'],
            comment=data['comment'],
            data_manager=data_manager
        )
        review.id = data['review_id']
        review.created_at = datetime.fromisoformat(data['created_at'])
        review.updated_at = datetime.fromisoformat(data['updated_at'])
        return review

    @property
    def place_id(self):
        return self._place_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
        self.updated_at = datetime.now()
        self.save()

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
        self.updated_at = datetime.now()
        self.save()

    def to_dict(self):
        return {
            "review_id": self.id,
            "place_id": self._place_id,
            "user_id": self._user_id,
            "rating": self._rating,
            "comment": self._comment,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
