f = open('input.txt', 'r')
data = [row.strip() for row in f]
def ddt(values):
    return [next-prev for prev, next in zip(values[:-1], values[1:])]
ans = 0
for row in data:
    values = []
    values.append([int(value) for value in row.split(' ')])
    while any([not value == 0 for value in values[-1]]):
        values.append(ddt(values[-1]))
    forecast = sum([history[-1] for history in values])
    ans += forecast
print(ans)