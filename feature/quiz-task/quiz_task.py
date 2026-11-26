from abc import ABC, abstractmethod
from basetask.base_task import AcademicTask

class Quiz(AcademicTask):
    def __init__(self, title, max_points, total_questions):
        super().__init__(title, max_points)
        self.__total_questions = total_questions
        self.correct_answers = 0

    def submit_work(self, correct_answers):
        self.correct_answers = correct_answers
        print(f"Quiz submitted: {self.title}")

    def grade_work(self):
        self.max_points += (self.correct_answers - self.__total_questions)
        self.is_graded = True

    def get_details(self):
        print(f"[QUIZ] {self.title} - Max Points: {self.max_points}")
