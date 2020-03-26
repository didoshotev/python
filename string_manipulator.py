text = input()

while True:
    command = input().split(" ")
    if command[0] == "Done":
        break
    elif command[0] == "Change":
        text = text.replace(command[1], command[2])
        print(text)
    elif command[0] == "Includes":
        if command[1] in text:
            print(True)
        else:
            print(False)
    elif command[0] == "End":
        end = command[1]
        idx = len(text) - len(end)
        if text[idx:] == end:
            print(True)
        else:
            print(False)
    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        idx = text.index(char)
        print(idx)
    elif command[0] == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        end_index = start_index + length
        text = text[start_index:end_index]
        print(text)