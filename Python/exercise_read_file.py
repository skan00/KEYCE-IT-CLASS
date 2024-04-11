total = 0

with open("numbers.txt", "r") as file:

    for line in file:
        number = float(line.strip())  # strip() removes the newline character at the end
        total += number

 
print("Sum :", total)