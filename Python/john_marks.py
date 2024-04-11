total = 0
count = 0

with open("john_marks.txt", "r") as file:

    for line in file:
        mark = float(line.strip())  # strip() removes the newline character at the end
        total += mark
        count += 1

average = round(total/count, 2) #round allows us to round a number
print("Average :", average)