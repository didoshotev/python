import re
n = int(input())

pattern = r"^(!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\])$"

for i in range(n):
    text = input()
    obj = {}
    result = re.match(pattern, text)
    if result:
        for letter in result[3]:
            if not obj:
                obj[result[2]] = [str(ord(letter))]
            else:
                obj[result[2]].append(str(ord(letter)))
        for key, value in obj.items():
            print(f"{key}: {' '.join(value)}")

    else:
        print("The message is invalid")
