# Write your solution to exercise 2 here

def separate(string: str):
    result = []

    # if empty string return empty list
    if string == "":
        return result

    # split into items
    items = string.split(",")
    for data in items:
        # for each item split into key and value
        parts = data.split(";")
        result.append((parts[0], parts[1]))
    return result


def to_dictionary(my_list: list):
    new_dictionary = {}
    # for each tuple in the list add key add value
    for data in my_list:
        new_dictionary[data[0]] = data[1]

    return new_dictionary


if __name__ == "__main__":
    # list1 = separate('country;finland,;helsinki,room;kitchen')
    # list2 = separate('name;ella')
    # list3 = separate('constructor;aston martin,driver;vettel')

    # print(list1) # [('country', 'finland'), ('city', 'helsinki'), ('room','kitchen')]
    # print(list2) # [('name', 'ella')]
    # print(list3) # [('constructor', 'aston martin'), ('driver', 'vettel')]

    dictionary1 = to_dictionary([('country', 'finland'), ('city', 'helsinki'), ('room', 'kitchen')])
    dictionary2 = to_dictionary([('name', 'ella')])
    dictionary3 = to_dictionary([('constructor', 'aston martin'), ('driver', 'vettel')])

    print(dictionary1)  # {'country': 'finland', 'city': 'helsinki', 'room': 'kitchen'}
    print(dictionary2)  # {'name': 'ella'}
    print(dictionary3)  # {'constructor': 'aston martin', 'driver': 'vettel'}
