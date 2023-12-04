f = open('input.txt', 'r')
data = [row.strip() for row in f]
copies = dict()
for idx, row in enumerate(data):
    left = row.split('|')[0]
    winning = [int(num) for num in left.split(':')[1].strip().split(' ') if num != '']
    right = row.split('|')[1]
    yours = [int(num) for num in right.strip().split(' ') if num != '']
    common = set(winning).intersection(set(yours))
    copy_num = len(common)
    copies[idx+1] = copies.get(idx+1, 1)
    for i in range(1, copy_num+1):
        copies[idx+1+i] = copies.get(idx+1+i, 1) + copies.get(idx+1, 1)
ans = sum(copies.values())
print(ans)