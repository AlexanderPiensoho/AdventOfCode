from collections import deque

values = list(range(100))
d = deque(values)
count = 0
with open ("day1-input.txt") as file:
    content = file.read()

    for i in content.splitlines():
        num = int(i[1:])
        direction = i[0:1]
        if direction == "R":
            d.rotate(num)
            rotated_value = d
        else:
            d.rotate(-num)
            rotated_value = d
        if rotated_value[50] == 0:
            count += 1
print(count)
