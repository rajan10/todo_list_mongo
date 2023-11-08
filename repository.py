from mongoengine import connect, Document, StringField, FloatField, DictField, ListField

connect("todo_mongo")


class User(Document):
    name = DictField()
    address = ListField(StringField(max_length=200))
    height = FloatField()


john = User(
    name={"title": "Mr.", "first_name": "John", "last_name": "Smith"},
    address=["Kathmandu", "Bhaktapur"],
    height=5.7,
)
john.save()
