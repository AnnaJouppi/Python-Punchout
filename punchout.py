import random
import time

# Global variables
commands = ['H - Help and instructions', 'S - Start game', 'X - Exit game']

# Initializing classes and objects

# Classes
class Character():
    name = ''
    age = ''
    nationality = ''
    strength = ''
    weakness = ''
    regular = ''
    def __init__(self, name = '', age = '', nationality = '', strength = '', weakness = '', regular = ''):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.strength = strength
        self.weakness = weakness
        self.regular = regular

class Move():
    def __init__(self):
        self.moves = {
    'Punch' : random.randrange(10, 40),
    'Kick' : random.randrange(10, 40),
    'Throw' : random.randrange(10, 40)
    }

# Objects for characters, stored in dictionary for easy access in character selection

characters = {
    'Anna': Character('Anna Flashfingers', '22', 'Finnish', 'Punch', 'Kick', 'Throw'), 
    'Duke' : Character('Duke Danger', '67', 'American', 'Throw', 'Punch', 'Kick'),
    'Nova' : Character('Nova Starlight', '30', 'Japanese', 'Kick', 'Throw', 'Punch'),
    'Isabelle' : Character('Isabelle Ironlegs', '96', 'Danish', 'Kick', 'Punch', 'Throw'),
    'Bobby' : Character('Bobby Backbreaker', '24', 'Irish', 'Throw', 'Kick', 'Punch'),
    'Max' : Character('Max Muscles', '51', 'French', 'Punch', 'Throw', 'Kick')}

# Main function where the fight takes place

