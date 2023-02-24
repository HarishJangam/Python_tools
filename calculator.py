
# def add(x,y) :
#     print(x+y)


# def substract(x,y):
#     print(x-y)


# def division(x,y):
#     print(x/y)


# def multiplication(x,y):
#     print(x*y)




# x=int(input("enter val"))
# y=int(input("enter val"))
# print("""
#       enter ur option 
#       1.add
#       2.substract
#       3.division
#       4.multiplication""")
# option=int(input("option :"))

# if(option==1):
#     add(x,y)
# elif(option==2):
#     substract(x,y)
# elif(option==3):
#     division(x,y)
# elif(option==4):
#     multiplication(x,y)
# else:
#     print("Invalid option")


# define functions for addition, subtraction, multiplication, and division
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# display menu of options to user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# take input from the user
choice = input("Enter choice (1/2/3/4): ")

# take input for numbers to operate on
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform calculation based on user's choice
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")
