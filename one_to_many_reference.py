"""One to Many
1. City  and Citizens = references"""

from utils import get_current_date
from mongoengine import (
    connect,
    StringField,
    IntField,
    EmailField,
    ListField,
    Document,
    DateTimeField,
    ReferenceField,
    CASCADE,
)

connect("relation_db")


class City(Document):
    name = StringField(max_length=100)
    country = StringField()
    created_at = DateTimeField(default=get_current_date)

    def __str__(self):
        return f"<City: {self.name}>"


class Citizen(Document):
    name = StringField(max_length=100)
    age = IntField()
    email = EmailField()
    phone = StringField(max_length=20)
    city = ReferenceField(City, reverse_delete_rule=CASCADE)  # object

    def __str__(self):
        return f"<Citizen: {self.name}>"


class CityRepo:
    def create(self, name: str, country: str) -> City:
        city = City(name=name, country=country)
        city.save()
        return city

    def read_by_name(self, name: str) -> City:
        city_read = City.objects.get(name=name)
        return city_read

    def update_by_name(self, name: str, country: str) -> City:
        city_update = self.read_by_name(name)
        if city_update:
            city_update.country = country
            city_update.save()
            return city_update

    def delete_by_name(self, name: str) -> None:
        city_delete = self.read_by_name(name)
        if city_delete:
            city_delete.delete()


# create
city_repo = CityRepo()
# city = city_repo.create(name="Lalitpur", country="Nepal")
# print(city)

# read
# city_read = city_repo.read_by_name(name="Kathmandu")
# print(city_read)

# udpate
# city_update = city_repo.update_by_name(name="Kathmandu", country="Canada")
# print(city_update)


# delete
city_repo.delete_by_name("Lalitpur")


class CitizenRepo:
    def __init__(self):
        self.city_repo = CityRepo()

    def create(
        self, name: str, age: int, email: str, phone: str, city_name: str
    ) -> Citizen:
        city_object = self.city_repo.read_by_name(city_name)
        citizen = Citizen(
            name=name, age=age, email=email, phone=phone, city=city_object
        )
        citizen.save()
        return citizen

    def read_by_name(self, name) -> Citizen:
        citizen = Citizen.objects.get(name=name)
        return citizen

    def update_by_name(
        self, name: str, age: int, email: str, phone: str, city_name: str, country: str
    ) -> Citizen:
        citizen = Citizen.objects.get(name=name)
        city_object = self.city_repo.read_by_name(city_name)
        if city_object:
            city_object.country = country
            city_object.save()
        if citizen:
            citizen.age = age
            citizen.email = email
            citizen.phone = phone
            citizen.city = city_object
            citizen.save()
        return citizen

    def delete_by_name(self, name: str) -> None:
        citizen_object = self.read_by_name(name)
        citizen_object.delete()


citizen_repo = CitizenRepo()

# create
# citizen_create = citizen_repo.create(
#     name="John",
#     age=31,
#     email="john@gmail.com",
#     phone="87654321",
#     city_name="Lalitpur",
# )

# print(citizen_create)

# read
# citizen = citizen_repo.read_by_name("Rajan")
# print(citizen)

# update
# citizen_to_update = citizen_repo.update_by_name(
#     name="Rajan",
#     age=35,
#     email="rajan10@gmail.com",
#     phone="1234",
#     city_name="Lalitpur",
#     country="Canada",
# )
# print(citizen_to_update)


# delete
# citizen_repo.delete("Rajan")
