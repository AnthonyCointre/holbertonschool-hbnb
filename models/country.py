<<<<<<< HEAD
#!/usr/bin/env python3

class country(base_model):
    """class that inherits from BaseModel"""
    def __init__(self, country_id="", country_name=""):
        self.id = country_id
        self.name = country_name
        
    def add(self):
        """Add a country"""
        self.country.append(country)
=======
#!/usr/bin/python3

class City:
    def __init__(self, city_id, name, country):
        self.city_id = city_id
        self.name = name
        self.country = country

    def __repr__(self):
        return f"City({self.city_id}, {self.name}, {self.country})"
>>>>>>> 19032e6d8d29dce5e6b8e6f732b82a0e810a730a
