f = open('input.txt', 'r')
data = [row.strip() for row in f]
times = [int(val) for val in data[0].split(':')[1].split(' ') if val != '']
distances = [int(val) for val in data[1].split(':')[1].split(' ') if val != '']
races = {time:distance for time, distance in zip(times, distances)}
ans = 1
# for race in races:
for time, distance in zip(times, distances):
    pos_distances = [i*(time-i) for i in range(time)]
    push_times = [i for i, pd in enumerate(pos_distances) if pd > distance]
    ways = len(push_times)
    ans *= ways
print(ans)