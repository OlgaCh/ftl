"""
Implements Class of students
Each class has properties:
- name (string)
- teacher (Teacher)
- students (list of Student)
"""


class Class_():
    def __init__(self, name='', teacher=None, students=None):
        self.name = name
        self.teacher = teacher
        self.students = students if students else []

    def __str__(self):
        return f'{self.name} class. Teacher - {self.teacher}. ' \
               f'Students: {", ".join([str(s) for s in self.students])}'

    def add_student(self, student):
        """
        Add student to the class.
        For sake of simplicity assume that each student in the class is unique.
        :param student: Student
        """
        self.students.append(student)

    def get_students(self):
        """
        Return list of students in the class
        :return: list of Student
        """
        return self.students

    def assign_teacher(self, teacher):
        """
        Assign teacher to a class
        :param teacher: Teacher
        """
        self.teacher = teacher

    def get_teacher(self):
        """
        Return teacher of the class
        :return: Teacher
        """
        return self.teacher

    def get_class_name(self):
        """
        Return name of a given class
        :return: string
        """
        return self.name

    def get_total_students(self):
        """
        Return number of students taking the class
        :return: int
        """
        return len(self.students)
