from tile import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8 Queen")

board = [Tile(i, SCREEN_WIDTH, SCREEN_HEIGHT) for i in range(64)]
rows_index = []


def find_empty_rows():
    global rows_index
    is_row_empty = True
    for row in range(8):
        for col in range(8):
            if not get_tile_by_position((row, col)).is_empty:
                is_row_empty = False
        if is_row_empty:
            rows_index.append(row)
        is_row_empty = True


def get_tile_by_position(pos):
    row, col = pos
    return board[row * 8 + col]


def check_board():
    for tile in board:
        if not tile.is_empty:
            if not check_validity(tile):
                return False
    return True


def is_pos_in_range(pos):
    row, col = pos
    return 0 <= row <= 7 and 0 <= col <= 7


def number_of_queens():
    num = 0
    for tile in board:
        if not tile.is_empty:
            num += 1
    return num


def check_validity(tile):
    row, col = tile.pos
    for i in range(8):
        if not get_tile_by_position((row, i)).is_empty and i != col:
            return False
        if not get_tile_by_position((i, col)).is_empty and i != row:
            return False
    temp_row, temp_col = row, col
    while True:
        temp_row -= 1
        temp_col -= 1
        if not is_pos_in_range((temp_row, temp_col)):
            break
        if not get_tile_by_position((temp_row, temp_col)).is_empty:
            return False
    temp_row, temp_col = row, col
    while True:
        temp_row += 1
        temp_col += 1
        if not is_pos_in_range((temp_row, temp_col)):
            break
        if not get_tile_by_position((temp_row, temp_col)).is_empty:
            return False
    temp_row, temp_col = row, col
    while True:
        temp_row += 1
        temp_col -= 1
        if not is_pos_in_range((temp_row, temp_col)):
            break
        if not get_tile_by_position((temp_row, temp_col)).is_empty:
            return False
    temp_row, temp_col = row, col
    while True:
        temp_row -= 1
        temp_col += 1
        if not is_pos_in_range((temp_row, temp_col)):
            break
        if not get_tile_by_position((temp_row, temp_col)).is_empty:
            return False
    return True


def solve(index=0):
    if number_of_queens() == 8:
        return True

    for col in range(8):
        tile = get_tile_by_position((rows_index[index], col))
        tile.put_queen()
        vld = check_board()
        tile.remove_queen()
        if vld:
            tile.put_queen()

            if solve(index+1):
                return True

            tile.remove_queen()
    return False


def handle_click(pos):
    x, y = pos
    col = int(x // (SCREEN_WIDTH/8))
    row = int(y // (SCREEN_HEIGHT/8))
    get_tile_by_position((row, col)).put_queen()


def redraw():
    for tile in board:
        tile.draw(win)


running = True
is_solved = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_solved:
                handle_click(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                find_empty_rows()
                is_solvable = solve()
                is_solved = True
                if not is_solvable:
                    print("Invalid setup")
    redraw()
    pygame.display.update()

pygame.quit()
