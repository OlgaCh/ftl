import pytest
from datetime import datetime

from ftl_exercise.models.quiz.question import Question
from ftl_exercise.models.person.teacher import Teacher
from ftl_exercise.models.person.student import Student
from ftl_exercise.models.study.class_ import Class_
from ftl_exercise.models.study.semester import Semester


@pytest.fixture
def teacher_1():
    yield Teacher('Gabriel', 'Marces')


@pytest.fixture
def teacher_2():
    yield Teacher('Michelle', 'Garcia')


@pytest.fixture
def student_1():
    yield Student('Jane', 'Doe')


@pytest.fixture
def student_2():
    yield Student('James', 'Bond')


@pytest.fixture
def student_3():
    yield Student('Donald', 'Duck')


@pytest.fixture
def class_1(teacher_1, student_1):
    yield Class_('Class 1', teacher_1, [student_1])


@pytest.fixture
def class_2(teacher_2, student_2, student_3):
    yield Class_('Class 2', teacher_2, [student_2, student_3])


@pytest.fixture
def class_3(teacher_1, student_1, student_3):
    yield Class_('Class 3', teacher_1, [student_1, student_3])


@pytest.fixture
def semester(class_1, class_2, class_3):
    yield Semester(name='Spring', start_date=datetime(2019, 2, 1), end_date=datetime(2019, 6, 1),
                   classes=[class_1, class_2, class_3])


@pytest.fixture
def questions_list_1():
    yield [
        Question('A', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('B', {'a': 1, 'b': 0, 'c': 0, 'd': 0}),
        Question('C', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}),
        Question('D', {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0}),
    ]


@pytest.fixture
def answers_1_1():
    yield {
        'A': ['a', 'd'],
        'B': ['a'],
        'C': ['b', 'c'],
        'D': ['c', 'd'],
    }


@pytest.fixture
def questions_list_2():
    yield [
        Question('B', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('D', {'a': 1, 'b': 0, 'c': 0, 'd': 0}),
        Question('A', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}),
        Question('C', {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0}),
    ]


@pytest.fixture
def answers_2_2():
    yield {
        'A': ['a', 'd'],
        'B': ['a'],
        'C': ['b', 'c'],
        'D': ['c', 'd'],
    }


@pytest.fixture
def answers_3_2():
    yield {
        'A': ['a'],
        'B': ['b', 'd'],
        'C': ['b', 'c'],
        'D': ['c', 'd'],
    }


@pytest.fixture
def questions_list_3():
    yield [
        Question('C', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('A', {'a': 1, 'b': 0, 'c': 0, 'd': 0}),
        Question('B', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}),
        Question('D', {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0}),
    ]


@pytest.fixture
def answers_1_3():
    yield {
        'A': ['a', 'd'],
        'B': ['a'],
        'C': ['b', 'c'],
        'D': ['c', 'd'],
    }


@pytest.fixture
def answers_3_3():
    yield {
        'A': ['d'],
        'B': ['b', 'c'],
        'C': ['c'],
        'D': ['a', 'b', 'c'],
    }


def test_semester_grades_provided(semester, teacher_1, teacher_2, student_1, student_2, student_3,
                                  questions_list_1, questions_list_2, questions_list_3,
                                  class_1, class_2, class_3,
                                  answers_1_1, answers_1_3, answers_2_2, answers_3_2, answers_3_3):
    # teachers create and assign quizes
    quiz_1 = teacher_1.create_quiz('Quiz 1', questions_list_1)
    teacher_1.assign_quiz(quiz_1, class_1)
    quiz_2 = teacher_2.create_quiz('Quiz 2', questions_list_2)
    teacher_2.assign_quiz(quiz_2, class_2)
    quiz_3 = teacher_1.create_quiz('Quiz 3', questions_list_3)
    teacher_1.assign_quiz(quiz_3, class_3)

    # students has quizes
    assert len(student_1.get_assignments()) == 2
    assert len(student_2.get_assignments()) == 1
    assert len(student_3.get_assignments()) == 2

    # students answer on quizes
    student_1.record_assignment_answer(student_1.get_assignments()[0], answers_1_1)
    student_1.record_assignment_answer(student_1.get_assignments()[1], answers_1_3)
    student_2.record_assignment_answer(student_2.get_assignments()[0], answers_2_2)
    student_3.record_assignment_answer(student_3.get_assignments()[0], answers_3_2)
    student_3.record_assignment_answer(student_3.get_assignments()[1], answers_3_3)

    # students completes quizes
    assert all([a.is_completed() for a in student_1.get_assignments()])
    assert all([a.is_completed() for a in student_2.get_assignments()])
    assert all([a.is_completed() for a in student_3.get_assignments()])

    # students don't have grades yet
    assert student_1.student_grades() == {}
    assert student_2.student_grades() == {}
    assert student_3.student_grades() == {}

    # teachers grade assignments
    teacher_1.grade_quiz(quiz_1, class_1)
    teacher_2.grade_quiz(quiz_2, class_2)
    teacher_1.grade_quiz(quiz_3, class_3)

    # students have grades for quizes
    print(str(student_1), student_1.student_grades())
    print(str(student_2), student_2.student_grades())
    print(str(student_3), student_3.student_grades())
    assert len(list(student_1.student_grades().keys())) == 2
    assert student_1.student_grades() == {'Quiz 1': 54, 'Quiz 3': 70}
    assert len(list(student_2.student_grades().keys())) == 1
    assert student_2.student_grades() == {'Quiz 2': 20}
    assert len(list(student_3.student_grades().keys())) == 2
    assert student_3.student_grades() == {'Quiz 2': 33, 'Quiz 3': 54}

    # teachers create cumulative grade per semester
    teacher_1_sem_grade = teacher_1.calculate_total_grade_per_student(semester)
    teacher_2_sem_grade = teacher_2.calculate_total_grade_per_student(semester)
    assert teacher_1_sem_grade == [('Jane Doe', 62), ('Donald Duck', 54)]
    assert teacher_2_sem_grade == [('James Bond', 20), ('Donald Duck', 33)]
