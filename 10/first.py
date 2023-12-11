f = open('input.txt', 'r')
data = [row.strip() for row in f]
h = len(data)
w = len(data[0])
dist = 0
def get_neighbors(tile, x, y):
    neighbors = []
    if tile == '|':
        if y > 0:
            neighbors.append((data[y-1][x], x, y-1, 'north'))
        if y < h - 1:
            neighbors.append((data[y+1][x], x, y+1, 'south'))
    elif tile == '-':
        if x > 0:
            neighbors.append((data[y][x-1], x-1, y, 'west'))
        if x < w - 1:
            neighbors.append((data[y][x+1], x+1, y, 'east'))
    elif tile == 'L':
        if y > 0:
            neighbors.append((data[y-1][x], x, y-1, 'north'))
        if x < w - 1:
            neighbors.append((data[y][x+1], x+1, y, 'east'))
    elif tile == 'J':
        if y > 0:
            neighbors.append((data[y-1][x], x, y-1, 'north'))
        if x > 0:
            neighbors.append((data[y][x-1], x-1, y, 'west'))
    elif tile == '7':
        if y < h - 1:
            neighbors.append((data[y+1][x], x, y+1, 'south'))
        if x > 0:
            neighbors.append((data[y][x-1], x-1, y, 'west'))
    elif tile == 'F':
        if y < h - 1:
            neighbors.append((data[y+1][x], x, y+1, 'south'))
        if x < w - 1:
            neighbors.append((data[y][x+1], x+1, y, 'east'))
    return neighbors
def infer_start_neighbors(x, y):
    neighbors = []
    if y > 0:
        north = data[y-1][x]
        if north in ['|', '7', 'F']:
            neighbors.append((north, x, y-1, 'north'))
    if y < h - 1:
        south = data[y+1][x]
        if south in ['|', 'L', 'J']:
            neighbors.append((south, x, y+1, 'south'))
    if x > 0:
        west = data[y][x-1]
        if west in ['-', 'L', 'F']:
            neighbors.append((west, x-1, y, 'west'))
    if x < w - 1:
        east = data[y][x+1]
        if east in ['-', 'J', '7']:
            neighbors.append((east, x+1, y, 'east'))
    return neighbors
def get_next(curr, x, y, came_from=None):
    global dist
    dist += 1
    if curr == 'S':
        neighbors = infer_start_neighbors(x, y)
    else:
        neighbors = get_neighbors(curr, x, y)
    if not came_from:
        next, next_x, next_y, dir = neighbors[0]
        if x < next_x:
            if next == '-':
                next_came_from = 'west'
            elif next == '7':
                next_came_from = 'north'
            elif next == 'J':
                next_came_from = 'south'
        elif x > next_x:
            if next == '-':
                next_came_from = 'east'
            elif next == 'L':
                next_came_from = 'south'
            elif next == 'F':
                next_came_from = 'north'
        elif y < next_y:
            if next == '|':
                next_came_from = 'north'
            elif next == 'L':
                next_came_from = 'west'
            elif next == 'J':
                next_came_from = 'east'
        else:
            if next == '|':
                next_came_from = 'south'
            elif next == '7':
                next_came_from = 'east'
            elif next == 'F':
                next_came_from = 'west'
        return next, next_x, next_y, next_came_from
    else:
        if came_from == 'west':
            _, _, _, dir0 = neighbors[0]
            _, _, _, dir1 = neighbors[1]
            if dir0 == 'east':
                next, next_x, next_y, _ = neighbors[0]
            else:
                next, next_x, next_y, _ = neighbors[1]
            if next == '-':
                next_came_from = 'west'
            elif next == '7':
                next_came_from = 'north'
            elif next == 'J':
                next_came_from = 'south'
            else:
                next_came_from = 'start'
            return next, next_x, next_y, next_came_from
        elif came_from == 'north':
            _, _, _, dir0 = neighbors[0]
            _, _, _, dir1 = neighbors[1]
            if dir0 == 'south':
                next, next_x, next_y, _ = neighbors[0]
            else:
                next, next_x, next_y, _ = neighbors[1]
            if next == '|':
                next_came_from = 'north'
            elif next == 'L':
                next_came_from = 'west'
            elif next == 'J':
                next_came_from = 'east'
            else:
                next_came_from = 'start'
            return next, next_x, next_y, next_came_from
        elif came_from == 'east':
            _, _, _, dir0 = neighbors[0]
            _, _, _, dir1 = neighbors[1]
            if dir0 == 'west':
                next, next_x, next_y, _ = neighbors[0]
            else:
                next, next_x, next_y, _ = neighbors[1]
            if next == '-':
                next_came_from = 'east'
            elif next == 'L':
                next_came_from = 'south'
            elif next == 'F':
                next_came_from = 'north'
            else:
                next_came_from = 'start'
            return next, next_x, next_y, next_came_from
        else:
            _, _, _, dir0 = neighbors[0]
            _, _, _, dir1 = neighbors[1]
            if dir0 == 'north':
                next, next_x, next_y, _ = neighbors[0]
            else:
                next, next_x, next_y, _ = neighbors[1]
            if next == '|':
                next_came_from = 'south'
            elif next == '7':
                next_came_from = 'east'
            elif next == 'F':
                next_came_from = 'west'
            else:
                next_came_from = 'start'
            return next, next_x, next_y, next_came_from
def find_S():
    for y, row in enumerate(data):
        x = row.find('S')
        if not x == -1:
            return x, y
    print('no S found')
x, y = find_S()
curr, x, y, came_from = get_next('S', x, y)
while not curr == 'S':
    curr, x, y, came_from = get_next(curr, x, y, came_from)
print(dist//2)