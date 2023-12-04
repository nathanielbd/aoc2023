import math
f = open('input.txt', 'r')
ans = 0
for row in f:
    row = row.strip()
    left = row.split('|')[0]
    winning = [int(num) for num in left.split(':')[1].strip().split(' ') if num != '']
    right = row.split('|')[1]
    yours = [int(num) for num in right.strip().split(' ') if num != '']
    common = set(winning).intersection(set(yours))
    to_add = math.floor(2**(len(common)-1))
    ans += to_add
print(ans)