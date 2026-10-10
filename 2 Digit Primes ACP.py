print("=======================================================================")
print("2 Digit Primes Finder")
print("=======================================================================")
print("In this program, you will get to know all the 2 digit Prime Numbers.\n")
print("The 2 Digit Prime Numbers are : ")



def SoE(number):
    prime = [True for i in range(number + 1)]
    small = 2

    while (small * small <= number):
        if (prime[small] == True):
            for i in range(small * small, number + 1, small):
                prime[i] = False

        small += 1

    for small in range(10, number + 1):
        if prime[small]:
            print(small)

SoE(100)

print("======================================================================")