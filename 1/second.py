f = open('input.txt', 'r')
ans = 0
num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5', 
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
def convert_str(s: str):
    indexes = {key:s.find(key) for key in num_dict if s.find(key) > -1}
    while len(indexes) > 0:
        to_replace = min(indexes, key=indexes.get)
        s = s.replace(to_replace, num_dict[to_replace])
        indexes = {key:s.find(key) for key in num_dict if s.find(key) > -1}
    return s
def build_nums(s: str):
    to_build = ''
    nums = []
    for char in s:
        to_build += char
        if char in num_dict.values():
            nums.append(char)
            to_build = ''
            continue
        for key in num_dict:
            if key in to_build:
                nums.append(num_dict[key])
                to_build = ''
                break
    return nums
def get_digits(s: str):
    digits = []
    for idx, char in enumerate(s):
        if char.isdigit():
            digits.append(char)
        for val, word in enumerate(num_dict.keys()):
            if s[idx:].startswith(word):
                digits.append(str(val+1))
    return digits
for row in f:
    # row = convert_str(row)
    # chars = list(row.strip())
    # nums = [char for char in chars if char.isnumeric()]
    # nums = build_nums(row.strip())
    nums = get_digits(row.strip())
    to_add = int(nums[0] + nums[-1])
    assert to_add >= 11 and to_add <= 99
    ans += to_add
print(ans)