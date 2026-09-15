# Simple function
def greet(name):
    print("Welcome aboard, " + name + "!")

greet("Kirk")

# Function with return
def double(number):
    return number * 2

result = double(5)
print(result)  # 10

# try / except
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by 0!"

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: Division by 0!
