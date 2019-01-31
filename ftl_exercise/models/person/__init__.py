"""
Implements basic Person class.
Main properties:
 - first_name (string)
 - last_name (string)
"""


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
