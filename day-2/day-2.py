import re

pattern = r"(\d*)\-(\d*)\s(.)\:\s(.+)"

with open("input.txt", "r") as f:
    data = f.read().splitlines()

    valid_passwords_p1 = 0
    valid_passwords_p2 = 0
    for pwd in data:
        match = re.match(pattern, pwd)
        if match:
            min_match = int(match.group(1))
            max_match = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            counter = password.count(letter)
            if counter >= min_match and counter <= max_match:
                valid_passwords_p1+=1

            if password[min_match-1] == letter and password[max_match-1] != letter \
                or password[min_match-1] != letter and password[max_match-1] == letter:
                valid_passwords_p2+=1

    print("Part 1:", valid_passwords_p1)
    print("Part 2:", valid_passwords_p2)
