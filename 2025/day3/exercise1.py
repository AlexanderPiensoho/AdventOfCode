def biggest_pair(list):
    best_result = 0
    for i in range(len(list) -1):
        idx_num = list[i]
        rem_list = list[i+1:]
        next_biggest_number = max(rem_list)

        current_pair = idx_num * 10 + next_biggest_number
        if current_pair > best_result:
            best_result = current_pair

    return best_result


def main():
    with open("input.txt") as file:
        content = file.read().split()
    
    battery=[] 
    for i in content:
        int_list = [int(item) for item in i]
        result=biggest_pair(int_list)
        battery.append(result)
    battery_sum = sum(battery)
    print(battery_sum)

if  __name__ == "__main__":
    main()
