with open("01.pi_digits.txt", "r") as file_object:
    lines = file_object.readlines() #store the file lines in a list

for line in lines:
    print(line.rstrip())