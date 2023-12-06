import sys
import re

non_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_with_0 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_without_0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Returns the list of numbers adjacent to the gear symbol ("*")
def check_gear(gear_index, line_index):
    global lines
    result = []

    # Check left
    if gear_index != 0:
        if lines[line_index][gear_index-1] in numbers:
            start_index = gear_index - 1
            end_index = gear_index
            while start_index >= 0 and lines[line_index][start_index] in numbers:
                start_index -= 1
            result.append(int(lines[line_index][start_index+1 : end_index]))

    # Check right
    if gear_index != len(lines[line_index]) - 1:
        if lines[line_index][gear_index+1] in numbers:
            start_index = gear_index + 1
            end_index = gear_index + 1
            while end_index < len(lines[line_index]) and lines[line_index][end_index] in numbers:
                end_index += 1
            result.append(int(lines[line_index][start_index : end_index]))

    # Check up
    tmp_result = {"upper left": "", "up": "", "upper right": ""}
    if line_index != 0:
        if gear_index != 0:
            if lines[line_index-1][gear_index-1] in numbers:
                start_index = gear_index - 1
                end_index = gear_index
                while start_index >= 0 and lines[line_index-1][start_index] in numbers:
                    start_index -= 1
                tmp_result["upper left"] = lines[line_index-1][start_index+1 : end_index]
        
        if gear_index != len(lines[line_index-1]) -1:
            if lines[line_index-1][gear_index+1] in numbers:
                start_index = gear_index + 1
                end_index = gear_index + 1
                while end_index < len(lines[line_index-1]) and lines[line_index-1][end_index] in numbers:
                    end_index += 1
                tmp_result["upper right"] = lines[line_index-1][start_index : end_index]
        
        if lines[line_index-1][gear_index] in numbers:
            tmp_result["up"] = lines[line_index-1][gear_index]
        
        # Return empty list if there is a number on the upper side but there are already two numbers in the result list
        if (tmp_result["upper left"] or tmp_result["up"] or tmp_result["upper right"]) and len(result) == 2:
            return []

        if tmp_result["up"]:
            result.append(int(tmp_result["upper left"] + tmp_result["up"] + tmp_result["upper right"]))
        else:
            for value in tmp_result.values():
                if value != "":
                    result.append(int(value))

    # Check down
    tmp_result = {"bottom left": "", "down": "", "bottom right": ""}
    if line_index != len(lines)-1:
        if gear_index != 0:
            if lines[line_index+1][gear_index-1] in numbers:
                start_index = gear_index - 1
                end_index = gear_index
                while start_index >= 0 and lines[line_index+1][start_index] in numbers:
                    start_index -= 1
                tmp_result["bottom left"] = lines[line_index+1][start_index+1 : end_index]

        if gear_index != len(lines[line_index+1]) - 1:
            if lines[line_index+1][gear_index+1] in numbers:
                start_index = gear_index + 1
                end_index = gear_index + 1
                while end_index < len(lines[line_index+1]) and lines[line_index+1][end_index] in numbers:
                    end_index += 1
                tmp_result["bottom right"] = lines[line_index+1][start_index : end_index]
        
        if lines[line_index+1][gear_index] in numbers:
            tmp_result["down"] = lines[line_index+1][gear_index]
        
        # Return empty list if there is a number on the bottom side but there are already two numbers in the result list
        if (tmp_result["bottom left"] or tmp_result["down"] or tmp_result["bottom right"]) and len(result) == 2:
            return []
        
        if tmp_result["down"]:
            result.append(int(tmp_result["bottom left"] + tmp_result["down"] + tmp_result["bottom right"]))
        else:
            for value in tmp_result.values():
                if value != "":
                    result.append(int(value))

    return result
    

def main():
    input_path = sys.argv[1]

    sum = 0

    with open(input_path, "r") as f:
        global lines
        lines = f.readlines()
        
        for line, line_index in zip(lines, range(len(lines))):
            for i in range(len(line)):
                if line[i] == "*":
                    gear_numbers = check_gear(i, line_index)
                    if len(gear_numbers) == 2:
                        sum += gear_numbers[0] * gear_numbers[1]
    
    print(sum)



if __name__ == "__main__":
    main()