# TASK:
#
# 1. Start the database
# 2. Create a context manager that will connect to the database and execute the sql command passed to it (the
# connection must be closed when the manager exits)
# 3. Output should be printed to console


import mariadb
import sys


class DataConn:
    def __init__(self, user, host, port, password, database):
        """Constructor"""
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.database = database

    def __enter__(self):
        """
        Open the database connection.
        """
        try:
            self.conn = mariadb.connect(
                user=self.user,
                host=self.host,
                port=self.port,
                password=self.password,
                database=self.database
            )
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)

        return self.conn

    def __exit__(self, exc_type, exc_value, tb):
        """
        Close the connection.
        """
        self.conn.close()


def get_sql(database, sql):
    with DataConn(**database) as db:
        cur = db.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        print(*row, sep='\n')


if __name__ == "__main__":
    database = {"user": "country_user",
                "host": "127.0.0.1",
                "port": 3306,
                "password": "qwerty",
                "database": "countries"}

    select_all_country = "SELECT * FROM country"
    select_all_capital = "SELECT * FROM capital"
    select_all = ("SELECT country.*, capital.name, capital.population FROM country JOIN capital ON country.capital_id "
                  "= capital.id")

    print("~" * 35)
    get_sql(database, select_all_country)
    print("~" * 35)
    get_sql(database, select_all_capital)
    print("~" * 35)
    get_sql(database, select_all)
    print("~" * 35)
