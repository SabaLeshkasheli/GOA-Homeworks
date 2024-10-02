#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.
num = int(input("Please enter a number : "))

if num < 0 or num % 2:
    print("your number is either a negative number or an even number : ")
else:
    print("Your number is not a negative number or isn't even")