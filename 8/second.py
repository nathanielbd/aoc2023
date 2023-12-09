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
starts = [start for start in nodes if start.endswith('A')]
n = len(lrs)
def get_steps(curr):
    i = 0
    while not curr.endswith('Z'):
        move = lrs[i % n]
        if move == 'L':
            curr = nodes[curr][0]
        else:
            curr = nodes[curr][1]
        i += 1
    return i
steps = [get_steps(start) for start in starts]
import math
print(math.lcm(*steps))
# currs = [start for start in nodes if start.endswith('A')]
# n = len(lrs)
# i = 0
# while any([not curr.endswith('Z') for curr in currs]):
#     move = lrs[i % n]
#     if move == 'L':
#         currs = [nodes[curr][0] for curr in currs]
#     else:
#         currs = [nodes[curr][1] for curr in currs]
#     i += 1
# print(i)