info = {}


def validation(name, dic):
    if name in dic:
        return True
    else:
        return False


while True:
    text = input().split("->")
    if text[0] == 'Statistics':
        break
    username = text[1]
    if text[0] == "Add":
        if validation(username, info):
            print(f"{username} is already registered")
        else:
            info[username] = []
    elif text[0] == "Send":
        email = text[2]
        if validation(username, info):
            info[username].append(email)
    elif text[0] == "Delete":
        if validation(username, info):
            del info[username]
        else:
            print(f"{username} not found!")


ordered = dict(sorted(info.items(), key=lambda x: (-len(x[1]), x[0])))


print(f"Users count: {len(info)}")
for key, value in ordered.items():
    print(key)
    for mail in value:
        print(f"- {mail}")



