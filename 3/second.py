f = open('input.txt', 'r')
grid = [row.strip() for row in f]
h = len(grid)
w = len(grid[0])
num = ''
neighboring_symbol = False
ans = 0
nums = {}
for i in range(h):
    gears = set()
    for j in range(w):
        char = grid[i][j]
        if char.isnumeric():
            num += char
        else:
            if len(num) > 0 and neighboring_symbol:
                for gear in gears:
                    nums[gear] = nums.get(gear, []) + [int(num)]
            num = ''
            neighboring_symbol = False
            gears = set()
        if len(num) > 0 and not neighboring_symbol:
            for x in range(max(j-1, 0), min(j+2, w)):
                for y in range(max(i-1, 0), min(i+2, h)):
                    symbol_cand = grid[y][x]
                    if not symbol_cand.isnumeric() and symbol_cand != '.':
                        neighboring_symbol = True
                        if symbol_cand == '*':
                            gears.add((x, y))
        if j == w-1:
            if len(num) > 0 and neighboring_symbol:
                for gear in gears:
                    nums[gear] = nums.get(gear, []) + [int(num)]
            num = ''
            neighboring_symbol = False
    num = ''
for gear, num_list in nums.items():
    if len(num_list) == 2:
        ans += num_list[0] * num_list[1]
print(ans)