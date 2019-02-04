"""
Implements Student class.
Main properties:
 - first_name (string)
 - last_name (string)
 - assignments (list) - all assignments which student needs to complete
 - grades (dict) - grades provided by teacher
"""

from ftl_exercise.models.person import Person
from ftl_exercise.models.study.assignment import Assignment


class Student(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignments = []
        self.grades = {}

    def get_new_assignment(self, quiz):
        """
        Accept new assignment from teacher
        :param quiz: Quiz to be completed
        """
        self.assignments.append(Assignment(quiz))

    def get_assignments(self):
        """
        Return all assignments completed by student
        :return: list of Assignment
        """
        return self.assignments

    def student_grades(self):
        """
        Get all grades obtained by student
        :return: dict with grades per assignment
        """
        return self.grades

    def record_assignment_answer(self, assignment, student_answers):
        """
        Allow student to answer on assignment questions.

        :param assignment: Assignment
        :param student_answers: dict - question as a key, answers as values
        """
        for question in student_answers:
            assignment.record_answer(question, student_answers.get(question))
