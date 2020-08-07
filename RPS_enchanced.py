import random
import json

rolls = {}  # roster.json


def main():
    player1, player2 = get_names()
    show_header()
    load_roster()
    play_game(player1, player2)


def show_header():
    print("")
    print("  ######################  ")
    print("")
    print("  Rock Paper Scissors  ")
    print("     Enhanced edition. ")
    print("")
    print("  ######################  ")
    print("")


def get_names():
    player1 = input("What's your name? ")
    player2 = "Computer"

    return player1, player2


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}
    r_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roster(player_1, r_names)
        roll2 = random.choice(r_names)

        if not roll1:
            print("Try again...")
            continue

        print(f"{player_1} roll {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f'{winner} takes the round!')
            wins[winner] += 1

        print(f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}.")
        print()

    all_winner = find_winner(wins, wins.keys())
    print(f"{all_winner} wins the game!")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("Wow, the play was tied, there was like 4% of chances to get that!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roster(player_name, roll_names):
    print("Rolls: ")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_text = text

    selected_text.isnumeric()
    # print(selected_text.isnumeric())  # print test czy to liczba

    if selected_text.isnumeric() == True:
        selected_index = (int(selected_text) - 1)
        if selected_index < 0 or selected_index >= len(rolls):
            print(f"no nie, no po prostu no nie, {player_name}, {text}? - może kiedyś będzie więcej opcji...")
            return None

        return roll_names[selected_index]

    else:
        choice_test_fail()


def choice_test_fail():
    print("nie ma nie dziala")
    return None


def load_roster():
    global rolls

    file = 'roster.json'
    with open(file, 'r', encoding='utf-8') as fin1:
        rolls = json.load(fin1)


if __name__ == '__main__':
    main()
