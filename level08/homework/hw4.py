#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.
num = int(input("Please enter a number : "))

if num % 2 == 0 and num > 100:
    print("Your number is more than 100 and even")

    