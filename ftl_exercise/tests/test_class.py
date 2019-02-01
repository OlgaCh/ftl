import pytest
from datetime import datetime

from ftl_exercise.models.person.student import Student
from ftl_exercise.models.person.teacher import Teacher
from ftl_exercise.models.study.class_ import Class_
from ftl_exercise.models.study.semester import Semester
from ftl_exercise.utils import DATE_PATTERN


@pytest.fixture
def teacher():
    yield Teacher('Gabriel', 'Marces')


@pytest.fixture
def another_teacher():
    yield Teacher('Amy', 'Woodberg')


@pytest.fixture
def students():
    yield [
        Student('Jimmy', 'Morris'),
        Student('Miranda', 'Kerr'),
        Student('Candice', 'Swanepoel'),
        Student('James', 'Bond')
    ]


@pytest.fixture
def another_students():
    yield [
        Student('Jim', 'Carrey'),
        Student('James', 'Bond'),
        Student('Donald', 'Duck')
    ]


@pytest.fixture
def math_class(another_students, teacher):
    yield Class_(name='Math', teacher=teacher, students=another_students)


@pytest.fixture
def arts_class(students, another_teacher):
    yield Class_(name='Arts', teacher=another_teacher, students=students)


@pytest.fixture
def semester(arts_class, math_class):
    start_date = datetime.strptime('01/09/2018', DATE_PATTERN)
    end_date = datetime.strptime('31/12/2018', DATE_PATTERN)
    yield Semester('1st', start_date, end_date, [arts_class, math_class])


def test_class_init(math_class, arts_class):
    assert str(math_class) == 'Math class. Teacher - Gabriel Marces. Students: Jim Carrey, James Bond, Donald Duck'
    assert str(arts_class) == 'Arts class. Teacher - Amy Woodberg. Students: Jimmy Morris, Miranda Kerr, ' \
                              'Candice Swanepoel, James Bond'


def test_class_accept_new_student(math_class):
    old_students_count = math_class.get_total_students()
    s = Student('Peter', 'Thompson')
    math_class.add_student(s)
    assert math_class.get_total_students() == old_students_count + 1


def test_class_could_have_new_teacher(arts_class):
    new_teacher = Teacher('Donna', 'Sullivan')
    arts_class.assign_teacher(new_teacher)
    assert 'Donna Sullivan' in str(arts_class.get_teacher())


def test_semester_init(semester):
    assert str(semester) == '1st Semester. Classes: Arts, Math'


def test_get_semester_classes(semester, arts_class, math_class):
    assert {arts_class, math_class} == set(semester.get_classes())


def test_get_semester_students(semester):
    students = [str(s) for s in semester.get_students()]
    assert set(students) == {'Jim Carrey', 'James Bond', 'Donald Duck', 'Jimmy Morris', 'Miranda Kerr',
                             'Candice Swanepoel'}
