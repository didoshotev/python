info = {}
disliked = 0


def like(guy, eat, dic):
    if guy not in dic:
        dic[guy] = [eat]
    elif guy in dic and eat not in dic[guy]:
        dic[guy].append(eat)


def unlike(guy, eat, dic):
    global disliked
    if guest in info and meal in info[guest]:
        info[guest].remove(meal)
        disliked += 1
        return f"{guest} doesn't like the {meal}."
    elif guest not in info:
        return f"{guest} is not at the party."
    elif meal not in info[guest]:
        return f"{guest} doesn't have the {meal} in his/her collection."


while True:
    command = input().split("-")
    if command[0] == "Stop":
        break
    [guest, meal] = command[1], command[2]
    if command[0] == "Like":
        like(guest, meal, info)

    elif command[0] == "Unlike":
        print(unlike(guest, meal, info))


ordered = dict(sorted(info.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in ordered.items():
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {disliked}")




