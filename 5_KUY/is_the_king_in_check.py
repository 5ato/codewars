"""
https://www.codewars.com/kata/5e28ae347036fa001a504bbe
"""


def is_inside(x: int, y: int) -> bool:
    if (0 <= x <= 7) and (0 <= y <= 7):
        return True
    return False


def horiz_vert(figure: dict, chessboard: list[list[str]], f: str) -> bool:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x = figure[f][0] + dx[i]
        y = figure[f][1] + dy[i]
        while is_inside(x, y):
            if '♔' == chessboard[y][x]:
                return True
            elif chessboard[y][x] != ' ':
                break
            x += dx[i]
            y += dy[i]
    return False


def diagonal_attack(figure: dict, chessboard: list[list[str]], f: str) -> bool:
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    for i in range(4):
        x, y = figure[f][0] + dx[i], figure[f][1] + dy[i]
        while is_inside(x, y):
            if '♔' == chessboard[y][x]:
                return True
            elif chessboard[y][x] != ' ':
                break
            x += dx[i]
            y += dy[i]
    return False



def pawn_attack(figure: dict, chessboard: list[list[str]]) -> bool:
    x1, y1 = figure['♟'][0]-1, figure['♟'][1]+1
    x2, y2 = figure['♟'][0]+1, figure['♟'][1]+1
    if is_inside(x1, y1) and is_inside(x2, y2):
        if '♔' in (chessboard[y1][x1],
                    chessboard[y2][x2]):
            return True
    return False


def knight_attack(figure: dict, chessboard: list[list[str]]) -> bool:
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, 1, -1]
    for i in range(8):
        x = dx[i] + figure['♞'][0]
        y = dy[i] + figure['♞'][1]
        if is_inside(x, y):
            if '♔' in chessboard[y][x]:
                return True
    return False



def king_is_in_check(chessboard : list[list[str]]) -> bool:
    figures = []
    danger = False
    for row in chessboard:
        x = 0
        for piece in row:
            if piece != ' ': figures.append({piece: (x, chessboard.index(row))})
            x += 1
    for figure in figures:
        if '♟' in figure:
            danger = pawn_attack(figure, chessboard)
            if danger:
                return danger
        if '♞' in figure:
            danger = knight_attack(figure, chessboard)
            if danger:
                return danger
        if '♝' in figure:
            danger = diagonal_attack(figure, chessboard, '♝')
            if danger:
                return danger
        if '♜' in figure:
            danger = horiz_vert(figure, chessboard, '♜')
            if danger:
                return danger
        if '♛' in figure:
            danger = diagonal_attack(figure, chessboard, '♛')
            if danger:
                return danger
            danger = horiz_vert(figure, chessboard, '♛')
            if danger:
                return danger
    return danger


def main():
    print(king_is_in_check([
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♟',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♜','♛',' ',' ',' ',' ','♛',' '],
            [' ',' ',' ',' ',' ','♔',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','♟',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]))
    
if __name__ == '__main__':
    main()
