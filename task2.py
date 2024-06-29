print("= = = = Calculator = = = =")
# function which add two numbers.
def add(num1,num2 ):
    return num1+num2
# function which subtract two numbers.
def subtract(num1,num2):
    return num1-num2
# function which multiply two numbers
def multiply(num1,num2):
    return num1*num2
# function which divide two numbers
def divide(num1,num2):
    return num1/num2
# function which give remainder when divide two numbers
def remainder(num1,num2):
    return num1%num2


print("Please select operation-\n"
      "1.Add\n"
      "2.Subtract\n"
      "3.Multiply\n"
      "4.Divide\n"
      "5.Modulo\n")
n = int(input("Enter your choice from (1-5):"))
num1 = int(input("Enter your first number"))
num2 = int(input("enter your second number"))
if n == 1:
    print("Sum of two no. is:", num1+num2)
elif n == 2:
    print("Subtraction of two no. is:", num1-num2)
elif n == 3:
    print("Multiplication of two no. is:", num1*num2)
elif n == 4:
    print("Division of two no. is:", num1/num2)
elif n==5:
    print("Modulo of two no. is:",num1%num2)
else:
    print("Invalid choice")
