def copy(str):
    str_copy = str[::-1]
    return str, str_copy


str = input("Str: ")
print(copy(str))