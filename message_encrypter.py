import re


pattern = r"([*|@])([A-Z][a-z]{2,})\1:\s((\[([A-Za-z])\]\|){3})$"
n = int(input())

for i in range(n):
    message = []
    text = input()
    result = re.findall(pattern, text)
    if re.search(pattern, text):
        result = list(result[0])
        txt = result[2]
        tag = result[1]
        for j in txt:
            if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
                message.append(str(ord(j)))
        print(f"{tag}: {' '.join(message)}")
    else:
        print("Valid message not found!")
