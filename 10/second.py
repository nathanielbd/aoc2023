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
loop = []
x, y = find_S()
loop.append((x, y))
curr, x, y, came_from = get_next('S', x, y)
loop.append((x, y))
while not curr == 'S':
    curr, x, y, came_from = get_next(curr, x, y, came_from)
    loop.append((x, y))
lhr = set()
rhr = set()
for prev, next in zip(loop[:-1], loop[1:]):
    prev_x, prev_y = prev
    next_x, next_y = next
    dx = next_x - prev_x
    dy = next_y - prev_y
    if dx < 0:
        for ly in range(prev_y, h):
            if ly == prev_y:
                continue
            if (prev_x, ly) in loop:
                break
            else:
                lhr.add((prev_x, ly))
        for ly in range(prev_y, h):
            if ly == next_y:
                continue
            if (next_x, ly) in loop:
                break
            else:
                lhr.add((next_x, ly))
        for ry in range(prev_y, 0, -1):
            if ry == prev_y:
                continue
            if (prev_x, ry) in loop:
                break
            else:
                rhr.add((prev_x, ry))
        for ry in range(prev_y, 0, -1):
            if ry == prev_y:
                continue
            if (next_x, ry) in loop:
                break
            else:
                rhr.add((next_x, ry))
    elif dx > 0:
        for ly in range(prev_y, 0, -1):
            if ly == prev_y:
                continue
            if (prev_x, ly) in loop:
                break
            else:
                lhr.add((prev_x, ly))
        for ly in range(prev_y, 0, -1):
            if ly == prev_y:
                continue
            if (next_x, ly) in loop:
                break
            else:
                lhr.add((next_x, ly))
        for ry in range(prev_y, h):
            if ry == prev_y:
                continue
            if (prev_x, ry) in loop:
                break
            else:
                rhr.add((prev_x, ry))
        for ry in range(prev_y, h):
            if ry == prev_y:
                continue
            if (next_x, ry) in loop:
                break
            else:
                rhr.add((next_x, ry))
    else:
        if dy < 0:
            for lx in range(prev_x, 0, -1):
                if lx == prev_x:
                    continue
                if (lx, prev_y) in loop:
                    break
                else:
                    lhr.add((lx, prev_y))
            for lx in range(prev_x, 0, -1):
                if lx == prev_x:
                    continue
                if (lx, next_y) in loop:
                    break
                else:
                    lhr.add((lx, next_y))
            for rx in range(prev_x, w):
                if rx == prev_x:
                    continue
                if (rx, prev_y) in loop:
                    break
                else:
                    rhr.add((rx, prev_y))
            for rx in range(prev_x, w):
                if rx == prev_x:
                    continue
                if (rx, next_y) in loop:
                    break
                else:
                    rhr.add((rx, next_y))
        else:
            for lx in range(prev_x, w):
                if lx == prev_x:
                    continue
                if (lx, prev_y) in loop:
                    break
                else:
                    lhr.add((lx, prev_y))
            for lx in range(prev_x, w):
                if lx == prev_x:
                    continue
                if (lx, next_y) in loop:
                    break
                else:
                    lhr.add((lx, next_y))
            for rx in range(prev_x, 0, -1):
                if rx == prev_x:
                    continue
                if (rx, prev_y) in loop:
                    break
                else:
                    rhr.add((rx, prev_y))
            for rx in range(prev_x, 0, -1):
                if rx == prev_x:
                    continue
                if (rx, next_y) in loop:
                    break
                else:
                    rhr.add((rx, next_y))
for y, row in enumerate(data):
    curr_row = ''
    for x, sym in enumerate(row):
        if (x, y) in loop:
            curr_row += 'X'
        elif (x, y) in lhr:
            curr_row += 'L'
        elif (x, y) in rhr:
            curr_row += 'R'
        else:
            curr_row += sym
    print(curr_row)
print(f"left: {len(lhr)}")
print(f"right: {len(rhr)}")
# interior = set()
# for x, y, came_from in loop[1:]:
#     if came_from == 'north':
#         in_dir = 
# new_map = []
# for y, row in enumerate(data):
#     curr_row = ''
#     for x, sym in enumerate(row):
#         north = sum([(x, j) in loop for j in range(y, -1, -1)])
#         south = sum([(x, j) in loop for j in range(y, h)])
#         west = sum([(i, y) in loop for i in range(x, -1, -1)])
#         east = sum([(i, y) in loop for i in range(x, w)])
#         if not (x, y) in loop:
#             if not any([dir % 2 != 1 for dir in [north, south, west, east]]):
#                 interior.add((x, y))
#                 curr_row += 'I'
#             else:
#                 curr_row += sym
#         else:
#             curr_row += 'X'
#     print(curr_row)
#     new_map.append(curr_row)
# print()
# interior_count = len(interior)
# def get_surrounding(grid, x, y):
#     surrounding = []
#     if x > 0:
#         if y > 0:
#             surrounding.append(grid[y-1][x-1])
#         if y < h - 1:
#             surrounding.append(grid[y+1][x-1])
#         surrounding.append(grid[y][x-1])
#     if x < w - 1:
#         if y > 0:
#             surrounding.append(grid[y-1][x+1])
#         if y < h - 1:
#             surrounding.append(grid[y+1][x+1])
#         surrounding.append(grid[y][x+1])
#     if y > 0:
#         surrounding.append(grid[y-1][x])
#     if y < h - 1:
#         surrounding.append(grid[y+1][x])
#     return surrounding
# for y, row in enumerate(data):
#     curr_row = ''
#     for x, sym in enumerate(row):
#         if (x, y) in interior:
#             if any([not symbol in ['I', 'X'] for symbol in get_surrounding(new_map, x, y)]):
#                 curr_row += 'O'
#                 interior_count -= 1
#             else:
#                 curr_row += 'I'
#         else:
#             if (x, y) in loop:
#                 curr_row += 'X'
#             else:
#                 curr_row += sym
#     print(curr_row)
# for x, y in interior:
#     if any([not sym in ['I', 'X'] for sym in get_surrounding(new_map, x, y)]):
#         interior_count -= 1
# print(interior_count)