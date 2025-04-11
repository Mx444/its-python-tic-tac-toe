import random

''' 
Gioco del Tris (Tic Tac Toe)

board : inizializza la matrice 3x3
player : simbolo del giocatore corrente
players : dizionario per memorizzare i nomi dei giocatori
opponent : tipo di avversario (PC o GIOCATORE)
'''
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

opponent = None
player = None
players = {}


'''
print_board() : Stampa la matrice 3x3
'''


def print_board():
    print("")
    print(
        f" {board[0][0] or ' '} | {board[0][1] or ' '} | {board[0][2] or ' '} ")
    print("-----------")
    print(
        f" {board[1][0] or ' '} | {board[1][1] or ' '} | {board[1][2] or ' '} ")
    print("-----------")
    print(
        f" {board[2][0] or ' '} | {board[2][1] or ' '} | {board[2][2] or ' '} ")
    print("")


'''
board_full() : Controlla se la matrice è piena
se è piena, ritorna True altrimenti False
e stampa il messaggio "Board piena!"
'''


def board_full():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    print("Board piena!")
    print_board()
    return True


'''
reset_board() : Resetta la matrice 3x3
'''


def reset_board():
    global board
    board = [["", "", ""] for _ in range(3)]
    print("Reset Board!")


'''
check_winner() : Controlla se c'è un vincitore
se c'è un vincitore, ritorna True altrimenti False
'''


def check_winner():
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False


'''
make_move(x, y) : Effettua una mossa
x : riga della matrice
y : colonna della matrice
'''


def make_move(x, y):
    global player

    if board[x][y] != "":
        print("Posizione già occupata!")
        return False

    board[x][y] = player

    if check_winner():
        print_board()
        print(f"Hai vinto, {players[player]} con il simbolo {player}!")
        reset_board()
        return True

    if board_full():
        print("Pareggio!")
        reset_board()
        return True

    player = "O" if player == "X" else "X"
    return True


'''
computer_move() : Effettua una mossa del computer
'''


def computer_move():
    available = [(i, j) for i in range(3)
                 for j in range(3) if board[i][j] == ""]
    if available:
        random_move = random.choice(available)
        print(f"Il Computer gioca in posizione {random_move}")
        make_move(random_move[0], random_move[1])


'''
setup_game() : Inizializza il gioco
'''


def setup_game():
    global player, players, opponent

    print("Gioco del Tris!")
    while True:
        mode_input = input(
            "Vuoi giocare contro il PC o contro un altro giocatore? (PC/GIOCATORE): ").strip().upper()
        if mode_input in ["PC", "GIOCATORE"]:
            opponent = mode_input
            break
        else:
            print("Inserisci 'PC' oppure 'GIOCATORE'.")

    if opponent == "PC":
        nome1 = input("Inserisci il tuo nome: ").strip()
        nome2 = "Computer"
        simbolo1 = ""
        while simbolo1 not in ["X", "O"]:
            simbolo1 = input(
                f"{nome1}, scegli il tuo simbolo (X/O): ").strip().upper()
        simbolo2 = "O" if simbolo1 == "X" else "X"
        print(f"{nome2} avrà il simbolo {simbolo2}.")
        players[simbolo1] = nome1
        players[simbolo2] = nome2
        player = simbolo1
    else:
        nome1 = input("Inserisci il nome del Giocatore 1: ").strip()
        nome2 = input("Inserisci il nome del Giocatore 2: ").strip()
        simbolo1 = ""
        while simbolo1 not in ["X", "O"]:
            simbolo1 = input(
                f"{nome1}, scegli il tuo simbolo (X/O): ").strip().upper()
        simbolo2 = "O" if simbolo1 == "X" else "X"
        print(f"{nome2} avrà il simbolo {simbolo2}.")
        players[simbolo1] = nome1
        players[simbolo2] = nome2
        player = simbolo1

    print_board()


'''
main() : Funzione principale del gioco
'''


def main():
    setup_game()
    while True:
        print_board()
        print(f"Tocca a {players[player]} ({player}).")
        if players[player].upper() == "COMPUTER":
            computer_move()
            continue
        try:
            x = int(input("Inserisci la riga (0-2): "))
            y = int(input("Inserisci la colonna (0-2): "))
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Posizione non valida!")
                continue
            make_move(x, y)
        except ValueError:
            print("Input non valido! Inserisci un numero.")
            continue


if __name__ == "__main__":
    main()
