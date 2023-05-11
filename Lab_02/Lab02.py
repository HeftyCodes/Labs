#Kenny Almanza
#Date: 02-03-23
#File:Lab02.py
# _   _       __ _         
#| | | | ___ / _| |_ _   _ 
#| |_| |/ _ \ |_| __| | | |
#|  _  |  __/  _| |_| |_| |
#|_| |_|\___|_|  \__|\__, |
#                    |___/ 
def is_prime(number):
    if number <= 1:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    else: return True

def factorial_for(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def factorial_while(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
        return result 

def largest_prime(number):
    for i in range(number -1,0,-1):
        if is_prime(i):
            return i

while True:
    user_input = input("Enter a Number or 'Done' to exit:")
    if user_input == 'Done':
        break
    try:
        number = int(user_input)
    except ValueError :
        print("Invalid input. Enter a Number.")
        continue

    if is_prime(number):
        print(f"{number} Is a Prime Number.")
    else:
        print(f"{number} Is Not a Prime Number")
        largest = largest_prime(number)
        if largest:
         print(f"The Largest Prime Number Less than {number} is {largest}.")
    if number < 20:
        factorial = factorial_for(number)
    print(f"The Factorial of {number} Using For Loop Is {factorial}.")
factorial = factorial_while(number)
print(f"The Factorial of {number} Using While Loop is {factorial}.")