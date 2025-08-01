#program to make a simple calculator

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. exponential")
num1=float(input("enter first number "))
n=int(input("enter number which corresponds to the operation you want to perform "))
num2=float(input("enter second number "))
if n==1:
    print("addition of",num1,"and",num2,"is",num1+num2)
elif n==2:
    print("subtraction of",num1,"and",num2,"is",num1-num2)
elif n==3:
    print("multiplication of",num1,"and",num2,"is",num1*num2)
elif n==4:
    if num2==0:
        print("can't divide by zero")
    else:
        print("division of",num1,"and",num2,"is",num1/num2)
elif n==5:
    print("exponential of",num1,"raised to",num2,"is",num1**num2)
else:
    print("enter valid number")
