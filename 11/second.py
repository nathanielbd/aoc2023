f = open('input.txt', 'r')
data = [row.strip() for row in f]
h = len(data)
w = len(data[0])
whole = ''.join(data)
galaxy_count = sum([1 for row in data for char in row if char == '#'])
def find_occurances(whole:str, substr:str):
    return [i for i in range(0, len(whole)) if whole[i:].startswith(substr)]
galaxy_idxes = find_occurances(whole, '#')
lengths = 0
is_empty_row = dict()
is_empty_col = dict()
for i in range(galaxy_count-1):
    curr = galaxy_idxes[i]
    curr_x = curr % w
    curr_y = curr // w
    print(f"processing galaxy {i+1}/{galaxy_count}")
    for j in range(i+1, galaxy_count):
        print(f"processing pair {i}:{j}")
        to = galaxy_idxes[j]
        to_x = to % w
        to_y = to // w
        dist_x = 0
        dist_y = 0
        if curr_x < to_x:
            for x in range(curr_x, to_x):
                dist_x += 1
                is_empty_col[x] = is_empty_col.get(x, not any([data[y][x] != '.' for y in range(h)]))
                if is_empty_col[x]:
                    dist_x += 999999
        elif to_x < curr_x:
            for x in range(to_x, curr_x):
                dist_x += 1
                is_empty_col[x] = is_empty_col.get(x, not any([data[y][x] != '.' for y in range(h)]))
                if is_empty_col[x]:
                    dist_x += 999999
        if curr_y < to_y:
            for y in range(curr_y, to_y):
                dist_y += 1
                is_empty_row[y] = is_empty_row.get(y, not any([data[y][x] != '.' for x in range(w)]))
                if is_empty_row[y]:
                    dist_y += 999999
        elif to_y < curr_y:
            for y in range(to_y, curr_y):
                dist_y += 1
                is_empty_row[y] = is_empty_row.get(y, not any([data[y][x] != '.' for x in range(w)]))
                if is_empty_row[y]:
                    dist_y += 999999
        print(dist_x, dist_y)
        lengths += dist_x + dist_y
print(lengths)