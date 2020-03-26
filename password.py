import re
n = int(input())

pattern = r"^(.+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^<>]\S+[^<>])<\1$"

for i in range(n):
    text = input()
    result = re.match(pattern, text)
    if result:
        password = result[2] + result[3] + result[4] + result[5]
        print(f"Password: {password}")
    else:
        print("Try another password!")
