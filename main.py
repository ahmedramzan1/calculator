def calaculator():
    num1 = int(input("Please enter a number: "))
    Operation = str(input("Please enter an Operation. [+/-/*//]: "))
    num2 = int(input("Please enter another number: "))
    if Operation == "+":
        print("The awnser is " ,num1 + num2)
    elif Operation == "-":
        print("The awnser is " ,num1 - num2)
    elif Operation == "*":
        print("The awnser is " ,num1 * num2)
    elif Operation == "/":
        print("The awnser is " ,num1 / num2)
    else:
        print("you have entered an invaild charcter ")

print(calaculator())


