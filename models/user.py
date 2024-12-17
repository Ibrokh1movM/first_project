class Users:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    def __repr__(self):
        return f"Users(username='{self.username}', phone_number='{self.phone_number}')"

    def __str__(self):
        return f"User: {self.username}, Phone: {self.phone_number}"

    def __eq__(self, other):
        if isinstance(other, Users):
            return self.username == other.username
        return False

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.password = new_password
            print("Password updated successfully.")
        else:
            print("Password must be at least 8 characters long.")
