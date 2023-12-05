f = open('input.txt', 'r')
data = [row.strip() for row in f]
def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g
maps = list(group(data, ''))
seeds = maps.pop(0)[0].split(': ')[1].split(' ')
maps = [list(map(lambda mapj: mapj.split(' '), mapi[2:])) for mapi in maps]
locs = dict()
for seed in seeds:
    seed = int(seed)
    dest = seed
    for i in range(len(maps)):
        for interval in maps[i]:
            interval = list(map(int, interval))
            dest_start, source_start, length = interval
            if source_start <= dest < source_start+length:
                diff = dest - source_start
                dest = dest_start + diff
                break
    locs[seed] = dest
print(min(locs.values()))