f = open('test.txt', 'r')
data = [row.strip() for row in f]
time = int(''.join([val for val in data[0].split(':')[1].split(' ') if val != '']))
distance = int(''.join([val for val in data[1].split(':')[1].split(' ') if val != '']))
pos_distances = [i*(time-i) for i in range(time)]
push_times = [i for i, pd in enumerate(pos_distances) if pd > distance]
ways = len(push_times)
print(ways)