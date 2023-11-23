"""
One to One
1. Patient and Disease = Embedded
2. Person and Car = Reference

One to Many
1. Question and Answers = Embedded
2. City and Citizens = Reference

Many to Many
1. Customers and Products
2. Books and Authors
"""
from enum import Enum
from mongoengine import (
    connect,
    StringField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    DateTimeField,
    FloatField,
    EmailField,
    DictField,
    EnumField,
    IntField,
    ReferenceField,
)

connect("relation-db")


class DiseaseType(Enum):
    COMMUNICABLE = "Communicable"
    NONCOMMUNICABLE = "Non-communicable"


class Disease(EmbeddedDocument):
    name = StringField(max_length=100)
    type = EnumField(DiseaseType)

    def __str__(self):
        return f"<Disease: {self.name}>"


class Patient(Document):
    name = StringField(max_length=100)
    disease = EmbeddedDocumentField(Disease)

    def __str__(self):
        return f"<Patient: {self.name}>"


# inside person has a car relation  1 to 1
class CarColor(Enum):
    RED = "R"
    BLACK = "B"
    GREEN = "G"
    YELLOW = "Y"


class Car(Document):
    name = StringField(max_length=50)
    model = DateTimeField()
    color = EnumField(CarColor)
    price = FloatField()

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


"""
One to Many
1. Question and Answers = Embedded
2. City and Citizens = Reference  """


# embeded ; in question there is answer document relation
class Answer(EmbeddedDocument):
    answer = StringField(max_length=100)
    created_at = DateTimeField()

    def __str__(self):
        return f"<Answer: {self.answer}>"


class Question(Document):
    question = StringField(max_length=100)
    created_at = DateTimeField()
    answers = ListField(EmbeddedDocumentField(Answer))

    def __str__(self):
        return f"<Question: {self.question}>"


class City(Document):
    name = StringField(max_length=100)
    country = StringField()
    created_at = DateTimeField()

    def __str__(self):
        return f"<City: {self.name}>"


class Citizen(Document):
    name = StringField(max_length=100)
    age = IntField()
    email = EmailField()
    phone = StringField(max_length=20)
    city = ReferenceField(City)

    def __str__(self):
        return "<Citizen: {self.name}>"


"""Many to Many
1. Books and Authors
2. Customers and Products"""


# reference relation
# many to many


class Book(Document):
    title = StringField(max_length=50)
    price = FloatField()
    published_date = DateTimeField()

    def __str__(self):
        return "<Book: {self.title}>"


class MaritalStatus(Enum):
    MARRIED = "Married"
    UNMARRIED = "Unmarried"


class Author(Document):
    name = StringField(max_length=100)
    email = EmailField()
    marital_staus = EnumField(MaritalStatus)

    def __str__(self):
        return "<Author: {self.name}>"


class BookAuthor(Document):
    book = ReferenceField(Book)
    author = ReferenceField(Author)

    def __str__(self):
        return "<BookAuthor: {self.book}>, <{self.author}>"
