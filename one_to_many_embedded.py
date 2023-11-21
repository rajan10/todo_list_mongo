"""One to Many
1. Question and Answers = Embedded"""

from utils import get_current_date
from enum import Enum
from mongoengine import (
    connect,
    StringField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    DateTimeField,
)

connect("relation_db")


class Answer(EmbeddedDocument):
    answer = StringField(max_length=100)
    created_at = DateTimeField(default=get_current_date)

    # def __str__(self):
    #     return f"{self.answer}>"


class Question(Document):
    question = StringField(max_length=100)
    created_at = DateTimeField(default=get_current_date)
    answers = ListField(EmbeddedDocumentField(Answer))

    def __str__(self):
        return f"<Question: {self.question}>"


# only Question CRUD operations  and in answers []
# answer=Answer()
# quesiton= Question_repo() [answer1,answer2]


class QuestionRepo:
    def create(self, question: str, answer_list: list) -> Question:
        answer_object_list = [Answer(answer=answer) for answer in answer_list]
        question = Question(question=question, answers=answer_object_list)
        question.save()
        return question

    def read_by_id(self, identifier: str) -> Question:
        question = Question.objects.get(id=identifier)
        return question

    def read_all(self) -> list[Question]:
        question_list = Question.objects()
        return list(question_list)

    def update_by_id(self, id: str, new_answers: list) -> Question:
        question_to_update = self.read_by_id(id)
        if question_to_update:
            # for each answer 'a' in new_answers, it creates an Answer object
            question_to_update.answers = [Answer(answer=a) for a in new_answers]
            question_to_update.save()
        return question_to_update

    def delete_by_id(self, identifier: str) -> None:
        question_to_delete = self.read_by_id(identifier)
        if question_to_delete:
            question_to_delete.delete()


question_repo = QuestionRepo()
# new_question = question_repo.create(
#     question="What is the capital of Canada?", answer_list=["Ottawa", "Toronto"]
# )

# question_object = question_repo.read_by_id(identifier="655c0214f5f0509b83c09ce3")
# # print(question_object)

# # print(question_object.answers)

# question_list = question_repo.read_all()
# for question in question_list:
#     print(question.answers)


# # questions = question_repo.read_all()
# # print(questions)

# update
# question_update = question_repo.update_by_id(
#     id="655c06da2607aa0a9368d0d2", new_answers=["Etobikoke", "Sherbourne"]
# )
# print(question_update)

# delete
question_repo.delete_by_id(identifier="655c06da2607aa0a9368d0d2")
