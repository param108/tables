import random
import sys
import time

random.seed()

seen = {}
wrong = 0
start = time.time()
while len(seen) < 400:
    randomA = random.randint(0,20)
    randomB = random.randint(0,20)
    qn = str(randomA)+" X "+str(randomB) + " = "
    if qn not in seen:
        seen[qn] = str(randomA*randomB)
        value = input(qn)
        if value == "q":
            print("You got "+str(wrong)+" wrong of " + str(len(seen)))
            print("in "+ str(time.time() - start)+ " seconds")
            sys.exit()
        while value != seen[qn]:
            wrong += 1
            print ("wrong answer. Try again")
            value = input(qn)
            if value == "q":
                print("You got "+str(wrong)+" wrong of " + str(len(seen)))
                print("in "+ str(time.time() - start)+ " seconds")
                sys.exit()
        print("Correct")
print("You got "+str(wrong)+" wrong of " + str(len(seen)))
print("in "+ str(time.time() - start)+ " seconds")


