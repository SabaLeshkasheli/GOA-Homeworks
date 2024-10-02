#შეამოწმე მომხმარებლის შემოტანილი რიცხვი თუ არის 5-ის ან 10-ის ჯერადი.

num = int(input("Please enter a number : "))

if num % 5 == 0 or num % 10 == 0:
    print("Your number can be devided by 10 or 5")

else:
    print("Your number cant be devided by 10 or 5")    