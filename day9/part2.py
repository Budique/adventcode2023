import sys

def process_line(arr):
    # True if arr is not full of 0's
    if any(arr):
        tmp = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        return arr[-1] + process_line(tmp)
    else:
        return 0

def main():
    input_path = sys.argv[1]
    
    result = 0
    with open(input_path, "r") as file:
        for line in file:
            arr = [int(num) for num in line.strip("\n").split()][::-1]
            result += process_line(arr)

    print(result)

if __name__ == "__main__":
    main()