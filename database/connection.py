import psycopg2

def create_connection():
    """
    this function creates a new database connection to the SQLite database
    :return:
    """
    try:
        conn = psycopg2.connect(
            database="nt",
            user="postgres",
            password="Muzaffar080403",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error while connecting to the database:", e)
        return None
