import pytest

from ftl_exercise.models.quiz.question import Question
from ftl_exercise.models.quiz.quiz import Quiz
from ftl_exercise.models.person.teacher import Teacher


@pytest.fixture
def teacher():
    yield Teacher('Gabriel', 'Marces')


@pytest.fixture
def questions_list():
    yield [
        Question('A', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('B', {'a': 1, 'b': 0, 'c': 0, 'd': 0}),
        Question('C', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}),
        Question('D', {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0}),
        Question('E', {'a': 0, 'b': 0.4, 'c': 0.6, 'd': 0}),
        Question('F', {'a': 0, 'b': 0, 'c': 0, 'd': 1}),
        Question('G', {'a': 0.8, 'b': 0.2, 'c': 0, 'd': 0}),
        Question('H', {'a': 0, 'b': 0.33, 'c': 0.33, 'd': 0.34}),
        Question('I', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}),
        Question('J', {'a': 0, 'b': 0, 'c': 1, 'd': 0}),
        Question('K', {'a': 0, 'b': 0.5, 'c': 0, 'd': 0.5}),
    ]


@pytest.fixture
def quiz_1(questions_list):
    questions = questions_list[:4]
    yield Quiz('Quiz 1', questions)


@pytest.fixture
def quiz_2(questions_list):
    questions = questions_list[4:7]
    yield Quiz('Quiz 2', questions)


@pytest.fixture
def quiz_3(questions_list):
    questions = questions_list[7:]
    yield Quiz('Quiz 3', questions)


@pytest.mark.parametrize("name, options, is_valid", [
    ('A', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0}, True),
    ('B', {'a': 1, 'b': 0, 'c': 0, 'd': 0}, True),
    ('C', {'a': 0.33, 'b': 0.34, 'c': 0.33, 'd': 0}, True),
    ('D', {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0, 'e': 0}, True),
    ('E', {'a': 1, 'b': 0.5, 'c': 0.5, 'd': 0}, False),
    ('F', {'b': 0.5, 'c': 0.5}, False),
])
def test_if_question_valid(name, options, is_valid):
    q = Question(name, options)
    assert q.validate_question() == is_valid


@pytest.mark.parametrize("name, options, new_option_text, new_option_val", [
    ('A', {'a': 0, 'b': 0.5, 'c': 0.5}, 'd', 0),
    pytest.param('A', {'a': 0, 'b': 0.5, 'c': 0.5}, 'd', 1, marks=pytest.mark.xfail),
])
def test_adding_new_option_to_question(name, options, new_option_text, new_option_val):
    q = Question(name, options)
    q.add_option(new_option_text, new_option_val)
    assert new_option_text in str(q)


def test_teacher_create_quiz(teacher, quiz_1, questions_list):
    quiz = teacher.create_quiz('Quiz 1', questions_list[:4])
    assert str(quiz) == str(quiz_1)
