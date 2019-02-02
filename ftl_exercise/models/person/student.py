"""
Implements Student class.
Main properties:
 - first_name (string)
 - last_name (string)
 -
"""

from ftl_exercise.models.person import Person


class Student(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignments = []

    def get_new_assignment(self, quiz):
        self.assignments.append(quiz)

    def get_assignments(self):
        return self.assignments
