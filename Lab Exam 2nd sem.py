text = input("Enter something: ")

letters = 0
numbers = 0
symbols = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        numbers += 1
    else:
        symbols += 1

print(f"Letters =", letters, "Numbers = ", numbers, "Symbols =", symbols)