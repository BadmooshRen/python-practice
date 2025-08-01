#write a program to display squared values of a list using map function

nums=[1, 2, 3, 4]
squared=list(map(lambda x:x**2,nums))
print("original list",nums)
print("squared list",squared)

#write a program to display cubed values of a list using map function

nums=[1, 2, 3, 4, 5, 6]
cubed=list(map(lambda x:x**2,nums))
print("original list",nums)
print("cubed list",cubed)

#write a program to convert a list containing lower case letters to upper case using map function

l=['hello','hie','bye','keep']
up=list(map(lambda x:x.upper(),l))
print("original list",l)
print("upper case list",up)

#write a program to convert a list containing upper case letters to lower case using map function

l= ['HELLO', 'HIE', 'BYE', 'KEEP']
low=list(map(lambda x:x.lower(),l))
print("original list",l)
print("lower case list",low)

#write a program to display numbers divisible by 13 using filter function

nums=[13,26,51,-76,-39,101,153]
divisible=list(filter(lambda x:x%13==0,nums))
print("original list",nums)
print("divisible of 13",divisible)

#write a program to display maximum from the list using reduce function

from functools import reduce

nums=[13,26,51,-76,-39,101,153,200,134]
max=reduce(lambda x,y:x if x>y else y,nums)
print("maximum is",max)

#write a program to display minimum from the list using reduce function

from functools import reduce

nums=[13,26,51,-76,-39,101,153,200,134]
min=reduce(lambda x,y:x if x<y else y,nums)
print("minimum is",min)

#write a program to display names which are greater than 3 letters

names=['max','sara','justin','cody','raj','shankar']
newname=list(filter(lambda x:len(x)>3,names))
print("names greater than 5 letters",newname)