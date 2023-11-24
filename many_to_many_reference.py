"""Many books can be written by  many authors
        1 book can be written by many authors
        1 author can write many  books"""


from enum import Enum

from mongoengine import (
    connect,
    StringField,
    Document,
    DateTimeField,
    FloatField,
    EmailField,
    EnumField,
    ReferenceField,
)

connect("relation_db")


class Book(Document):
    title = StringField(max_length=50)
    price = FloatField()
    published_date = DateTimeField()

    def __str__(self):
        return f"<Book: {self.title}>"


class MaritalStatus(Enum):
    MARRIED = "Married"
    UNMARRIED = "Unmarried"


class Author(Document):
    name = StringField(max_length=100)
    email = EmailField()
    marital_staus = EnumField(MaritalStatus)

    def __str__(self):
        return f"<Author: {self.name}>"


class BookAuthor(Document):
    book = ReferenceField(Book)
    author = ReferenceField(Author)

    def __str__(self):
        return f"<BookAuthor: {self.book}>, <{self.author}>"


class BookRepo:
    def create(self, title: str, price: float, published_date: str) -> Book:
        book = Book(title=title, price=price, published_date=published_date)
        book.save()
        return book

    def read_by_title(self, title: str) -> Book:
        book = Book.objects.get(title=title)
        return book

    def update_by_title(self, title: str, price: float) -> Book:
        book = self.read_by_title(title=title)
        if book:
            book.price = price
            book.save()
        return book

    def delete_by_title(self, title: str) -> None:
        book = self.read_by_title(title=title)
        if book:
            book.delete()


book_repo = BookRepo()
# book = book_repo.create(title="Mahabharat", price=222.25, published_date="2023-11-02")
# print(book)


class AuthorRepo:
    def create(self, name: str, email: str, marital_staus: MaritalStatus) -> Author:
        author = Author(name=name, email=email, marital_staus=marital_staus)
        author.save()
        return author

    def read_by_name(self, name: str) -> Author:
        author = Author.objects.get(name=name)
        return author

    def update_by_name(
        self, name: str, email: str, marital_status: MaritalStatus
    ) -> Author:
        author = self.read_by_name(name=name)
        if author:
            author.email = email
            author.marital_staus = marital_status
            author.save()
        return author

    def delete_by_name(self, name: str) -> None:
        author = self.read_by_name(name=name)
        if author:
            author.delete()


author_repo = AuthorRepo()
# author_repo.create(
#     name="Ved Vyas",
#     email="ved@gmail.com",
#     marital_staus=MaritalStatus.UNMARRIED,
# )


class BookAuthorRepo:
    def create(self, book: Book, author: Author) -> BookAuthor:
        book_author = BookAuthor(book=book, author=author)
        book_author.save()
        return book_author

    def read_by_book(self, book: Book) -> BookAuthor:
        read_book = BookAuthor.objects.get(book=book)
        return read_book

    def read_by_author(self, author: Author) -> BookAuthor:
        read_author = BookAuthor.objects.get(author=author)
        return read_author

    def update_by_book(self, book: Book, author: Author) -> BookAuthor:
        book = self.read_by_book(book=book)
        if book:
            book.author = author
            book.save
        return book

    def update_by_author(self, book: Book, author: Author) -> BookAuthor:
        author = self.read_by_author(author=author)
        if author:
            author.book = book
            author.save
        return book

    def delete_by_id(self, id: str) -> None:
        book_author = BookAuthor.objects.get(_id=id)
        if book_author:
            book_author.delete()


mahabharat = book_repo.read_by_title(title="Mahabharat")
bhanukhakta = author_repo.read_by_name(name="Bhanubhakta")

# vedvyas = author_repo.read_by_name(name="Ved Vyas")
# book_author_repo = BookAuthorRepo()
# book_author = book_author_repo.create(book=mahabharat, author=vedvyas)
# print(book_author)


# query how many books written by Bhanubhakta?
# relations = BookAuthor.objects(author=bhanukhakta)
# for relation in relations:
#     print(f" Book's Title: {relation.book.title} => price: {relation.book.price}")
# # print(len(relations))


# who has written Mahabaharat?

relations = BookAuthor.objects(book=mahabharat)
for relation in relations:
    print(relation.author.name)
# print(relations)
# print(len(relations))
