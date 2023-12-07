import sys
import functools

def custom_cmp(card):
    order = "J23456789TQKA"
    return [order.index(char) for char in card]

def read_input(path):
    result = {}
    with open(path, 'r') as file:
        for line in file:
            tmp = line.split(" ")
            result[tmp[0]] = int(tmp[1].split("\n")[0])
    return result

def process_cards(cards):
    tmp = {}
    jokers = 0
    for card in cards:
        if card == "J":
            jokers += 1
            continue
        if not card in tmp:
            tmp[card] = 1
        else:
            tmp[card] += 1
    
    tmp = [value for value in tmp.values()]
    tmp.sort()
    leng = len(tmp)

    if jokers == 5:
        return 6
    
    tmp[-1] += jokers

    if leng == 1:
        return 6
    if leng == 2:
        if tmp[-1] == 4:
            return 5
        return 4
    if leng == 3:
        return tmp[-1]
    if leng == 4:
        return 1
    return 0
        

def main():
    input_path = sys.argv[1]
    hands = read_input(input_path)

    types = [[] for i in range(7)]

    for hand in hands:
        types[process_cards(hand)].append(hand)
    
    result = 0
    rank = 1
    for i in range(7):
        types[i] = sorted(types[i], key=custom_cmp)
        
        for hand in types[i]:
            result += hands[hand] * rank
            rank += 1

    print(result)

if __name__ == "__main__":
    main()