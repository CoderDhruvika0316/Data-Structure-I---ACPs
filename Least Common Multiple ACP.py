largest = int(input("Enter the first number:"))
smallest = int(input("Enter the second number:"))

print(f"\nThe LCM of {largest} and {smallest} is : ", end = " ")

lcm = max(largest, smallest)

while True:
    if lcm % largest == 0 and lcm % smallest == 0:
        print(lcm)
        break
    else:
        lcm += 1