
print("Task 1 : comand line Calculator")

Number_1 = int(input("enter your first number: "))
Number_2 = int(input("enter your seacond number: "))

operation = str(input("enter OPERATION FROM + - * /  : "))


if (operation== "+"):
    print ("the addition of" , Number_1 , "and", Number_2 , "is " , Number_1 + Number_2)
elif (operation== "-"):
    print ("the subtraction of" , Number_1 , "and", Number_2 , "is " , Number_1 - Number_2)
elif (operation== "*"):
    print ("the multiplication of" , Number_1 , "and", Number_2 , "is " , Number_1 * Number_2)
elif (operation== "/"):
    try:
        print("The division of", Number_1, "and", Number_2, "is", Number_1 / Number_2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! please enter another value.")
else :
    print(" choose operator between + - * and / ")

