#შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.

num1 = int(input("Please enter a number : "))
num2 = int(input("Please enter a second number : "))

print(num1 > num2)

if num1 % 10 or num2 % 10:
    print("Your number can be devided by 10")
else:
    print("Your number cant be devided by 10")