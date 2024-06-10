#!/usr/bin/python3

class Review:
    def __init__(self, review_id, user, place):
        self.review_id = review_id
        self.user = user
        self.place = place

    def __repr__(self):
        return  f"Review({self.review_id}, {self.user}, {self.place})"
