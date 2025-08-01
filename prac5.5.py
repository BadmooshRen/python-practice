#program to check if a number is prime or not

num=int(input("enter a number "))
flag=False
if num==1 or num==0:
    print(num, "is not prime")    
elif num>1:
    for i in range(2,num):
        if (num % i) == 0:
            flag=True
            break
    if flag:
        print(num, "is not prime")
    else:
        print(num, "is prime")