def fight():
         # Choosing a random character for AI, and it's strength and weakness
        ai_character = random.choice(list(characters.values()))
        ai_character_name = ai_character.name
        ai_character_strength = ai_character.strength
        ai_character_weakness = ai_character.weakness
        ai_character_regular = ai_character.regular

        # Choosing a character for player
        print('\nFighters:\n'.upper())
        for character in characters.values():
            print(f'Name: {character.name} | Age: {character.age} | Nationality: {character.nationality} | Strength: {character.strength} | Weakness: {character.weakness}')
        print(f"\nAiOpponent's fighter: {ai_character_name} !")
        player_character_name = None
        while player_character_name is None:
            player_name = input(f'\nChoose your fighter by typing their first name:\n')
            # Chooses the key in the characters dictionary
            player_character = player_name.capitalize()

            try:
                player_character_name = characters[player_character].name
                print(f'\nYour fighter: {player_character_name} !')
            except KeyError:
                print(f"Fighter by that name does not exist. Please try again!")  
    
        # Fight rounds begin
        winner_ai = 0
        winner_player = 0
        round = 1

        for i in range(3):
            aiOpponent_hp = 100
            player_hp = 100
            round_str = f'ROUND {round}'
            round += 1
            if round == 4:
                round_str = 'FINAL ROUND'

            print(f'\n*** {player_character_name} VS {ai_character_name} {round_str} ***\n')
        
            while aiOpponent_hp > 0 and player_hp > 0:
                player_move_list = ['p', 'P', 'k', 'K', 't', 'T']

                while True:
                    try:
                        player_move = input(f'Your turn! P - Punch, K - Kick T - Throw\n')
                        if player_move not in player_move_list:
                            raise ValueError
                    except ValueError:
                            print('The move does not exist!')
                    else:
                        break

                # AI moves
                
                # Probabilities for AI to use it's moves
                strength_prob = 0.6
                regular_prob = 0.3

                random_num = random.random()

                # if number is less than 0.6, 60% chance
                if random_num < strength_prob:
                    move_name = ai_character_strength
                    move_dmg = Move().moves[ai_character_strength] + 5

                # if number is less than 0.9 but higher than 0.6, 30% chance
                elif random_num < strength_prob + regular_prob:
                    move_name = ai_character_regular
                    move_dmg = Move().moves[ai_character_regular]

                # if number is more than 0.9, 10% chance
                else:
                    move_name = ai_character_weakness
                    move_dmg = Move().moves[ai_character_weakness] - 5

                # Player moves

                # Punch
                if (player_move == 'P' or player_move == 'p') and aiOpponent_hp > 0:
                    player_move_name = 'punch'
                    player_dmg = Move().moves['Punch']
                    # Checking for weakness and strength
                    if characters[player_character].strength == 'Punch':
                        player_dmg += 5
                    elif characters[player_character].weakness == 'Punch':
                        player_dmg -= 5

                    aiOpponent_hp -= player_dmg
                    player_hp -= move_dmg
                    print(f'Your {player_move_name.upper()} did {player_dmg} damage!')
                    print(f"AiOpponent's {move_name.upper()} did {move_dmg} damage!\n")
                    print(f'You now have {player_hp} hp left!')
                    print(f'{ai_character_name} now has {aiOpponent_hp} hp left!\n')

                # Kick
                elif (player_move == 'K' or player_move == 'k') and aiOpponent_hp > 0:
                    player_move_name = 'kick'
                    player_dmg = Move().moves['Kick']

                    # Checking for weakness and strength
                    if characters[player_character].strength == 'Kick':
                        player_dmg += 5
                    elif characters[player_character].weakness == 'Kick':
                        player_dmg -= 5

                    aiOpponent_hp -= player_dmg
                    player_hp -= move_dmg
                    print(f'Your {player_move_name.upper()} did {player_dmg} damage!')
                    print(f"AiOpponent's {move_name.upper()} did {move_dmg} damage!\n")
                    print(f'You now have {player_hp} hp left!')
                    print(f'{ai_character_name} now has {aiOpponent_hp} hp left!\n')

                # Throw
                elif (player_move == 'T' or player_move == 't') and aiOpponent_hp > 0:
                    player_move_name = 'throw'
                    player_dmg = Move().moves['Throw']

                    # Checking for weakness and strength
                    if characters[player_character].strength == 'Throw':
                        player_dmg += 5
                    elif characters[player_character].weakness == 'Throw':
                        player_dmg -= 5

                    aiOpponent_hp -= player_dmg
                    player_hp -= move_dmg
                    print(f'Your {player_move_name.upper()} did {player_dmg} damage!')
                    print(f"AiOpponent's {move_name.upper()} did {move_dmg} damage!\n")
                    print(f'You now have {player_hp} hp left!')
                    print(f'{ai_character_name} now has {aiOpponent_hp} hp left!\n')

                # determining the winner of the round
                if aiOpponent_hp <= 0 and player_hp <= 0:
                    print("IT'S A TIE!")
                elif aiOpponent_hp < 0 and player_hp > 0:
                    print('YOU WIN THE ROUND!')
                    winner_player += 1
                elif aiOpponent_hp > 0 and player_hp < 0:
                    print('AIOPPONENT WINS THE ROUND!')
                    winner_ai += 1

        # determining the winner of the whole battle
        if winner_ai < winner_player:
            print('YOU ARE THE BATTLE WINNER!\n')
        if winner_ai > winner_player:
            print('AI IS THE BATTLE WINNER!\n')
        if winner_ai == winner_player:
            print('BATTLE ENDS WITH A TIE!\n')
        
        print(f'Battle results:\nRounds won by you: {winner_player}\nRounds won by {ai_character_name}: {winner_ai}\n ')

# Printing main menu commands
def main_program():
    print('\n')
    print('**** PYTHON PUNCHOUT ****\n')
    print("Welcome to Python Punchout! This command line fighthing game features:\n\n* Six different characters with weaknesses and strengths affecting damage\n* An AI Opponent chosen at random\n* Three rounds of fighting\n* Three magnificent moves: Punch, Kick and Throw\n\nPress S to start fighthing!\n")

    while True:
        for i in commands:
            print(i)

        # H - Help
        user_command = input('\nChoose a command: \n')
        try:
            if user_command == 'H' or user_command == 'h':
                with open('help.txt', 'r') as file:
                    for line in file:
                        print(line.strip())
            # S - Start game
            elif user_command == 'S' or user_command == 's':
                fight()
            # X - Exit game
            elif user_command == 'X' or user_command == 'x':
                while True: 
                    try:  
                        user_verify = input('Are you sure you want to exit the game? Y - Yes, N - No ')
                        if user_verify == 'Y' or user_verify == 'y':
                            print('Thank you for playing!')
                            time.sleep(3) # Closes command line window after 3s
                            break
                        elif user_verify == 'N' or user_verify == 'n':
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("\nPlease enter a valid command.\n")
                if user_verify == "Y" or user_verify == "y":
                    break
            else:
                raise ValueError
        except ValueError:
            print("\nPlease enter a valid command.\n")
main_program()