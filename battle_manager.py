info = {}

while True:
    command = input().split(":")
    if command[0] == "Results":
        break
    elif command[0] == "Add":
        name = command[1]
        health = int(command[2])
        energy = int(command[3])
        if name not in info:
            info[name] = [health, energy]
        else:
            info[name][0] += health
            info[name][1] += energy
    elif command[0] == "Attack":
        attacker = command[1]
        defender = command[2]
        dmg = int(command[3])
        if attacker in info and defender in info:
            info[defender][0] -= dmg
            info[attacker][1] -= 1
            if info[defender][0] <= 0:
                print(f"{defender} was disqualified!")
                del info[defender]
            if info[attacker][1] <= 0:
                print(f"{attacker} was disqualified!")
                del info[attacker]

    elif command[0] == "Delete":
        username = command[1]
        if username == "All":
            info = {}
        else:
            if username in info:
                del info[username]


ordered = dict(sorted(info.items(), key=lambda x: (-x[1][0], x[0])))

print(f"People count: {len(ordered)}")

for key, value in ordered.items():
    value = [str(x) for x in value]
    print(f"{key} - {' - '.join(value)}")