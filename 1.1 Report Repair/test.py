import re
pass_file = open(r"D:\Users\grace\PycharmProjects\aoc\2.1 Password Philosophy\test", "r")

pass_list = [entry.replace("\n", "") for entry in pass_file.readlines()]


elements = [re.split(r"[-: ]\s*",x) for x in pass_list]
positions = [(int(first), int(second)) for first, second, _, _ in elements]
password = [pword for _, _, _, pword  in elements]
letter = [char for _, _, char, _ in elements]

n = 0
for pword in password:
  for count, item in enumerate(pword, 1):
    print(count)
    print(positions[n][0])

if positions[n][0] == count:
  print("yes")

print(count)
print(positions[n][0])
