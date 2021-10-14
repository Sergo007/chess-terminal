#                     Mark all possible moves of chess Queen
#                     from dot $(r, c) inside chessboard
def get_figure_color(figure):
    if figure in '♜♞♝♛♚♟':
        return 'black'
    if figure in '♖♘♗♕♔♙':
        return 'white'
    return None


def get_move_tik(board, r, c, by_r, by_c):
    sz = len(board)
    if 0 <= r + by_r < sz and 0 <= c + by_c < sz:
        if board[r + by_r][c + by_c] == ' ':
            return True, (r + by_r, c + by_c)
        else:
            if get_figure_color(board[r + by_r][c + by_c]) != get_figure_color(board[r][c]):
                return False, (r + by_r, c + by_c)
    return False, None


def get_figure_all_moves(board, r, c):
    if board[r][c] in '♛♕':
        return get_all_queen_moves(board, r, c)
    if board[r][c] in '♝♗':
        return get_all_elephant_moves(board, r, c)
    if board[r][c] in '♚♔':
        return get_all_king_moves(board, r, c)
    if board[r][c] in '♜♖':
        return get_all_rook_moves(board, r, c)
    if board[r][c] in '♞♘':
        return get_all_horse_moves(board, r, c)
    if board[r][c] in '♟♙':
        return get_all_pawn_moves(board, r, c)

    return []


def get_all_pawn_moves(board, r, c):
    moves = []
    if get_figure_color(board[r][c]) == 'white':
        _, move = get_move_tik(board, r, c, -1, 0)
        if move is not None:
            moves.append(move)
        if r == 6:
            _, move = get_move_tik(board, r, c, -2, 0)
            if move is not None:
                moves.append(move)

        is_tik, move = get_move_tik(board, r, c, -1, -1)
        if move is not None:
            if not is_tik:
                moves.append(move)
        is_tik, move = get_move_tik(board, r, c, -1, 1)
        if move is not None:
            if not is_tik:
                moves.append(move)

    if get_figure_color(board[r][c]) == 'black':
        _, move = get_move_tik(board, r, c, 1, 0)
        if move is not None:
            moves.append(move)
        if r == 1:
            _, move = get_move_tik(board, r, c, 2, 0)
            if move is not None:
                moves.append(move)

        is_tik, move = get_move_tik(board, r, c, 1, -1)
        if move is not None:
            if not is_tik:
                moves.append(move)
        is_tik, move = get_move_tik(board, r, c, 1, 1)
        if move is not None:
            if not is_tik:
                moves.append(move)

    return moves


def get_all_horse_moves(board, r, c):
    moves = []
    _, move = get_move_tik(board, r, c, -2, -1)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, -2, 1)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, -1, -2)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, 1, -2)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, 2, -1)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, 2, 1)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, 1, 2)
    if move is not None:
        moves.append(move)

    _, move = get_move_tik(board, r, c, -1, 2)
    if move is not None:
        moves.append(move)

    return moves


