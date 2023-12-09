f = open('input.txt', 'r')
data = [row.strip() for row in f]
lrs = data[0]
node_list = data[2:]
nodes = dict()
for node in node_list:
    curr, tup = node.split(' = ')
    l = tup[1:4]
    r = tup[6:9]
    nodes[curr] = (l, r)
curr = 'AAA'
n = len(lrs)
i = 0
while curr != 'ZZZ':
    move = lrs[i % n]
    if move == 'L':
        curr = nodes[curr][0]
    else:
        curr = nodes[curr][1]
    i += 1
print(i)