name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")


num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter a diffrent number: "))

# the three math calculations

multiplication = num1 * num2
division = num1 / num2
addition = num1 + num2

#displaying the results of the math equations

print(f"The result of {num1} times {num2} is: {multiplication:.2f}")
print(f"The result of {num1} divided by {num2} is: {division:.2f}")
print(f"The result of {num1} plus {num2} is: {addition:.2f}")

#compare the numbers

if num1 > num2:
    print("Number 1 is larger than Number 2")
elif num1 < num2:
    print("Number 1 is smaller than Number 2")
else:
    print("Number 1 and Number 2 are equal")

    #display student information

print(f"Name: {name}")
print(f"Student ID: {student_id}")
