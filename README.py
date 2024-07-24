#we wil make calculator

num1=int(input("enter first no."))
num2=int(input("enter 2nd number:"))
print("enter 1 addition")
print("enter 2.substraction")
print("enter 3.multiplication")
print("enter 4.division")
ch=int(input("enter your choice:"))
if (ch==1):
    c=num1+num2
    print("aswer is",c)
elif (ch==2):
    c=num1-num2
    print("answer is",c)
elif (ch==3):
    c=num1*num2
    print("answer is",c)
elif (ch==4):
    c=num1/num2
    print("answer is",c)
else:
    print("wrong choice")
