class CharField:
    def __init__(self, prompt):
        self.prompt = prompt
        self.value = ""

    def validate(self):
        """
        this function checks if the value is valid
        :return:
        """
        self.value = input(f"{self.prompt}: ").strip()
        if len(self.value) > 0:
            return True
        print("Field cannot be empty. Please try again.")
        return False


class PasswordField(CharField):
    def validate(self):
        """
        this function checks if the value is valid
        :return:
        """
        self.value = input(f"{self.prompt}: ").strip()
        if len(self.value) < 8:
            print("Password must be at least 8 characters long.")
            return False
        if not any(char.isupper() for char in self.value):
            print("Password must contain at least one uppercase letter.")
            return False
        if not any(char.islower() for char in self.value):
            print("Password must contain at least one lowercase letter.")
            return False
        if not any(char.isdigit() for char in self.value):
            print("Password must contain at least one number.")
            return False
        if not any(char in "!@#$%^&*()-_+=<>?/\\|{}[]" for char in self.value):
            print("Password must contain at least one special character (!@#$%^&* etc.).")
            return False
        return True


def display_users(users):
    """
    this function displays the users
    :param users:
    :return:
    """
    if not users:
        print("No users found.")
        return
    print("\nList of Users:")
    for user in users:
        print(f"Username: {user[0]}, Phone Number: {user[1]}")
