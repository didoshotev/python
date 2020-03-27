text = input()

while True:
    command = input().split(" ")
    if command[0] == "End":
        break
    elif command[0] == "Translate":
        [char, replacement] = command[1], command[2]
        text = text.replace(char, replacement)
        print(text)
    elif command[0] == "Includes":
        if command[1] in text:
            print(True)
        else:
            print(False)
    elif command[0] == "Start":
        if text.startswith(command[1]):
            print(True)
        else:
            print(False)
    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif command[0] == "FindIndex":
        last = text.rfind(command[1])
        print(last)
    elif command[0] == "Remove":
        start = int(command[1])
        count = int(command[2])
        end = start + count
        old = text[:start]
        new = text[end:]
        text = old + new
        print(text)

