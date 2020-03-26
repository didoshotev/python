info = {}

while True:
    command = input().split(": ")
    user_check = True
    if command[0] == "Log out":
        break
    username = command[1]
    if username in info:
        user_check = False
    if command[0] == "New follower":
        if user_check:
            info[username] = [0, 0]
    elif command[0] == "Like":
        count = int(command[2])
        if user_check:
            info[username] = [count, 0]
        else:
            info[username][0] += count
    elif command[0] == "Comment":
        if user_check:
            info[username] = [0, 1]
        else:
            info[username][1] += 1
    elif command[0] == "Blocked":
        if user_check:
            print(f"{username} doesn't exist.")
        else:
            del info[username]


print(f"{len(info)} followers")

ordered = dict(sorted(info.items(), key=lambda x: (-sum(x[1]), x[0])))

for key, value in ordered.items():
    print(f"{key}: {sum(value)}")

