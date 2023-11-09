"""One to One
1. Patient and Disease = Embedded
2. Person and Car = Reference"""


from enum import Enum

from mongoengine import (
    connect,
    EmbeddedDocument,
    EnumField,
    StringField,
    Document,
    DictField,
    IntField,
    EmbeddedDocumentField,
)


connect("relation_db")


class Type(Enum):
    COMMUNICABLE = "communicable"
    NONCOMMUNICABLE = "noncommunicable"


class Disease(EmbeddedDocument):
    name = StringField(max_length=50)
    type = EnumField(Type)

    def __str__(self):
        return f"<Disease: {self.name}>"


class Patient(Document):
    name = StringField(max_length=100)
    address = DictField()
    phone = StringField()
    age = IntField()
    disease = EmbeddedDocumentField(Disease)

    def __str__(self):
        return f"<Patient: {self.name}>"


class PatientRepo:
    def create(
        self,
        name: str,
        address: dict,
        phone: str,
        age: int,
        disease_name: str,
        type: str,
    ):
        disease = Disease(name=disease_name, type=type)
        patient = Patient(
            name=name, address=address, phone=phone, age=age, disease=disease
        )
        patient.save()
        return patient

    def read(self, id):
        patient = Patient.objects.get(id=id)
        return patient

    def update_age(self, id, age):
        patient = self.read(id=id)
        patient.age = age
        patient.save()
        return patient

    def delete(self, id):
        patient = self.read(id=id)
        patient.delete()


patient_repo = PatientRepo()
# patient = patient_repo.create(
#     name="John",
#     address={"city": "Kathmandu", "zipcode": 12345},
#     phone="9841507682",
#     age=30,
#     disease_name="common_cold",
#     type=Type.COMMUNICABLE,
# )
# print(patient)
# patient = patient_repo.read(id="654c2eb8796efb77ef04e522")
# print(patient)

# patient_repo.delete(id="654c2eb8796efb77ef04e522")

patient = patient_repo.update_age(id="654c2ec0585832a5c558c479", age=31)
print(patient.age)
