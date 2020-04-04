skill = input()

while True:
    command = input().split(" ")
    if command[0] == "For" and command[1] == "Azeroth":
        break
    elif command[0] == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif command[0] == "DefensiveStance":
        skill = skill.lower()
        print(skill)
    elif command[0] == "Dispel":
        [index, letter] = command[1], command[2]
        index = int(index)
        if 0 <= index <= len(skill):
            skill = list(skill)
            skill[index] = letter
            skill = "".join(skill)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command[1] == "Change" and command[0] == "Target":
        [first_substring, second_substring] = command[2], command[3]
        skill = skill.replace(first_substring, second_substring)
        print(skill)
    elif command[1] == "Remove" and command[0] == "Target":
        substring = command[2]
        skill = skill.replace(substring, "")
        print(skill)
    else:
        print("Command doesn't exist!")