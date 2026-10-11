number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

print(f"\nThe LCM of {number_1} and {number_2} is : ", end = " ")

lcm = max(number_1, number_2)

while True:
    if lcm / number_1 and lcm / number_2:
        print(lcm)
        break
    else:
        lcm += 1