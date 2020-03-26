import re
n = int(input())

pattern = r"^\|(|[A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#$"

for i in range(n):
    text = input()
    result = re.match(pattern, text)
    if result:
        [name, title] = result[1], result[2]
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armour: {len(title)}")
    else:
        print("Access denied!")


