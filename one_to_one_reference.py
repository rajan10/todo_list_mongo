"""
One to One relation
2. Person and Car = Reference"""
from enum import Enum
from mongoengine import (
    connect,
    Document,
    StringField,
    DateTimeField,
    EnumField,
    EmailField,
    IntField,
    ReferenceField,
    DictField,
)


connect("relation_db")


class CarColor(Enum):
    RED = "R"
    GREEN = "G"
    BLACK = "B"
    YELLOW = "Y"


class Car(Document):
    name = StringField(max_length=100)
    model = DateTimeField()
    color = EnumField(CarColor)

    def __str__(self):
        return f"<Car: {self.name}>"


class Person(Document):
    name = StringField(max_length=200)
    email = EmailField()
    address = DictField()
    age = IntField()
    car = ReferenceField(Car)

    def __str__(self):
        return f"<Person: {self.name}>"


class CarRepo:
    def create(self, name: str, model: DateTimeField, color: str):
        car = Car(name=name, model=model, color=color)
        car.save()
        return car

    def read_by_name(self, name: str):
        car_read = Car.objects(name=name).first()
        return car_read

    def update_by_name(self, name: str, model: DateTimeField, color: str):
        car_update = Car.objects(name=name).first()
        car_update.model = model
        car_update.color = color
        car_update.save()
        return car_update

    def delete_by_name(self, name: str):
        car_delete = car_repo.read_by_name(name=name)
        car_delete.delete()


car_repo = CarRepo()
# toyota = car_repo.create(name="Toyota", model="2022-01-01", color=CarColor.RED)
# print(toyota)
# car_read = car_repo.read_by_name(name="Toyota")
# print(car_read)

# car_update_by_name = car_repo.update_by_name(
#     name="Toyota", model="2023-01-01", color=CarColor.GREEN
# )
# print(car_update_by_name)
# print(f"{car_update_by_name.color} , {car_update_by_name.model}")

# car_repo.delete_by_name(name="Toyota")


class PersonRepo:
    # CRUD operations
    def create(self, name: str, email: str, address: dict, age: int, car: Car):
        person = Person(name=name, email=email, address=address, car=car)
        person.save()
        return person

    def read_by_name(self, name: str):
        person_read = Person.objects(name=name).first()
        return person_read


person_repo = PersonRepo()
# toyota = car_repo.read_by_name(name="Toyota")
# john = person_repo.create(
#     name="John",
#     email="john@gmail.com",
#     address={"street": "Sproat Ave", "city": "Toronto"},
#     age=34,
#     car=toyota,
# )
# josh = person_repo.create(
#     name="Josh",
#     email="Josh@gmail.com",
#     address={"street": "Sproat Ave", "city": "Toronto"},
#     age=34,
#     car=toyota,
# )
# print(john)
# print(josh)

# john = person_repo.read_by_name(name="John")
# print(john.car.color)
# print(john.car.model)
