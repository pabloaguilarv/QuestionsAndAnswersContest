# Classes related to the questions.

from database import Database as DB
import random

class Questions():

    def get_questions(self,database,rank):
        with DB(database) as db:
            db.execute('select * from rank_'+str(rank))
            self.questions = db.fetchall()
    
    def show_random_question(self):
        self.round_question = random.choice(self.questions)
        print('\n'+self.round_question[1])

class Options():

    def get_options(self,question):
        self.options = question[2:6]

    def show_options(self):
        letters = ['A','B','C','D']
        for index,option in enumerate(self.options):
            print(f'{letters[index]}: {option}')