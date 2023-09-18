# Ramkumar Arcot Dharmalingam || AI || [CODSOFT]
# TIC-TAC-TOE AI

import random

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, AI):
        return 1
    if is_winner(board, HUMAN):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = AI
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = HUMAN
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in get_available_moves(board):
        board[move[0]][move[1]] = AI
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]

    while True:
        print_board(board)
        if is_board_full(board):
            print("It's a draw!")
            break
        
        human_move = None
        while human_move not in get_available_moves(board):
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            human_move = (row, col)
        
        board[human_move[0]][human_move[1]] = HUMAN

        if is_winner(board, HUMAN):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        if is_winner(board, AI):
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
