import random
import time

OPERATORS = ["+", "-", "*"]
OPERAND1 = 3
OPERAND2 = 4
TOTALQUE = 5

def generateProblem():
    left = random.randint(OPERAND1,OPERAND2)
    right = random.randint(OPERAND1,OPERAND2)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

# expr, answer = generateProblem()
# print(expr, answer)

worng = 0
input("Press enter to start!")
print("-------------------------------")

startTime = time.time()

for i in range(TOTALQUE):
    expr, answer = generateProblem()
    while True:
        guess = input("Problem " + str(i+1) + ":" + expr + " = ")
        if guess == str(answer):
            break
        worng += 1

endTime = time.time()
totalTime = endTime - startTime

print("----------------------------------")
print("Nice work! You finished in", totalTime, "seconds!")