from domain.domain_student import *
from domain.domain_subject import *

class Grade:
    def __init__(self, student_id, subject, grade):
        self.__grade = grade
        self.__student = student_id
        self.__subject = subject

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def __str__(self):
        return f"{self.get_student()} - {self.get_subject()}: {self.get_grade()}"


class StudentGradeDTO:
    def __init__(self, student_name, grade):
        self.__student_name = student_name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def get_name(self):
        return self.__student_name

    def __str__(self) -> str:
        return f'Studentul: {self.get_name()} - Nota: {self.get_grade()}'