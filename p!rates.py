targeted = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    [city, population, gold] = command
    population = int(population)
    gold = int(gold)
    if city not in targeted:
        targeted[city] = [population, gold]
    else:
        targeted[city][0] += population
        targeted[city][1] += gold

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    elif command[0] == "Plunder":
        city = command[1]
        population = int(command[2])
        gold = int(command[3])
        if city in targeted:
            targeted[city][0] -= population
            targeted[city][1] -= gold
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
            if targeted[city][0] <= 0 or targeted[city][1] <= 0:
                print(f"{city} has been wiped off the map!")
                del targeted[city]
    elif command[0] == "Prosper":
        city = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        elif city in targeted:
            targeted[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {targeted[city][1]} gold.")

ordered = dict(sorted(targeted.items(), key=lambda x: (-x[1][1], x[0])))

if len(ordered) > 0:
    print(f"Ahoy, Captain! There are {len(ordered)} wealthy settlements to go to:")
    for key, value in ordered.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

