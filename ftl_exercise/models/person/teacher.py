"""
Implements Teacher class.
Main properties:
 - first_name (string)
 - last_name (string)
 - quizes (dict) - Dictionary representing all quizes created by this teacher. Quiz name assumed to be unique and
                   used as a key.

Class behavior:
 - assign_quiz - create quiz for class
 - grade_quiz - grade quiz answers
 - calculate_total_grade_per_student - provide accumulated grades per student per semester
"""

from ftl_exercise.models.person import Person
from ftl_exercise.models.quiz.quiz import Quiz


class Teacher(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.quizes = {}

    def create_quiz(self, name, questions):
        """
        Allow teacher to create new quiz
        :param topic: str Quiz name
        :param questions: list of Question - questions (and grades) which needs to be placed in quiz
        :return: Quiz
        """
        new_quiz = Quiz(name, questions)
        self.quizes[new_quiz.get_name()] = new_quiz
        return new_quiz

    def assign_quiz(self, quiz, class_):
        """
        Assign quiz to class teacher teach at.
        For each student of a class we create assignment with a copy of original quiz.
        Initially quiz has info on how it should be graded. This information provided with quiz data
        but shouldn't be shown to the student in UI (that part of hidding sensitive data is ommited per now).

        Adds new assignment for the quiz to each student.
        """
        for student in class_.get_students():
            student.get_new_assignment(quiz)

    def grade_quiz(self, quiz, class_):
        """
        Validate quiz answers provided by students and generate grades
        :return:
        """
        quiz_name = quiz.get_name()
        for student in class_.get_students():
            for assignment in student.get_assignments():
                # Assume that quiz same if name match
                if assignment.get_quiz() == quiz_name:
                    grade = assignment.validate_assignment()
                    self.set_student_grade(student, quiz_name, grade)
                    break

    def calculate_total_grade_per_student(self, semester):
        """
        Create cumulative grade for each student per current semester and course.
        :param semester: Semester - semester for which students needs to be graded
        :return: list of tuples - each tuple created from student's full name and overall grade
        """
        semester_grades = []
        seen_students = set()
        for class_ in semester.get_classes():
            # Skip classes which not handled by current teacher
            if str(class_.get_teacher()) != str(self):
                continue
            for student in class_.get_students():
                # Process each student only once
                if str(student) in seen_students:
                    continue
                seen_students.add(str(student))
                grades_count = 0
                grades_sum = 0
                grades = student.student_grades()
                for grade in grades:
                    # Grade only quizes created by this teacher.
                    if grade in self.quizes:
                        grades_count += 1
                        grades_sum += grades.get(grade)
                semester_grades.append((str(student), int(grades_sum/grades_count)))
        return semester_grades

    def set_student_grade(self, student, quiz_name, grade):
        """
        Provide grade to student once assignment completed

        :param student: Student
        :param quiz_name: str - Quiz which was graded
        :param grade: int - grade
        """
        student.grades[quiz_name] = grade
