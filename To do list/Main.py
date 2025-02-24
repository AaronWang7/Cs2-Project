
print("Welcome to the todo list")


def open_file():
       with open("To do list\To_do_list.txt",mode ="r" endcoding ) as file:
              file_reader = (file)
              print(file_reader)

              


def main():
    while True:
        print("What would you like to do? \n Add\n Remove\n completed a item\n Show all items")
        user_choice = input(":").strip().lower()
        if user_choice == "add":
                print("What would you like to add?")
                items_add = input(":")
        elif user_choice == "Remove":
                print("What would you like to remove?")
        elif user_choice == "show all items":
              open_file()
                



main()