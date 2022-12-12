num1 = int (input("enter first number: "))
num2 = int (input("enter second number: "))

print("enter which operation would you like to perform?")
ch = input ("Enter any of these char for specific operation +,-,*,/: ")

Result = 0
if ch == '+':
    result = num1 + num2
elif ch == '.':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2

else:
    print ("input character is not recognized!")

print (num1, ch , num2, "=", result)

