def mutate_string(string, position, character):
    string = [i for i in string]
    string[position] = character
    return "".join(string)


print(mutate_string("abc", 2, "d"))
