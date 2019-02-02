"""
Implements basic Question class.

Each question has few options available.
Assume that each question could have 1pt at max. So if 2 options may be chosen each of those
will cost 0.5pt, if 3 options - 0.33pt. Maximum number of different options per question allowed - 5.

Ideally we should validate that teacher provide correct cost for each option within a question and
enter between 3 and 5 options per question.

Properties:
- question_str (str)
- options (dict with option text as a key and it's weight as value.

N.B. In real system I'd prefer to make option key as a hash out of it's text to keep it short enough.
Then for each hash key create nested dict with question text and weight as values.
But since it's poc assume that answer is short enough to keep it as a key.
"""
import logging

from ftl_exercise.utils import MAX_ANSWERS, MIN_ANSWERS


class Question():
    def __init__(self, question_str='', options=None):
        self.question_str = question_str
        self.options = options if options else {}

    def __str__(self):
        nl = '\n'
        return f'Question: {self.question_str}{nl}' \
               f'Options:{nl}{nl.join(list(self.options.keys()))}'

    def add_option(self, option_text, option_val):
        """
        Adding new option to the existing question
        :param option_text: potential answer for question
        :param option_val (float): it's weight
        """
        if len(list(self.options.keys())) <= MAX_ANSWERS - 1 and \
                sum(list(self.options.values())) + option_val <= 1 and \
                not self.options.get(option_text):
            self.options[option_text] = option_val
        else:
            logging.warning(f'Can\'t add new option. '
                            f'Option text: {option_text}, Option value: {option_val}')

    def validate_options_cost(self):
        """
        All answers of the question should provide 1.0 point in total.
        """
        return sum(list(self.options.values())) == 1

    def validate_options_count(self):
        """
        Each test should have from 3 to 5 options
        """
        return len(list(self.options.keys())) in range(MIN_ANSWERS, MAX_ANSWERS + 1)

    def validate_question(self):
        """
        Validates question created on different criterias.
        :return: bool - True if question valid, False otherwise
        """
        return self.validate_options_cost() and self.validate_options_count()

    def get_text(self):
        """
        Return text of a question.
        :return: str
        """
        return self.question_str

    def get_options(self):
        """
        Return all options question has
        :return: dict
        """
        return self.options
