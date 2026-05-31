d = {'a': 1, 'b': 2, 'd': 3}

key = input("Enter key: ")

try:
    print("The value associated with '{}' is : {}".format(key, d[key]))
except KeyError:
    print("The value associated with '{}' is : Key Not found".format(key))