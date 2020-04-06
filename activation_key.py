text = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {text}")
        break
    elif command[0] == "Contains":
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip" and command[1] == "Upper":
        start = int(command[2])
        end = int(command[3])
        new_word = text[start:end].upper()
        new_start = text[:start]
        new_end = text[end:]
        text = new_start + new_word + new_end
        print(text)
    elif command[0] == "Flip" and command[1] == "Lower":
        start = int(command[2])
        end = int(command[3])
        new_word = text[start:end].lower()
        new_start = text[:start]
        new_end = text[end:]
        text = new_start + new_word + new_end
        print(text)
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        text = text[:start] + text[end:]
        print(text)

