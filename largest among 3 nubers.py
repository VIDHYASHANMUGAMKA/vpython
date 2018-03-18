num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if(num1>=num2)and(num1>=num3):
    largest=num1
    print("num1 is the largest number")
elif(num2>=num1)and(num2>=num3):
    largest=num2
    print("num2 is the largest number")
else:
    largest=num3
    print("num3 is the largest number ")
