num=int(input("enter a number "))
rev=0
temp=num
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if rev==num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")