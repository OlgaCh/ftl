**Task Description**

Please use your most proficient programming language to create object oriented design and
use test driven development to implement classes and methods with appropriate data structure
and test the code for the following scenario. Please add comments describing any assumptions
you make:

* There are Teachers
* There are Students
* Students are in classes that teachers teach
* Teachers can create multiple quizzes with many questions (each question is multiple choice)
* Teachers can assign quizzes to students
* Students solve/answer questions to complete the quiz, but they don't have to complete it at
once. (Partial submissions can be made).
* Quizzes need to get graded
* For each teacher, they can calculate each student's total grade accumulated over a semester
for their classes

**Project Structure**
Project consist of 2 main parts: `models` and `tests`.

`models` implements basic entities:
* `Person`, `Student`, `Teacher`;
* `Question`, `Quiz`;
* `Semester`, `Class`, `Assignment`;

as well as logic around those.

`tests` has `pytest` tests in to ensure that all logic works as expected.

**Tests**

To run test suit execute
> pytest

To check code clarity with flake run
> flake8


Gherkin test cases are placed into `gherkin` directory.
They cover study process from 2 pov: student and teacher.