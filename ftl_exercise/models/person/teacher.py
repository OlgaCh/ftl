"""
Implements Teacher class.
Main properties:
 - first_name (string)
 - last_name (string)

Class behavior:
 - assign_quiz - create quiz for class
 - grade_quiz - grade quiz answers
 - calculate_total_grade_per_student - provide accumulated grades per student per semester
"""

from ftl_exercise.models.person import Person
from ftl_exercise.models.quiz.quiz import Quiz
from ftl_exercise.models.study.assignment import Assignment


class Teacher(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_quiz(self, name, questions):
        """
        Allow teacher to create new quiz
        :param topic: str Quiz name
        :param questions: list of Question - questions (and grades) which needs to be placed in quiz
        :return: Quiz
        """
        return Quiz(name, questions)

    def assign_quiz(self, quiz, class_):
        """
        Assign quiz to class teacher teach at.
        For each student of a class we create assignment with a copy of original quiz.
        Initially quiz has info on how it should be graded. This information provided with quiz data
        but shouldn't be shown to the student in UI (that part of hidding sensitive data is ommited per now).

        Adds new assignment for the quiz to each student.
        """
        for student in class_.get_students():
            student.get_new_assignment(Assignment(quiz))

    def grade_quiz(self):
        """
        Validate quiz answers provided by students and generate grades
        :return:
        """
        pass

    def calculate_total_grade_per_student(self):
        """
        Create cumulative grade for each student per current semester and course
        :return:
        """
        pass
