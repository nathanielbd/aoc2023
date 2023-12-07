f = open('input.txt', 'r')
data = [row.strip() for row in f]
hands = [row.split(' ')[0] for row in data]
bids = [row.split(' ')[1] for row in data]
def compare_card_counters(cntr1:tuple[str, int], cntr2:tuple[str, int]):
    card1, cnt1 = cntr1
    card2, cnt2 = cntr2
    if cnt1 < cnt2:
        return -1
    elif cnt1 > cnt2:
        return 1
    else:
        map_val = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
        if card1.isnumeric():
            card1 = int(card1)
        else:
            card1 = map_val[card1]
        if card2.isnumeric():
            card2 = int(card2)
        else:
            card2 = map_val[card2]
        if card1 < card2:
            return -1
        elif card2 == card2:
            return 0
        else:
            return 1
from functools import cmp_to_key
from collections import Counter
def compare_hands(hand1:str, hand2:str):
    map_val = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    counts1 = Counter(hand1.replace('J', ''))
    counts2 = Counter(hand2.replace('J', ''))
    if len(counts1) == 0:
        to_replace1 = 'A'
    else:
        to_replace1, _ = sorted(counts1.most_common(), key=cmp_to_key(compare_card_counters))[-1]
    if len(counts2) == 0:
        to_replace2 = 'A'
    else:
        to_replace2, _ = sorted(counts2.most_common(), key=cmp_to_key(compare_card_counters))[-1]
    counts1 = Counter(hand1.replace('J', to_replace1))
    counts2 = Counter(hand2.replace('J', to_replace2))
    uniques1 = len(counts1)
    uniques2 = len(counts2)
    if uniques1 > uniques2:
        return -1
    elif uniques1 < uniques2:
        return 1
    else:
        if uniques1 == 2:
            (_, _), (_, one_sec) = counts1.most_common(2)
            (_, _), (_, two_sec) = counts2.most_common(2)
            if one_sec > two_sec:
                return -1
            elif one_sec < two_sec:
                return 1
        elif uniques1 == 3:
            _, one_top = counts1.most_common(1)[0]
            _, two_top = counts2.most_common(1)[0]
            if one_top > two_top:
                return 1
            elif one_top < two_top:
                return -1
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
                return 1
            elif first < second:
                return -1
        print('what')
        return 0
ranked_hands = sorted(hands, key=cmp_to_key(compare_hands))
ans = 0
for hand, bid in zip(hands, bids):
    rank = ranked_hands.index(hand)+1
    ans += int(bid)*rank
print(ans)