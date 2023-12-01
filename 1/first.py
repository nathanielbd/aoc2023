f = open('input.txt', 'r')
ans = 0
for row in f:
    chars = list(row.strip())
    nums = [char for char in chars if char.isnumeric()]
    ans += int(nums[0] + nums[-1])
print(ans)