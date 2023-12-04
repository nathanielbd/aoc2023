f = open('input.txt', 'r')
grid = [row.strip() for row in f]
h = len(grid)
w = len(grid[0])
num = ''
neighboring_symbol = False
ans = 0
for i in range(h):
    for j in range(w):
        char = grid[i][j]
        if char.isnumeric():
            num += char
        else:
            if len(num) > 0 and neighboring_symbol:
                ans += int(num)
                print(num)
            num = ''
            neighboring_symbol = False
        if len(num) > 0 and not neighboring_symbol:
            for x in range(max(j-1, 0), min(j+2, w)):
                for y in range(max(i-1, 0), min(i+2, h)):
                    if not grid[y][x].isnumeric() and grid[y][x] != '.':
                        neighboring_symbol = True
        if j == w-1:
            if len(num) > 0 and neighboring_symbol:
                ans += int(num)
                print(num)
            num = ''
            neighboring_symbol = False
    num = ''
print(ans)

# grid = []
# objs = []
# nums = []
# for row in f:
#     grid.append(row.strip())
#     objs.append([val for val in row.strip().split('.') if val != ''])
#     num_row = []
#     curr_num = ''
#     for char in row.strip():
#         if char.isnumeric():
#             curr_num += char
#         elif curr_num != '':
#             num_row.append(curr_num)
#             curr_num = ''
#         else:
#             continue
#     nums.append(num_row)
# def is_adjacent(num_x, num_y, num_len, symbol_x, symbol_y):
#     locs = [(x, num_y) for x in range(num_x, num_x + num_len)]
#     ret = False
#     for x, y in locs:
#         x_dis = abs(x - symbol_x)
#         y_dis = abs(y - symbol_y)
#         if x_dis == 1 and y_dis == 1:
#             ret = True
#         elif x_dis == 0 and y_dis == 1:
#             ret = True
#         elif y_dis == 0 and x_dis == 1:
#             ret = True
#         # elif x_dis == 0 and y_dis == 0:
#         #     # if we have a negative number
#         #     # return False
#         #     return True
#     return ret
# ans = 0
# def process_obj(obj: str, i: int, j: int):
#     global ans
#     # print(f"num: {obj} at ({j}, {i})")
#     to_add = False
#     for y in range(max(i-1, 0), min(i+2, len(grid))):
#         row = grid[y]
#         for x in range(len(row)):
#             if not row[x].isnumeric() \
#                 and row[x] != '.':
#                     # print(f"adjacent to {row[x]} at ({x}, {y})?")
#                     if is_adjacent(j, i, len(obj), x, y):
#                         to_add = True
#                         # print('yes')
#                         break
#                     # print('no')
#         if to_add:
#             break
#     if to_add:
#         val = int(obj)
#         if val < 0:
#             val *= -1
#         ans += val
#         print(val)
# for idx, row in enumerate(grid):
#     j = 0
#     for num in nums[idx]:
#         j = row.find(num, j)
#         # if j > 0:
#         #     if row[j-1] == '-':
#         #         print('negative number!')
#         #         j -= 1
#         #         num = f"-{num}"
#         assert j != -1
#         process_obj(num, idx, j)
# print(ans)
