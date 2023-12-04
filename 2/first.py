f = open('input.txt', 'r')
ans = 0
for row in f:
    idx = int(row.strip().split(':')[0].split(' ')[1])
    moves = row.strip().split(':')[1].split(';')
    to_add = True
    for move in moves:
        actions = move.split(',')
        for action in actions:
            _, num, color = action.split(' ')
            num = int(num)
            if num > 12 and color == 'red':
                to_add = False
            elif num > 13 and color == 'green':
                to_add = False
            elif num > 14 and color == 'blue':
                to_add = False
    if to_add:
        ans += idx
print(ans)