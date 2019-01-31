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


class Teacher(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def assign_quiz(self):
        """
        Creates quiz and assign it to class
        :return:
        """
        pass

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
