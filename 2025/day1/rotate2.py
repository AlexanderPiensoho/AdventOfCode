count = 0
base_value = 50
min_value = 0

with open("day1-input.txt") as file:
    content = file.read()

    for i in content.splitlines():
        
        direction = i[0]
        num = int(i[1:])
        
        for j in range(num):
            if direction == "R":
                base_value += 1 

            else:
                base_value -= 1

        
            if base_value % 100 == min_value:
                count += 1

print(count)
print(base_value)
