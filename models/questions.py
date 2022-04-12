# Classes related to the questions.

from models.base_model import BaseModel
import random

class Question(BaseModel):
    def __init__(self,database):
        BaseModel.__init__(self,database)


    def get_questions(self,category):
        self.execute('select * from questions where category_id = ?', (category,))
        self.questions = self.fetchall()
    

    def show_random_question(self):
        self.round_question = random.choice(self.questions)
        print('\n'+self.round_question[2])


    def pass_id(self) -> int:
        return self.round_question[0]