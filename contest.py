# Main file for Questions and Answer Contest

from players import Player
from questions import Questions, Options
from prizes import Prize
from database import Database as DB
import time

prizes = Prize().create_list()

def start_game(prizes):
    questions = Questions()
    options = Options()
    
    for round in [1,2,3,4,5]:
        questions.get_questions('contest.db',round)
        questions.show_random_question()
        
        options.get_options(questions.round_question)

        # Give some time to read and make it look cool
        time.sleep(10)
        while True:
            options.show_options()
            player_answer = input('Enter your answer: ')

            if player_answer not in ['A','B','C','D']:
                print('\nSelect a valid option.')
            else:
                break
        
        if player_answer==questions.round_question:
            # If correct, collect prize and continue with next rank.
            pass


def check_player():
    pass


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
        current_player = Player(input('Enter your name:\n'))

        print(f'\nHello {current_player.name}.\n\nThese are the prizes that you can get:\n')

        for index,prize in enumerate(prizes):
            print(f'Rank {index}: ${prize: ,.0f} USD')

        start_game(prizes,current_player)