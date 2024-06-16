# HBnB Evolution: Part 1 (Model + API)

## Description of the project
Creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask.

## Evironment
- Operating system : Ubuntu 20.04 LTS
- Virtual Environment : hbtn
- Flask : Flask-RESTful, flask-restx, flask-swagger-ui

## Project specifitacation
### The Three Layers of Our API Cake:
- Services Layer: This is where our API greets the world. It handles all the requests and responses.
- Business Logic Layer: The brain of the operation. This is where all the processing and decision-making happens.
- Persistence Layer: For now, it’s our humble file system, but we’ll graduate to a database in the future.

### The Data Model: Key Entities
- Places: These are the heart of our app. Each place (like a house, apartment, or room) has characteristics like name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, amenities, and reviews.
- Users: Users are either owners (hosts) or reviewers (commenters) of places. They have attributes like email, password, first name, and last name. A user can be a host for multiple places and can also write reviews for places they don’t own.
- Reviews: Represent user feedback and ratings for a place. This is where users share their experiences.
- Amenities: These are features of places, like Wi-Fi, pools, etc. Users can pick from a catalog or add new ones.
- Country and City: Every place is tied to a city, and each city belongs to a country. This is important for categorizing and searching places.

### Business Logic: Rules to Live By
- Unique Users: Each user is unique and identified by their email.
- One Host per Place: Every place must have exactly one host.
- Flexible Hosting: A user can host multiple places or none at all.
- Open Reviewing: Users can write reviews for places they don’t own.
- Amenity Options: Places can have multiple amenities from a catalog, and users can add new ones.
- City-Country Structure: A place belongs to a city, cities belong to countries, and a country can have multiple cities.

## Examples
Tests example :
```
~/holbertonschool-hbnb$ python3 -m unittest discover -s app/tests/
....................
----------------------------------------------------------------------
Ran 20 tests in 0.016s

OK
~/holbertonschool-hbnb$
```

## UML Diagram 
![UML](https://github.com/AnthonyCointre/holbertonschool-hbnb/blob/main/hbnb_diagram.png)

Created by : 
- [Anthony Cointre](https://github.com/AnthonyCointre/)
- [Nadège Luthier](https://github.com/NadegeL/)