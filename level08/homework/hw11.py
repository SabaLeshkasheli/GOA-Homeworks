#დაწერე პროგრამა, რომელიც ამოწმებს, თუ string იწყება ასოთი "A" ან ასოთი "B".

text = input("Please wrtite a text : ")

if text.startswith("A") or text.startswith("B"):
    print("Your text stars with a or b")
else:
    print("Your text doesn't start with a or b")
