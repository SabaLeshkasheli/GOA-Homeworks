#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი.

num = int(input("Please enter a number : "))

if num % 3 or num %2:
    print("Your number can be devided by 3 or is an even number")
else:
    print("Your number is invalid")