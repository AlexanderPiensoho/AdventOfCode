import re

ID_counter=0
with open("first-input.txt") as file:
    content = file.read()

structured = re.split(",", content)

for i in structured:
    split_again = re.split("-", i)
    first_number = int(split_again[0])
    second_number = int(split_again[1])

    for number in range(first_number, second_number+1, 1): 
        if re.match(r"(.+)\1+$", str(number)):
            ID_counter += int(number)
         
print(ID_counter)
