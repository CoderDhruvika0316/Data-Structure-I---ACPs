quiz_scores = [100, 86, 24, 50, 98, 32, 12, 46, 60, 74, 92]

print("=" * 100)
print("MY QUIZ RESULT SEARCHER")
print("=" * 100)

print(f"List of the Quiz Scores : {quiz_scores}")

print("-" * 82)
print("PART 1 : DIRECT ACCESS") 
print("-" * 82)

first_score = quiz_scores[0]

print(f"First Score : {first_score}")
print("Time Complexity : [O(1)]")
print(f"Theta Notation : [Theta(1)]")
print("Reason : The acess only takes one step.")

print()

print("-" * 82)
print("PART 2 : Linear Search") 
print("-" * 82)

target_score = int(input("Enter a target score from the list:"))
steps = 0
find = False

for score in quiz_scores:
    steps += 1

    if score == target_score:
        found = True
        print(f"Score found : {score}")
        print(f"Steps taken : {steps}")
        break

if find == True:
    print("Score : Found")
    print(f"Steps Taken : {steps}")
else:
    print("Score : Not Found")
    print(f"Steps Taken : {steps}")


print("Best Case : Omega(1)")
print("Average Case : O(number)")
print("Worst Case : O(number)")
print("Reason : The program may need to check many values.")

print()

print("-" * 82)
print("PART 3 : Pair Comparison") 
print("-" * 82)

pairs = 0

for score in quiz_scores:
    for scores in quiz_scores:
        pairs += 1

print(f"Total Pairs Checked : {pairs}")
print("Time Complexity : [O(number ^ 2)]")
print("Reason : An double loop compares every score with another score.")

print("-" * 82)

print()

print("-" * 82)
print("PART 4 : Case Comparison") 
print("-" * 82)

best = 100
average = 32
worst = 92

print(f"Best Target : {best} - Found at the Start")
print(f"Average Target : {average} - Found in the Middle")
print(f"Worst Target : {worst} - Found in the End")

print("-" * 82)

print()

print("=" * 100)
print("ASYMPTOTIC ANALYSIS SUMAMRY")
print("=" * 100)

print("[O(1)] - Direct access is best.")
print("[O(number)] - Linear search grows with the number of scores.")
print("[O(number ^ 2)] - Nested loop search compares one score with another score.")
print("\nOmega(1) - Best case when target is found first.")
print("Theta(1) - Average case when target is found around the middle.")
print("O(1) - Upper/Worst case when target is found near/at the end.")
print("=" * 100)