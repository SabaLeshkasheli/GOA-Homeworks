#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი.
num = int(input("Please enter a number : "))

if num < 50 and num % 10:
    print("Your number is less than 50 and can be devided by 10")
else:
    print("Your number is more than 50")