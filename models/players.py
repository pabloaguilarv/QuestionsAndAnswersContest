# Classes related to Player

from models.base_model import BaseModel

class Player(BaseModel):
    def __init__(self, name):
        self.name = name
        BaseModel.__init__(self,'models/players.db')


    def save_player(self):
        self.execute('insert into players (name) values(?)', (self.name,))
        self._id = self.cursor.lastrowid
        # self.execute('select * from players order by id desc')
        # self._id = self.fetchone()[0]
        

    def _show_id(self):
        print(f'Please, save your ID to check your stats later: {self._id}')
        

    def get_stats(self,id):
        self.execute('select * from players where id = ?', (id,))
        stats = self.fetchone()
        self.name,self.max_rank,self.max_prize = stats[1],stats[2],stats[3]


    def show_stats(self):
        print(f"{self.name}'s max rank achieved is rank #{self.max_rank} and max prize is {self.max_prize}")


    def save_stats(self):
        self.execute('select * from players where id = ?',(self._id))
        stats = self.fetchone()
        if stats[2]< self._rank: #Compare max rank achieved
            self.execute('update players set max_rank = ? where id = ?',(self._rank, self._id))
        if stats[3] < self._prize: #Compare max prize achieved
            self.execute('update players set max_prize = ? where id = ?',(self._prize, self._id))


    'SHOULD I PUT SET RANK AND PRIZE TOGETHER?'
    def _set_rank(self,rank):
        self._rank = rank


    def _set_prize(self,prize):
        self._prize = prize


class AlreadyPlayer(Player):
    def __init__(self,id):
        BaseModel.__init__(self,'models/players.db')
        self._id = id
        self.execute('select name from players where id = ?',(self._id,))
        self.name = self.fetchone()[0]
    

    def save_player(self):
        pass    