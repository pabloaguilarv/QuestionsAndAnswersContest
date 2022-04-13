# Classes related to the rounds.

class Round():
    def __init__(self,prizes,current_player):
        self.prizes = prizes
        self.player = current_player

    def desist(self,category):
        print('Exiting game.')
        if category < 2:
            print('No prizes earned.')
            return
        self.player._set_prize(self.prizes[category-2])
        self.player._set_rank(category-1)
        self.player.save_stats()
        print(f'Prize won: ${self.player._prize: ,.0f}. Rank achieved: {self.player._rank}.')


    def award(self,category):
        self.player._set_prize(self.prizes[category-1])
        self.player._set_rank(category)
        print(f'Correct! Round {category} cleared.')
    

    def endgame(self,category):
        self.player._set_prize(0)
        self.player._set_rank(category-1)
        self.player.save_stats()
        print('Wrong answer. Game Over.')
        print('No prize awarded.')


    def completed(self,category):
        if category < 5:
            return
        self.player.save_stats()
        print('Congratulations! You completed the game!')
        print(f'You won ${self.player._prize: ,.0f} and your highest rank is now {self.player._rank}!')


    def show_prizes(self):
        for index,prize in enumerate(self.prizes):
            print(f'Rank {index+1}: ${prize: ,.0f} USD')
        print('\nStarting Round 1...')

    def show_round_prize(self,category):
        print(f'For ${self.prizes[category-1]: ,.0f} USD')

    
    def show(self,category):
        print(f'Round {category}')

    def show_answer(self,options,player_answer):
        print(f'{player_answer}: {options.options[player_answer][1]}')