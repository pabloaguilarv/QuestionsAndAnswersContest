#Get question options, show and verify answer.

from models.base_model import BaseModel

letters = ['A','B','C','D']

class Options(BaseModel):
    def __init__(self,database):
        BaseModel.__init__(self,database)


    def get_options(self,question_id):
        self.execute('select * from options where question_id = ?', (question_id,))
        self.options = dict(zip(letters,self.fetchall()))
    

    def show_options(self):
        for index,option in self.options.items():
            print(f'{index}: {option[1]}')
    

    def check_answer(self,player_answer) -> bool:
        if self.options[player_answer][-1]:
            return True
        return False