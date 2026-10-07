seats = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122]

print("=================================================================================================")
print("MY TRAIN SEAT FINDER")
print("=================================================================================================")
print(f"List of Seats : {seats}")

target = int(input("Enter a target seat from the list of seats:"))

def binary_search(seat, target):
    low = 0
    high = len(seat) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        print(f"Middle Seat : {seat[mid]}")

        if seats[mid] == target:
            return mid, steps

        elif target < seats[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1, steps

index, steps = binary_search(seats, target)

print()

print("----------------------------------------------------------------------")
print("BINARY SEARCH RESULT")
print("----------------------------------------------------------------------")

if index != -1:
    print(f"Result : Target seat {target} found at position {index}")

else:
    print("Result : Seat not found.")

print(f"Steps Taken : {steps}")
print("Time Complexity : [O(log number)]")
print("Space Complexity : [O(1)]")

def recursive_binary_search(seat, target, low, high):
    if low > high:
        return - 1

    mid = (low + high ) // 2
    print(f"Recursive Check : {seat[mid]}")

    if seat[mid] == target:
        return mid
    elif target < seat[mid]:
        return recursive_binary_search(seat, target, low, mid - 1)
    else:
        return recursive_binary_search(seat, target, mid + 1, high)

recur_index = recursive_binary_search(seats, target, 0, len(seats) - 1)

print()

print("----------------------------------------------------------------------")
print("RECURSIVE BINARY SEARCH RESULT")
print("----------------------------------------------------------------------")

if recur_index != -1:
    print(f"Result : Target Seat {target} found at {recur_index}")

else:
    print("Result : Seat not found.")

print(f"Steps Taken : {steps}")
print("Time Complexity : [O(log number)]")
print("Space Complexity : [O(log number)]")
print("=================================================================================================")

print()

print("=================================================================================================")
print("COMPLEXITY LADDER")
print("=================================================================================================")
print("O(1) - Directly checking one fixed seat")
print("O(log number) - Binary search by cutting the list into two halves")
print("O(number) - Checking every seat one by one")
print("O(number ^ 2) - Comapring every seat with another seat")
print("=================================================================================================")

print()

print("=================================================================================================")
print("SUMMARY")
print("=================================================================================================")
print("Binary Search is faster than checking evry seat one by one.")
print("Binary Search only works when the list of seats is ordered.")
print("Recursive Binary Search also uses O(log number) time.")
print("However, recursion uses extra space in the call stack.")
print("=================================================================================================")