def get_integer_input():
    number = int(input("Enter an integer: "))
    return number

def check_even_odd(number):    
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

number = get_integer_input()
result = check_even_odd(number)
print(result)
