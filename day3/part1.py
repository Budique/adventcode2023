import sys

non_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_with_0 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_without_0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Returns if there is a symbol adjacent to the number
def check_number(start_index, end_index, line_number):
    global lines

    checklist = {"up": True,
                 "down": True,
                 "left": True,
                 "right": True}

    if line_number == 0:
        checklist["up"] = False
    if line_number == len(lines) - 1:
        checklist["down"] = False
    if start_index == 0:
        checklist["left"] = False
    if end_index == len(lines[line_number]) - 2:
        checklist["right"] = False

    # Returns true if there is a symbol up the number
    if checklist["up"]:
        for i in range(start_index, end_index + 1):
            if lines[line_number - 1][i] not in non_symbols:
                return True
            
        if checklist["left"]:
            if lines[line_number - 1][start_index - 1] not in non_symbols:
                return True
            
        if checklist["right"]:
            if lines[line_number - 1][end_index + 1] not in non_symbols:
                return True

    # Returns true if there is a symbol below the number
    if checklist["down"]:
        for i in range(start_index, end_index + 1):
            if lines[line_number + 1][i] not in non_symbols:
                return True
            
        if checklist["left"]:
            if lines[line_number + 1][start_index - 1] not in non_symbols:
                return True
            
        if checklist["right"]:
            if lines[line_number + 1][end_index + 1] not in non_symbols:
                return True
    
    # Returns true if there is a symbol right next to the number
    if checklist["left"]:
        if lines[line_number][start_index - 1] not in non_symbols:
            return True

    # Returns true if there is a symbol left next to the number    
    if checklist["right"]:
        if lines[line_number][end_index + 1] not in non_symbols:
            return True


    return False

def main():
    input_path = sys.argv[1]

    sum = 0

    with open(input_path, "r") as f:
        global lines
        lines = f.readlines()
        
        for line, line_number in zip(lines, range(len(lines))):
            i = 0
            while i < len(line):
                if line[i] in numbers_with_0:
                    start_index = i
                    while line[i] in numbers_with_0:
                        i += 1
                    end_index = i
                    if check_number(start_index, end_index - 1, line_number):
                        sum += int(line[start_index : end_index])
                i += 1

        
    
    print(sum)



if __name__ == "__main__":
    main()