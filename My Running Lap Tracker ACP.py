number = int(input("\nEnter the number of laps:"))

print("\n", "=" * 70)
print("MY RUNNING LAP TRACKER")
print("=" * 70)

total = number * (number + 1) // 2
steps = 1

print("-" * 50)
print("First Solution : Formula (Constant)")
print("-" * 50)
print(f"Total Running Lap Points : {total}")
print(f"Steps : {steps}")
print("Time Complexity : O(1)")
print("Space Complexity : O(1)\n")

total = 0
steps = 0

for laps in range(1, number + 1):
    total += laps
    steps += 1

print("-" * 50)
print("Second Solution : Single Loop (Linear)")
print("-" * 50)
print(f"Total Running Lap Points : {total}")
print(f"Steps : {steps}")
print("Time Complexity : O(number)")
print("Space Complexity : O(1)\n")


total = 0
steps = 0

for laps in range(number):
    for count in range(1, laps + 1):
        total += 1
        steps += 1

print("-" * 50)
print("Third Solution : Double Loop (Quadratic)")
print("-" * 50)
print(f"Total Running Lap Points : {total}")
print(f"Steps : {steps}")
print("Time Complexity : O(number ^ 2)")
print("Space Complexity : O(1)")

print("=" * 70)

print("\n", "=" * 100)
print("ALGORITHMS EFFICIENCY COMPARISON")
print("=" * 100)

print("Formula : Works fastest because it has one calculation")
print("Single Loop : Works average because it repeats once per each lap")
print("Double Loop : Work worst because it repats twice per each lap (It uses a loop inside another loop)\n")
print("Best Solution -> Formula : Works fastest and is the most efficient")

print("=" * 100)