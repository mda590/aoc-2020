import sys

# PART 1
with open("input.txt", "r") as f:
    data = f.read().splitlines()
    for num1 in data:
        num1 = int(num1)
        for num2 in data:
            num2 = int(num2)
            calc = num1 + num2
            if calc == 2020:
                print("Part 1:", num1*num2)

# PART 2
with open("input.txt", "r") as f:
    data = f.read().splitlines()
    for num1 in data:
        num1 = int(num1)
        for num2 in data:
            num2 = int(num2)
            for num3 in data:
                num3 = int(num3)
                calc = num1 + num2 + num3
                if calc == 2020:
                    print("Part 2:", num1*num2*num3)
