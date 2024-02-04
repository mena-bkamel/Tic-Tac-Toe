import os

players = {"A": "X",
           "B": "O"
           }
list = [" ", " ", " ", " ", " ", "  ", " ", " ", " "]


def game_over(char):
    if list[0] == players[char] and list[1] == players[char] and list[2] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    elif list[3] == players[char] and list[4] == players[char] and list[5] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    elif list[6] == players[char] and list[7] == players[char] and list[8] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    # ************
    elif list[0] == players[char] and list[3] == players[char] and list[6] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    elif list[1] == players[char] and list[4] == players[char] and list[5] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    elif list[2] == players[char] and list[5] == players[char] and list[8] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True
    # ******************

    elif list[0] == players[char] and list[4] == players[char] and list[8] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True

    elif list[2] == players[char] and list[4] == players[char] and list[6] == players[char]:
        print(f"Player {char} is the winner 🏆")
        return True


# *-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*---*--*-

continue_game = True
chosen_places = []

while continue_game:
    for key in players:
        os.system("cls")
        graph = f"{list[0]} | {list[1]} | {list[2]}\n---------\n{list[3]} | {list[4]} | {list[5]}\n---------\n{list[6]} | {list[7]} | {list[8]}"
        print(graph)

        try:
            answer = int(input(f"Player {key}: choose a number "))

            while answer in chosen_places:
                print("$$ This number has been already chosen before.choose another number $$")
                answer = int(input(f"Player {key}: choose a number "))
            else:
                chosen_places.append(answer)
                list[answer - 1] = players[key]

        except ValueError as error:
            print(f"{error} is not valid")
            answer = int(input(f"Player {key}: choose a number "))

        if game_over(key):
            continue_game = False
            graph = f"{list[0]} | {list[1]} | {list[2]} \n{list[3]} | {list[4]} | {list[5]} \n{list[6]} | {list[7]} | {list[8]} "
            print(graph)
            break
        else:

            os.system("cls")
