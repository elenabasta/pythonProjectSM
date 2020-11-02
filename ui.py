from item_manager import Start


def show_menu():
    while True:
        print('Item Manager')
        print('--------------')
        print('1. Add Item to collection')
        print('2. Show Items in collection')
        print('3. Delete Items from collection')
        print('4. Exit')
        response = input('Choice> ')

        if response == '1':
            add_item()
        elif response == '2':
            show_items()
        elif response == '3':
            delete_items()
        else:
            print('Invalid Choice!')


def add_item():
    print()
    name = input('Name> ')
    description = input('Description> ')
    if item_list:
        for item in item_list.items():
            if item[0] == name:
                print('Item already exists in the collection')
    else:
        item_list.update({name: description})
        print('Item added!')

    Start(name, description)


def show_items():
    print('Showing items in the collection: \r\n')
    if item_list:
        for item in item_list.items():
            print('Item Name:' + str(item[0]))
            print('Description:' + str(item[1]))
    else:
        print('List is empty. Please insert an item!')


def delete_items():
    print('What would you like to delete: \r\n')
    if item_list:
        for item in item_list.items():
            print('Item Name:' + str(item[0]))
            print('Description:' + str(item[1]))

        response = input('Insert item name to be deleted> ')
        result = item_list.pop(response, None)
        print("Deleted item's value = ", result)
        print("Updated Dictionary :", item_list)
    else:
        print('List is empty. Please insert an item!')


def show_description(start_id: int) -> None:
    s = Start.get_by_id(start_id)
    print()
    print("Marks for student {0} ({1} {2})".format(s.get_id(), s.name, s.description))
    print("{0:10}\t{1:5}".format("Subject", "Mark"))
    for subject, mark in s.get_gradebook().items():
        print("{0:10}\t{1:<5}".format(subject, mark))


def assign_description(start_id: int) -> None:
    s = Start.get_by_id(start_id)
    print()
    print("Adding marks for student {0} ({1} {2})".format(s.get_id(), s.name, s.description))

    while True:
        subject = input("Subject> ")
        mark = input("Mark> ")
        s.add_grade(subject, float(mark))
        response = input("Type [x] to return or [a] to add more grades.")
        if response != 'a':
            return


try:
    item_list = {}
    show_menu()
except Exception as e:
    print(e)
