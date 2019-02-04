import pytest

from ftl_exercise.models.quiz.question import Question
from ftl_exercise.models.quiz.quiz import Quiz
from ftl_exercise.models.person.teacher import Teacher
from ftl_exercise.models.person.student import Student
from ftl_exercise.models.study.class_ import Class_
from ftl_exercise.models.study.assignment import Assignment


@pytest.fixture
def questions_list():
    yield [
        Question('A', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('B', {'a': 1, 'b': 0, 'c': 0, 'd': 0}),
        Question('C', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}),
        Question('D', {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0}),
    ]


@pytest.fixture
def answers():
    yield {
        'A': ['a', 'd'],
        'B': ['a'],
        'C': ['b', 'c'],
        'D': ['c', 'd'],
    }


@pytest.fixture
def quiz(questions_list):
    questions = questions_list
    yield Quiz('Quiz 1', questions)


@pytest.fixture
def teacher():
    yield Teacher('Gabriel', 'Marces')


@pytest.fixture
def student():
    yield Student('Jane', 'Doe')


@pytest.fixture
def class_(teacher, student):
    yield Class_('Test', teacher, [student])


@pytest.fixture
def assignment(quiz, answers):
    yield Assignment(quiz, answers)


def test_teacher_can_assign_quiz(teacher, quiz, class_, student):
    assert len(student.get_assignments()) == 0
    teacher.assign_quiz(quiz, class_)
    assert len(student.get_assignments()) == 1


def test_student_can_answer_on_assignment(teacher, quiz, class_, student, answers):
    # teacher creates assignment to class
    teacher.assign_quiz(quiz, class_)
    assignment = student.get_assignments()[0]
    # student doesn't provide any answers yet
    assert assignment.is_completed() is False
    # answers to assignment is recorded
    student.record_assignment_answer(assignment, answers)
    assert assignment.is_completed()


@pytest.mark.xfail
def test_each_question_can_be_answered_once(assignment):
    assignment.record_answer('A', ['b'])
    assert '"A": ["b"]' in str(assignment)


@pytest.mark.xfail
def test_question_can_be_answered_if_in_quiz(assignment):
    assignment.record_answer('E', ['a'])
    assert '"E": ["a"]' in str(assignment)


def test_assignment_can_be_graded(assignment):
    grade = assignment.validate_assignment()
    assert grade == 54


def test_student_can_make_partial_submissions(teacher, quiz, class_, student, answers):
    teacher.assign_quiz(quiz, class_)
    assignment = student.get_assignments()[0]
    assert assignment.is_completed() is False
    first_batch = {k: answers[k] for k in ['A', 'B']}
    second_batch = {k: answers[k] for k in ['C', 'D']}
    student.record_assignment_answer(assignment, first_batch)
    # assignment not completed yet
    assert assignment.is_completed() is False
    student.record_assignment_answer(assignment, second_batch)
    # assignment completed
    assert assignment.is_completed()
    # Grade is the same
    grade = assignment.validate_assignment()
    assert grade == 54


def test_teacher_can_grade_assignment(teacher, quiz, class_, student, answers):
    teacher.assign_quiz(quiz, class_)
    assignment = student.get_assignments()[0]
    student.record_assignment_answer(assignment, answers)
    # student doesn't have any grades yet
    assert student.student_grades() == {}
    teacher.grade_quiz(quiz, class_)
    # student got grade for assignment
    assert student.student_grades().get(quiz.get_name()) == 54
