# Q1. Check if a number is positive, negative, or zero.

n = int(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")


# Q2. Check whether a number is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Q3. Find the greater of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")


# Q4. Find the greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)


# Q5. Check if a person is eligible to vote (age >= 18).

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Q6. Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# Q7. Check if a character is a vowel or consonant.

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# Q8. Check whether a number is divisible by 5 and 11.

n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")


# Q9. Check if a number is a multiple of both 3 and 7.

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# Q10. Assign grades based on marks.

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 0:
    print("Grade F")
else:
    print("Invalid marks")


# Q11. Check if a character is uppercase or lowercase.

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")


# Q12. Find whether the entered alphabet is a vowel using if-elif.

ch = input("Enter an alphabet: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")


# Q13. Check if three sides can form a triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


# Q14. Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")


# Q15. Find the largest among four numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number:", a)
elif b >= a and b >= c and b >= d:
    print("Largest number:", b)
elif c >= a and c >= b and c >= d:
    print("Largest number:", c)
else:
    print("Largest number:", d)


# Q16. Check whether a number is a three-digit number.

n = int(input("Enter a number: "))

if 100 <= abs(n) <= 999:
    print("Three digit number")
else:
    print("Not a three digit number")


# Q17. Calculate electricity bill using slab rates.
# First 100 units = Rs. 5 per unit
# Next 100 units = Rs. 7 per unit
# Above 200 units = Rs. 10 per unit

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity bill: Rs.", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity bill: Rs.", bill)


# Q18. Calculate income tax based on income slabs.
# Up to Rs. 250000 = No tax
# Rs. 250001 to Rs. 500000 = 5%
# Above Rs. 500000 = 10% on excess amount

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
    print("Income tax: Rs.", tax)
elif income <= 500000:
    tax = (income - 250000) * 0.05
    print("Income tax: Rs.", tax)
else:
    tax = 12500 + (income - 500000) * 0.10
    print("Income tax: Rs.", tax)


# Q19. Check if a student passes (minimum 35 marks in each subject).

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student is Pass")
else:
    print("Student is Fail")


# Q20. Find whether a number is within a given range.

n = int(input("Enter a number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low <= n <= high:
    print("Number is within range")
else:
    print("Number is outside range")


# Q21. Build a simple calculator using if-elif-else.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Addition:", a + b)
elif op == '-':
    print("Subtraction:", a - b)
elif op == '*':
    print("Multiplication:", a * b)
elif op == '/':
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division by zero not possible")
else:
    print("Invalid operator")


# Q22. Check if a year is a century leap year.

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
else:
    print("Not a century leap year")


# Q23. Determine the season based on the month number.

month = int(input("Enter month number (1-12): "))

if month in [3, 4, 5]:
    print("Summer season")
elif month in [6, 7, 8, 9]:
    print("Rainy season")
elif month in [10, 11]:
    print("Autumn season")
elif month in [12, 1, 2]:
    print("Winter season")
else:
    print("Invalid month")


# Q24. Find the number of days in a month.

month = int(input("Enter month number: "))
year = int(input("Enter year: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month")


# Q25. Check whether a password meets minimum conditions.

password = input("Enter your password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Valid password")
else:
    print("Password must have at least 8 characters and one digit")


# Q26. Determine ticket price based on age.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 12:
    print("Ticket price: Rs. 100")
elif age < 60:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 150")


# Q27. Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount < 1000:
    discount = 0
    print("No discount")
elif amount < 5000:
    discount = amount * 0.10
    print("Discount: Rs.", discount)
else:
    discount = amount * 0.20
    print("Discount: Rs.", discount)

if amount >= 0:
    print("Final amount: Rs.", amount - discount)


# Q28. Check if a person is eligible for a driving license.

age = int(input("Enter your age: "))
eyesight = input("Is eyesight normal? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


# Q29. Create a login system with username and password validation.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")


# Q30. Create a menu-driven program using if-elif-else.

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition:", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction:", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication:", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division by zero not possible")

elif choice == 5:
    print("Exit")

else:
    print("Invalid choice")