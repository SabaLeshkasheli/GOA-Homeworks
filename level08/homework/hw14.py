#მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა  20-ის ჯერადი და დადებითი.
num = int(input("Please enter a number : "))

if num % 20 and num > 0:
    print("Your number can be devided by 20 and is a positive number")
else:
    print("your number cant be devided by 20 and isnt a postive number")