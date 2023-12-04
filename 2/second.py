f = open('input.txt', 'r')
ans = 0
from operator import mul
from functools import reduce
for row in f:
    idx = int(row.strip().split(':')[0].split(' ')[1])
    moves = row.strip().split(':')[1].split(';')
    poss = dict()
    for move in moves:
        actions = move.split(',')
        for action in actions:
            _, num, color = action.split(' ')
            num = int(num)
            poss[color] = max(poss.get(color, 0), num)
    ans += reduce(mul, poss.values(), 1)
print(ans)