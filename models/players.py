# Classes related to Player

from models.base_model import BaseModel

class Player(BaseModel):
    def __init__(self, name):
        self.name = name
        BaseModel.__init__(self,'models/players.db')


    def save_player(self):
        self.execute('insert into players (name) values(?)', (self.name,))
        self._id = self.cursor.lastrowid
        self.commit()
    
    
    def get_player(self):
        self.execute('select name from players where name=?', (self.name,))
        if self.fetchOne() is None:
            return
        print('Player is already in database. Start again and enter your ID.')
        return exit()

    def _show_id(self):
        print(f'Please, save your ID to check your stats later: {self._id}')
        

    def get_stats(self):
        self.execute('select * from players where id = ?',(self._id,))
        stats = self.fetchOne()
        self.name,self.max_rank,self.max_prize = stats[1],stats[2],stats[3]


    def show_stats(self):
        if self.max_prize == None or self.max_rank == None:
            print('No stats available yet. Play a game and get past round 1 to get stats.')
            return
        print(f"{self.name}'s max rank achieved is rank {self.max_rank} and max prize is ${self.max_prize: ,.0f}.")


    def save_stats(self):
        self.execute('select * from players where id = ?',(self._id,))
        stats = self.fetchOne()

        if stats[2] is None or stats[2] < self._rank: #Compare max rank achieved
            self.execute('update players set max_rank = ? where id = ?',(self._rank, self._id))

        if stats[3] is None or stats[3] < self._prize: #Compare max prize achieved
            self.execute('update players set max_prize = ? where id = ?',(self._prize, self._id))
        self.commit()


    def _set_rank(self,rank):
        self._rank = rank


    def show_score(self):
        print(f'Current prize: ${self._prize: ,.0f}. Current Rank: {self._rank}.\n')


    def _set_prize(self,prize):
        self._prize = prize


class AlreadyPlayer(Player):
    def __init__(self,id):
        BaseModel.__init__(self,'models/players.db')
        self._id = id
        

    def get_player(self):
        self.execute('select name from players where id = ?',(self._id,))
        self.name = self.fetchOne()
        if self.name == None:
            print('No player found with the given ID.')
            return exit()
        self.name = self.name[0]
    

    def save_player(self):
        pass    