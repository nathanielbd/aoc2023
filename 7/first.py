f = open('input.txt', 'r')
data = [row.strip() for row in f]
hands = [row.split(' ')[0] for row in data]
bids = [row.split(' ')[1] for row in data]
from collections import Counter
def compare_hands(hand1:str, hand2:str):
    counts1 = Counter(hand1)
    counts2 = Counter(hand2)
    uniques1 = len(counts1)
    uniques2 = len(counts2)
    if uniques1 > uniques2:
        # return False, hand1, hand2
        return -1
    elif uniques1 < uniques2:
        # return True, hand1, hand2
        return 1
    else:
        if uniques1 == 2:
            (_, _), (_, one_sec) = counts1.most_common(2)
            (_, _), (_, two_sec) = counts2.most_common(2)
            if one_sec > two_sec:
                # return False, hand1, hand2
                return -1
            elif one_sec < two_sec:
                # return True, hand1, hand2
                return 1
        elif uniques1 == 3:
            _, one_top = counts1.most_common(1)[0]
            _, two_top = counts2.most_common(1)[0]
            if one_top > two_top:
                # return True, hand1, hand2
                return 1
            elif one_top < two_top:
                # return False, hand1, hand2
                return -1
        map_val = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        for i in range(5):
            first = hand1[i]
            if first.isnumeric():
                first = int(first)
            else:
                first = map_val[first]
            second = hand2[i]
            if second.isnumeric():
                second = int(second)
            else:
                second = map_val[second]
            if first > second:
                # return True, hand1, hand2
                return 1
            elif first < second:
                # return False, hand1, hand2
                return -1
        print('what')
        # return None, None, None
        return 0
# def bubble_sort(hands: list[str]):
#     n = len(hands)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(1, n):
#             res, hand1, hand2 = compare_hands(hands[i-1], hands[i])
#             if not res:
#                 # print(f'swapped {hand1} and {hand2}')
#                 hands[i-1], hands[i] = hand2, hand1
#                 swapped = True
#                 # print(hands)
#     return hands
# ranked_hands = bubble_sort(hands)[::-1]
# print(ranked_hands)
# print(hands)
# ranked_hands = hands.sort(key=compare_hands)
from functools import cmp_to_key
ranked_hands = sorted(hands, key=cmp_to_key(compare_hands))
ans = 0
for hand, bid in zip(hands, bids):
    rank = ranked_hands.index(hand)+1
    ans += int(bid)*rank
print(ans)