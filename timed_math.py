import random
import time

operators = ['+','-','*']
min_number = 2
max_number = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_number,max_number)
    right = random.randint(min_number,max_number)
    operator = random.choice(operators)
    

    expression = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expression)

    return expression,answer

wrong = 0
input("WELCOME TO TIMING MATH CHALLENGE!!!")
input("Press enter to start the challenge!")
print("------------------------------------")
print("\n")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
       guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
       if guess == str(answer):
           break
       wrong+=1

end_time = time.time()
total_time = end_time - start_time

print("------------------------------------")
print("\n")
print("Nice work! You finished in", total_time, "seconds")
