"""
Implements Quiz.
Assumings:
* each quiz has no end date and could be completed within semester.
* quiz should be validated as per number of correctly answered questions in relation to overall
  number of questions (converted to %). Thus max grade - 100%.
* we're not penalizing grade if incorrect answer was chosen (whereas ideally should to)

Properties:
- name (str)
- questions (list of Question)
"""


class Quiz():
    def __init__(self, name='', questions=None):
        self.name = name
        self.questions = questions if questions else []

    def __str__(self):
        nl = '\n'
        return f'Quiz {self.name}. ' \
               f'Questions:{nl}{nl.join([str(q) for q in self.questions])}'

    def add_question(self, question):
        """
        Add question to the existing quiz
        :param question: Question
        """
        self.questions.append(question)

    def get_questions(self):
        """
        Return all questions which belong to quiz
        :return: list of Question
        """
        return self.questions

    def get_questions_text(self):
        """
        Helper method to return question text only
        :return: list of str
        """
        return [q.get_text() for q in self.questions]

    def get_number_of_questions(self):
        """
        Return number of questions which are in the quiz
        :return: int
        """
        return len(self.questions)

    def to_dict(self):
        """
        Converts quiz and all it's questions to dict.
        :return: dict
        """
        return {q.get_text(): q.get_options() for q in self.questions}

    def get_name(self):
        """
        Return name of quiz
        :return: str
        """
        return self.name
