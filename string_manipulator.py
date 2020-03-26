text = input()

def change(string, char, replacement):
    string = string.repalce(char, replacement)
    return string


def includes(string, txt):
    if txt in string:
        return True
    else:
        return False


def end(string, end_string):
    idx = len(string) - len(end_string)
    if string[idx:] == end_string:
        return True
    else:
        return False


def uppercase(string):
    string = string.upper()
    return string


def find_index(string, char):
    idx = string.index(char)
    return idx


def cut(string, start_index, length):
    end_index = start_index + length
    string = string[start_index:end_index]
    return text


while True:
    command = input().split(" ")
    if command[0] == "Done":
        break
    elif command[0] == "Change":
        print(change(text, command[1], command[2]))
    elif command[0] == "Includes":
        print(includes(text, command[1]))
    elif command[0] == "End":
        print(end(text, command[1]))
    elif command[0] == "Uppercase":
        print(uppercase(text))
    elif command[0] == "FindIndex":
        print(find_index(text, command[1]))
    elif command[0] == "Cut":
        print(cut(text, command[1], command[2]))