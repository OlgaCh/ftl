import pytest

from ftl_exercise.models.person import Person
from ftl_exercise.models.person.student import Student
from ftl_exercise.models.person.teacher import Teacher


@pytest.mark.parametrize("first_name, last_name, cls, name_to_string", [
    ('Jane', 'Doe', Person, 'Jane Doe'),
    ('Paul', 'Smith', Student, 'Paul Smith'),
    ('Mr. Garry', 'Bergman', Teacher, 'Mr. Garry Bergman'),
])
def test_person_has_name(first_name, last_name, cls, name_to_string):
    p = cls(first_name, last_name)
    assert str(p) == name_to_string


def test_new_student_has_no_assignments(name='Mary', last_name='Jane'):
    s = Student(name, last_name)
    assert len(s.assignments) == 0
