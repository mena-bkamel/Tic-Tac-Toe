from check_the_winner import GameOver
import os

players = {
    "Player-A": "X",
    "Player-B": "O"
}


def create_graph(array) -> None:
    print(f" {array[0]} | {array[1]} | {array[2]} \n{f"_" * 12} \n"
          f" {array[3]} | {array[4]} | {array[5]} \n{f"_" * 12}\n"
          f" {array[6]} | {array[7]} | {array[8]} \n")


cells = [" " for n in range(1, 10)]


def turn_ove(code: str, player: str) -> None:

    create_graph(cells)
    try:
        prompt = int(input(f'{player} write a number from 1-9: '))

    except ValueError as err:
        print(f"Error:{err}")
        turn_ove(code, player)
    else:
        try:
            cells[prompt - 1] = code
        except IndexError as err:
            print(f"Error: {err}")
            turn_ove(code, player)


def play_the_game(players_dic: dict, cells_list: list):
    game_continue = True

    while game_continue:
        os.system("cls")
        for player in players_dic:
            turn_ove(code=players_dic[player], player=player)

            if GameOver(cells, players_dic[player], player).check_answer():
                game_continue = False
                break
    create_graph(cells)


play_the_game(players, cells)


