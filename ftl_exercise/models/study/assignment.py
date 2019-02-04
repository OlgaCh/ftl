"""
Implements Assignment class.
Each assignment created per quiz. Every student have same quiz only once.
Assignment allows to record student's answers and make partial submissions.
It is not defined in original spec. But assume that student can't change answer once it was recorded.
Properties:
- quiz
- assignment_answers
"""
import logging
import json


class Assignment():
    def __init__(self, quiz=None, answers=None):
        self.quiz = quiz
        self.assignment_answers = answers if answers else {}

    def __str__(self):
        nl = '\n'
        return f'{str(self.quiz)}. {nl}' \
               f'Answers provided:{nl}{json.dumps(self.assignment_answers)}'

    def get_quiz(self):
        """
        Return name of quiz
        :return: str
        """
        return self.quiz.get_name()

    def is_completed(self):
        """
        Return True if student answer all questions in quiz. False otherwise
        :return: bool
        """
        total_questions = self.quiz.get_number_of_questions()
        return len(self.assignment_answers) == total_questions

    def record_answer(self, question, answers):
        """
        Add new answer(s) to the assignment. If it's not possible raise warning.
        :param question: Question - to answer
        :param answers: list of str - list of selected answers
        """
        if question in self.quiz.get_questions_text() and question not in self.assignment_answers:
            self.assignment_answers[question] = answers
        else:
            logging.warning(f'Can\'t records answers {", ".join(answers)} for {question}')

    def validate_assignment(self):
        """
        Return grade for the assignment in percents from 0 to 100.
        :return: int
        """
        if not self.is_completed():
            # Using here Exception class but custom exception class may be created
            raise Exception('Can\'t validate assignment which is not completed.')
        total_questions = len(self.assignment_answers)
        quiz_with_answers = self.quiz.to_dict()
        grade = 0
        for question, answers in self.assignment_answers.items():
            quiz_question = quiz_with_answers.get(question)
            grade += sum([quiz_question.get(a) for a in answers])
        return int(grade/total_questions*100)
