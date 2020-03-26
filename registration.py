import re
n = int(input())
successful = 0

pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+(.*)?)P@\$"

for i in range(n):
    text = input()
    result = re.match(pattern, text)
    if result:
        successful += 1
        print("Registration was successful")
        print(f"Username: {result[1]}, Password: {result[2]}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {successful}")