def get_all_elephant_moves(board, r, c):
    sz = len(board)
    moves = []

    for k in range(1, sz):  # range from figure to NW direction - север запад
        if 0 <= r - k < sz and 0 <= c - k < sz:
            if board[r - k][c - k] == ' ':
                moves.append((r - k, c - k))
            else:
                if get_figure_color(board[r - k][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to SE direction - юг восток
        if 0 <= r + k < sz and 0 <= c + k < sz:
            if board[r + k][c + k] == ' ':
                moves.append((r + k, c + k))
            else:
                if get_figure_color(board[r + k][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c + k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to SW direction - юг запад
        if 0 <= r + k < sz and 0 <= c - k < sz:
            if board[r + k][c - k] == ' ':
                moves.append((r + k, c - k))
            else:
                if get_figure_color(board[r + k][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to NE direction - север восток
        if 0 <= r - k < sz and 0 <= c + k < sz:
            if board[r - k][c + k] == ' ':
                moves.append((r - k, c + k))
            else:
                if get_figure_color(board[r - k][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c + k))
                break
        else:
            break

    return moves


def get_all_queen_moves(board, r, c):
    sz = len(board)
    moves = []
    for k in range(1, sz):  # range N
        if 0 <= r < sz and 0 <= c - k < sz:
            if board[r][c - k] == ' ':
                moves.append((r, c - k))
            else:
                if get_figure_color(board[r][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range S
        if 0 <= r < sz and 0 <= c + k < sz:
            if board[r][c + k] == ' ':
                moves.append((r, c + k))
            else:
                if get_figure_color(board[r][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r, c + k))
                break
        else:
            break

    for k in range(1, sz):  # range W
        if 0 <= r - k < sz and 0 <= c < sz:
            if board[r - k][c] == ' ':
                moves.append((r - k, c))
            else:
                if get_figure_color(board[r - k][c]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c))
                break
        else:
            break

    for k in range(1, sz):  # range E
        if 0 <= r + k < sz and 0 <= c < sz:
            if board[r + k][c] == ' ':
                moves.append((r + k, c))
            else:
                if get_figure_color(board[r + k][c]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to NW direction - север запад
        if 0 <= r - k < sz and 0 <= c - k < sz:
            if board[r - k][c - k] == ' ':
                moves.append((r - k, c - k))
            else:
                if get_figure_color(board[r - k][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to SE direction - юг восток
        if 0 <= r + k < sz and 0 <= c + k < sz:
            if board[r + k][c + k] == ' ':
                moves.append((r + k, c + k))
            else:
                if get_figure_color(board[r + k][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c + k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to SW direction - юг запад
        if 0 <= r + k < sz and 0 <= c - k < sz:
            if board[r + k][c - k] == ' ':
                moves.append((r + k, c - k))
            else:
                if get_figure_color(board[r + k][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range from figure to NE direction - север восток
        if 0 <= r - k < sz and 0 <= c + k < sz:
            if board[r - k][c + k] == ' ':
                moves.append((r - k, c + k))
            else:
                if get_figure_color(board[r - k][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c + k))
                break
        else:
            break

    return moves


def get_all_king_moves(board, r, c):
    sz = len(board)
    moves = []
    k = 1
    # range N
    if 0 <= r < sz and 0 <= c - k < sz:
        if board[r][c - k] == ' ':
            moves.append((r, c - k))
        else:
            if get_figure_color(board[r][c - k]) != get_figure_color(board[r][c]):
                moves.append((r, c - k))

    # range S
    if 0 <= r < sz and 0 <= c + k < sz:
        if board[r][c + k] == ' ':
            moves.append((r, c + k))
        else:
            if get_figure_color(board[r][c + k]) != get_figure_color(board[r][c]):
                moves.append((r, c + k))

    # range W
    if 0 <= r - k < sz and 0 <= c < sz:
        if board[r - k][c] == ' ':
            moves.append((r - k, c))
        else:
            if get_figure_color(board[r - k][c]) != get_figure_color(board[r][c]):
                moves.append((r - k, c))

    # range E
    if 0 <= r + k < sz and 0 <= c < sz:
        if board[r + k][c] == ' ':
            moves.append((r + k, c))
        else:
            if get_figure_color(board[r + k][c]) != get_figure_color(board[r][c]):
                moves.append((r + k, c))

    # range from figure to NW direction - север запад
    if 0 <= r - k < sz and 0 <= c - k < sz:
        if board[r - k][c - k] == ' ':
            moves.append((r - k, c - k))
        else:
            if get_figure_color(board[r - k][c - k]) != get_figure_color(board[r][c]):
                moves.append((r - k, c - k))

    # range from figure to SE direction - юг восток
    if 0 <= r + k < sz and 0 <= c + k < sz:
        if board[r + k][c + k] == ' ':
            moves.append((r + k, c + k))
        else:
            if get_figure_color(board[r + k][c + k]) != get_figure_color(board[r][c]):
                moves.append((r + k, c + k))

    # range from figure to SW direction - юг запад
    if 0 <= r + k < sz and 0 <= c - k < sz:
        if board[r + k][c - k] == ' ':
            moves.append((r + k, c - k))
        else:
            if get_figure_color(board[r + k][c - k]) != get_figure_color(board[r][c]):
                moves.append((r + k, c - k))

    # range from figure to NE direction - север восток
    if 0 <= r - k < sz and 0 <= c + k < sz:
        if board[r - k][c + k] == ' ':
            moves.append((r - k, c + k))
        else:
            if get_figure_color(board[r - k][c + k]) != get_figure_color(board[r][c]):
                moves.append((r - k, c + k))

    moves.append((r, c))
    return moves


def get_all_rook_moves(board, r, c):
    sz = len(board)
    moves = []
    for k in range(1, sz):  # range N
        if 0 <= r < sz and 0 <= c - k < sz:
            if board[r][c - k] == ' ':
                moves.append((r, c - k))
            else:
                if get_figure_color(board[r][c - k]) != get_figure_color(board[r][c]):
                    moves.append((r, c - k))
                break
        else:
            break

    for k in range(1, sz):  # range S
        if 0 <= r < sz and 0 <= c + k < sz:
            if board[r][c + k] == ' ':
                moves.append((r, c + k))
            else:
                if get_figure_color(board[r][c + k]) != get_figure_color(board[r][c]):
                    moves.append((r, c + k))
                break
        else:
            break

    for k in range(1, sz):  # range W
        if 0 <= r - k < sz and 0 <= c < sz:
            if board[r - k][c] == ' ':
                moves.append((r - k, c))
            else:
                if get_figure_color(board[r - k][c]) != get_figure_color(board[r][c]):
                    moves.append((r - k, c))
                break
        else:
            break

    for k in range(1, sz):  # range E
        if 0 <= r + k < sz and 0 <= c < sz:
            if board[r + k][c] == ' ':
                moves.append((r + k, c))
            else:
                if get_figure_color(board[r + k][c]) != get_figure_color(board[r][c]):
                    moves.append((r + k, c))
                break
        else:
            break

    return moves


def clear_console():
    print("\033c\033[3J", end='')


def print_board(board, moves=None):
    if moves is None:
        moves = []

    def is_move(moves, r, c):
        for row, col in moves:
            if (row == r) and (col == c):
                return True
        return False

    def move_style(value, i, j):
        # if (i + j) % 2 == 0:
        #     return '\x1b[0;30;46m' + value + '\x1b[0m'
        return '\x1b[6;30;43m' + value + '\x1b[0m'

    def with_style(value, i, j):
        if (i + j) % 2 == 0:
            return '\33[7m' + value + '\33[0m'
        return '\x1b[6;30;42m' + value + '\x1b[0m'

    sz = 8
    print("   A  B  C  D  E  F  G  H ")
    for i in range(sz):
        print(f"{sz - i} ", end='')
        for j in range(sz):
            if is_move(moves, i, j):
                print(move_style(f" {board[i][j]} ", i + 1, j + 1), end='')
            else:
                print(with_style(f" {board[i][j]} ", i + 1, j + 1), end='')
        print(f" {sz - i}")
    print("   A  B  C  D  E  F  G  H ")


def new_chess_board():
    # return [
    #     ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    #     ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    #     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #     ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    #     ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    # ]
    return [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟', ' ', '♟', '♟', ' ', '♟', '♟', '♟'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '♟', ' ', ' ', '♟', '♕', ' ', ' '],
        [' ', ' ', ' ', '♙', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['♙', '♙', '♙', ' ', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', ' ', '♔', '♗', '♘', '♖'],
    ]


class ChessPositionError(Exception):
    pass


def convert_to_row_col(position: str):
    p = list(position.lower())
    if len(p) != 2:
        raise ChessPositionError(f"Position '{position}' format not correct. ")
    if p[0] not in 'abcdefgh':
        raise ChessPositionError(f"Position '{position}' format not correct. ")
    if not p[1].isnumeric():
        raise ChessPositionError(f"Position '{position}' format not correct. ")
    if int(p[1]) == 0:
        raise ChessPositionError(f"Position '{position}' format not correct. ")

    row = 8 - int(p[1])
    col = 0
    if p[0] == 'a':
        col = 0
    elif p[0] == 'b':
        col = 1
    elif p[0] == 'c':
        col = 2
    elif p[0] == 'd':
        col = 3
    elif p[0] == 'e':
        col = 4
    elif p[0] == 'f':
        col = 5
    elif p[0] == 'g':
        col = 6
    elif p[0] == 'h':
        col = 7
    return row, col


def rearrange_figure(board_, from_p, to_p):
    from_row, from_col = convert_to_row_col(from_p)
    to_row, to_col = convert_to_row_col(to_p)
    figure = board_[from_row][from_col]
    board_[from_row][from_col] = ' '
    board_[to_row][to_col] = figure


board = new_chess_board()
pieces_move = 'white'


def chess_input(text):
    try:
        input_text = input(text)
        input_text = input_text.lower()
        while "  " in input_text:
            input_text = input_text.replace("  ", " ")
        return input_text, True
    except KeyboardInterrupt:
        return "", False


is_next_tik = True
while is_next_tik:
    clear_console()
    print_board(board)

    if pieces_move == 'white':
        print("white pieces move.")
    else:
        print("black pieces move.")

    input_line, is_next_tik = chess_input("chess: ")

    if "new" in input_line:
        board = new_chess_board()

    if "exit" in input_line:
        is_next_tik = False

    if "moves" in input_line:
        moves_command = input_line.split(" ")
        if len(moves_command) != 2:
            print("'moves' command format is not correct.")
            print("Manual: moves <figure position> ")
            print("Example: moves a2")
            _, is_next_tik = chess_input("press enter")
        else:
            try:
                figure_row, figure_col = convert_to_row_col(moves_command[1])
                clear_console()
                print_board(board, get_figure_all_moves(board, figure_row, figure_col))
                _, is_next_tik = chess_input("press enter")
            except ChessPositionError as e:
                print("'moves' command format is not correct.", e)
                print("Manual: moves <figure position> ")
                print("Example: moves a2")
                _, is_next_tik = chess_input("press enter")
    if "go" in input_line:
        go_command = input_line.split(" ")
        if len(go_command) != 3:
            print("'go' command format is not correct.")
            print("Manual: go <from position> <to position>")
            print("Example: go a2 a4")
            _, is_next_tik = chess_input("press enter")
        else:
            try:
                rearrange_figure(board, go_command[1], go_command[2])
                if pieces_move == 'white':
                    pieces_move = 'black'
                else:
                    pieces_move = 'white'
            except ChessPositionError as e:
                print("'go' command format is not correct.", e)
                print("Manual: go <from position> <to position>")
                print("Example: go a2 a4")
                _, is_next_tik = chess_input("press enter")

clear_console()
