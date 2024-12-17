from database.connection import create_connection
from models.user import Users

def create_user(username, password,phone_number):
    """
    this function creates a new user
    :param user:
    :return:
    """
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO users (username, password, phone_number) 
    VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(query, (username, password, phone_number))
        conn.commit()
        print("User created successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def get_all_users():
    """
    this function returns all users
    :return:
    """
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT username, phone_number FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users


def delete_user(username):
    """
    this function deletes a user
    :param username:
    :return:
    """
    conn = create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE username = %s"
    try:
        cursor.execute(query, (username,))
        conn.commit()
        if cursor.rowcount > 0:
            print("User deleted successfully!")
        else:
            print("User not found!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
