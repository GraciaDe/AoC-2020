import re
pass_file = open("Passwords", "r")

pass_list = [entry.replace("\n", "") for entry in pass_file.readlines()]


elements = [re.split(r"[-: ]\s*",x) for x in pass_list]
positions = [(int(first), int(second)) for first, second, _, _ in elements]
password = [pword for _, _, _, pword  in elements]
letter = [char for _, _, char, _ in elements]

valid = []

for pword, pos, char in zip(password, positions, letter):
    i = 0
    for index, item in enumerate(pword, 1):
        for x in pos:
            if index == x:
                if item == char:
                    i+=1
    if i == 1:
        valid.append(pword)

#print(f"Element list - {elements}")
#print(f"Position list - {positions}")
#print(f"Password list - {password}")
#print(f"Letter list - {letter}")
#print(f"Valid list - {valid}")
print(f"Valid count: {len(valid)}")

