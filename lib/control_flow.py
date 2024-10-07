#!/usr/bin/env python3

def admin_login(username, password):
    if ((username == "admin") or (username == "ADMIN")):
        if (password == "12345"):
            return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    if (temperature <= 40):
        return "It's brisk out there!"
    elif (temperature < 65):
        return "It's a little chilly out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    multiple_of_3 = (num % 3 == 0)
    multiple_of_5 = (num % 5 == 0)

    if (multiple_of_3):
        if (multiple_of_5):
            return "FizzBuzz"
        return "Fizz"
    elif (multiple_of_5):
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2
    elif (operation == "*"):
        return num1 * num2 
    elif (operation == "/"):
        return num1 / num2
    print('Invalid operation!')
    return None