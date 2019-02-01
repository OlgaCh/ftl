"""
Implements Quiz.
Assumings:
* each quiz has no end date and could be completed within semester.
* quiz should be validated as per number of correctly answered questions in relation to overall
  number of questions (converted to %). Thus max grade - 100%.
* It is ok to round quiz grade to the nearest int number in favor of student, i.e. both 87.2% and 87.8%
  are converted to 88% grade.

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
