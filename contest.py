# Main file for Questions and Answer Contest

from models.players import Player
from models.questions import Question
from models.base_model import BaseModel as DB
from models.options import Options
import time

prizes = [100,200,400,800,1600]

def start_game(prizes):
    questions = Question('contest.db')
    options = Options('contest.db')
    
    for category in range(1,6):
        questions.get_questions(category)
        questions.show_random_question()
        options.get_options(questions.pass_id())

        while True:
            options.show_options()
            player_answer = input('Enter your answer: ')

            if player_answer not in ['A','B','C','D','']:
                print('\nSelect a valid option.')
            else:
                break
        
        'CONSIDER THE ROUND OBJECT TO HANDLE THE ANSWER SITUATIONS'
        if player_answer == '':
            desist(category,prizes)
            break
        elif options.check_answer(player_answer):
            award(category,prizes)
            continue
        else:
            endgame(category)
            break
    completed(prizes)

def desist(category,prizes):
    if category < 2:
        return
    current_player._set_prize(prizes[category-2])
    current_player._set_rank(category-1)
    current_player.save_stats()
    print('Exiting game.')


def award(category,prizes):
    current_player._set_prize(prizes[category-1])
    current_player._set_rank(category)
    print('Correct!')


def endgame(category):
    current_player._set_prize(0)
    current_player._set_rank(category-1)
    current_player.save_stats()
    print('Wrong answer. Game Over.')

def completed(prizes):
    current_player._set_prize(prizes(4))
    current_player._set_rank(5)
    current_player.save_stats()
    print('Congratulations! You completed the game!')

if __name__ == '__main__':

    print('\nWelcome to the Contest\nSelect an option:')

    # Ensure the right input
    while True:
        print('\n1: Start game.\n2: Check player stats.')
        try: option = int(input())
        except:
            print('\nPlease enter a valid option.')
            continue

        if option not in [1,2]:
            print('\nPlease enter a valid option.')
        else:
            break

    # Start game or check player stats
    if option:
        if int(input('\n1: New Player.\n2: I have an ID.')):
            current_player = Player(input('\nEnter your name:\n'),'players.db')
            current_player.save_player()
            current_player._show_id()

        print(f'\nHello {current_player.name}.\n\nThese are the prizes that you can get:\n')

        for index,prize in enumerate(prizes):
            print(f'Rank {index}: ${prize: ,.0f} USD')

        start_game(prizes,current_player)