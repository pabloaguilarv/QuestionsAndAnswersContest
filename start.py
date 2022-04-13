# Main file for Questions and Answer Contest

from http.client import CONTINUE
from models.players import AlreadyPlayer, Player
from models.questions import Question
from models.options import Options
from models.round import Round
import os
import time

prizes = [100,200,400,800,1600]

def clear_screen():
    os.system('cls')

def start_game(prizes,current_player):
    questions = Question('models/contest.db')
    options = Options('models/contest.db')
    round = Round(prizes,current_player)
    
    for category in range(1,6):
        questions.get(category)
        questions.get_random()
        options.get(questions.pass_id())

        while True:
            round.show(category)
            round.show_round_prize(category)
            questions.show_random()
            options.show()

            player_answer = input('\nEnter your answer (Enter E to exit with current prize): ').upper()

            if player_answer not in ['A','B','C','D','E']:
                clear_screen()
                print('\n\033[1;31;40mSelect a valid option.\033[0m')
            else:
                break
        
        if player_answer == 'E':
            round.desist(category)
            break
        elif options.check_answer(player_answer):
            clear_screen()

            round.show_answer(options,player_answer)
            round.award(category)
            current_player.show_score()
            round.completed(category)

            time.sleep(3); 'Allow some time before next question.'
            continue
        else:
            round.endgame(category)
            break


if __name__ == '__main__':

    os.system('python basedbcreation.py')
    clear_screen()

    print('\nWelcome to the Contest\nSelect one.')

    # Ensure the right input
    while True:
        try: first_option = int(input('\n1: Start game.\n2: Check player stats.\n3. Exit.\nOption: '))
        except:
            clear_screen()
            print('\n\033[1;31;40mPlease enter a valid option.\033[0m')
            continue

        if first_option not in [1,2,3]:
            clear_screen()
            print('\n\033[1;31;40mPlease enter a valid option.\033[0m')
        else:
            break
    
    clear_screen()

    # Start game or check player stats
    if first_option == 1:

        while True:
            try: second_option = int(input('\nStart game.\n\n1: New Player.\n2: I have an ID.\n3: Exit.\nOption: '))
            except:
                clear_screen()
                print('\n\033[1;31;40mPlease enter a valid option.\033[0m')
                continue
            
            if second_option not in [1,2,3]:
                clear_screen()
                print('\n\033[1;31;40mPlease enter a valid option.\033[0m')
            else:
                break

        if second_option == 1: # Create player
            current_player = Player(input('\nEnter your name: '))
            current_player.get_player()
            current_player.save_player()
            current_player._show_id()
            time.sleep(5); 'Allow player to see ID.'

        if second_option == 2:
            current_player = AlreadyPlayer(input('\nEnter your ID: '))
            current_player.get_player()
        
        if second_option == 3:
            exit()

        clear_screen()

        print(f'\nHello {current_player.name}.\n\nThese are the prizes that you can get:\n')

        pre_round = Round(prizes,current_player).show_prizes()

        time.sleep(5)
        clear_screen()
        start_game(prizes,current_player)

    if first_option == 2:
        current_player = AlreadyPlayer(input('\nEnter your ID: '))
        current_player.get_player()
        current_player.get_stats()
        current_player.show_stats()
    
    if first_option == 3:
        exit()