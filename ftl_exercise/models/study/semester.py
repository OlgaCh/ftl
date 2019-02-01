"""
Implements semester.
In my country semester usually has name like 1st/2nd or autumn/spring so adding name as a
property.
Properties:
 - name (string)
 - start_date (datetime)
 - end_date (datetime)
 - classes (list of Class_)
"""


class Semester():
    def __init__(self, name='', start_date=None, end_date=None, classes=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.classes = classes if classes else []

    def __str__(self):
        return f'{self.name} Semester. ' \
               f'Classes: {", ".join([c.get_class_name() for c in self.get_classes()])}'

    def get_classes(self):
        """
        Return list of Class taken at given Semester
        :return: list of Class
        """
        return self.classes

    def add_class(self, class_):
        """
        Adds class to the semester
        :param class_: Class_
        :return:
        """
        self.classes.append(class_)

    def get_students(self):
        """
        Return list of students who take classes in Semester
        :return: list of Student
        """
        students = [s for c in self.classes for s in c.get_students()]
        # allow only unique students
        students = list(set(students))
        return students
