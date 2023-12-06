import sys

numbers_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def isNumber(string, index):
    tmp = string[index:index+3]
    try:
        return numbers_dict[tmp]
    except:
        pass

    tmp = string[index:index+4]
    try:
        return numbers_dict[tmp]
    except:
        pass

    tmp = string[index:index+5]
    try:
        return numbers_dict[tmp]
    except:
        pass

    return 0

def processLine(string):
    global sum

    size = len(string)
    
    first = -1
    last = 0
    index = 0

    while index < size:
        if string[index] in numbers:
            if first == -1:
                first = int(string[index])
            last = int(string[index])

        tmp = isNumber(string, index)
        if tmp:
            if first == -1:
                first = tmp
            last = tmp

        index += 1

    sum += 10*first + last

def main():
    input_path = sys.argv[1]

    global sum
    sum = 0

    with open(input_path, "r") as f:
        for line in f:
            processLine(line)

    print(sum)


if __name__ == "__main__":
    main()