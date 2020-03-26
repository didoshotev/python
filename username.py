username = input()

while True:
    command = input()
    if command == "Sign up":
        break
    elif command == "Case lower":
        username = username.lower()
        print(username)
    elif command == "Case upper":
        username = username.upper()
        print(username)
    elif "Reverse" in command:
        command = command.split(" ")
        start = int(command[1]) - 1
        end = int(command[2])
        if 0 <= start <= len(username) and 0 <= end <= len(username):
            part = username[end:start:-1]
            print(part)
    elif "Cut" in command:
        command = command.split(" ")
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif "Replace" in command:
        command = command.split(" ")
        char = command[1]
        username = username.replace(char, "*")
        print(username)
    elif "Check" in command:
        command = command.split(" ")
        char = command[1]
        if char not in username:
            print(f"Your username must contain {char}.")
        else:
            print("Valid")
