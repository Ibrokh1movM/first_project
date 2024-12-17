from controllers.user_controller import create_user, get_all_users, delete_user
from views.view import display_users, CharField, PasswordField
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n1. Create User")
        print(Fore.GREEN + Style.BRIGHT + "2. View All Users")
        print(Fore.YELLOW + "3. Delete User")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.MAGENTA + "Enter your choice: ")

        if choice == "1":
            print(Fore.BLUE + Style.BRIGHT + "\nEnter User Details:")

            username_field = CharField("Enter username")
            password_field = PasswordField("Enter password")
            phone_number_field = CharField("Enter phone number")

            if username_field.validate() and password_field.validate() and phone_number_field.validate():
                create_user(username_field.value, password_field.value, phone_number_field.value)
                print(Fore.GREEN + "User created successfully!")
            else:
                print(Fore.RED + "Failed to create user due to invalid inputs.")

        elif choice == "2":
            users = get_all_users()
            if users:
                display_users(users)
            else:
                print(Fore.RED + "No users found.")

        elif choice == "3":
            username = input(Fore.YELLOW + "Enter username to delete: ")
            delete_user(username)

        elif choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "Exiting... Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
