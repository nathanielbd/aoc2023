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
seeds = [(int(fseed), int(fseed)+int(sseed)-1) for fseed, sseed in zip(seeds[::2], seeds[1::2])]
maps = [list(map(lambda mapj: mapj.split(' '), mapi[2:])) for mapi in maps]
final_intervals = []
def get_overlap(int1, int2):
    start = max(int1[0], int2[0])
    end = min(int1[1], int2[1])
    return (start, end) if start <= end else None
def outer_join(interval, cut):
    if cut[0] == interval[0]:
        if cut[1] == interval[1]:
            return []
        else:
            return [(cut[1]+1, interval[1])]
    else:
        if cut[1] == interval[1]:
            return [(interval[0], cut[0]-1)]
        else:
            return [(interval[0], cut[0]-1), (cut[1]+1, interval[1])]
for i in range(len(maps)):
    new_seeds = []
    for seed_interval in seeds:
        unprocessed = [seed_interval]
        for interval in maps[i]:
            interval = list(map(int, interval))
            dest_start, source_start, length = interval
            map_interval = (source_start, source_start+length-1)
            new_unprocessed = []
            for span in unprocessed:
                overlap = get_overlap(span, map_interval)
                if overlap:
                    oj = outer_join(span, overlap)
                    offset = dest_start-source_start
                    new_seeds += [(overlap[0]+offset, overlap[1]+offset)]
                    new_unprocessed += oj
                else:
                    new_unprocessed += [span]
            unprocessed = new_unprocessed
        new_seeds += unprocessed
    seeds = new_seeds
print(min([start for start, end in seeds]))