from contextlib import contextmanager

import mariadb
import sys

select_all_country = "SELECT * FROM country"
select_all_capital = "SELECT * FROM capital"
select_all = ("SELECT country.*, capital.name, capital.population FROM country JOIN capital ON country.capital_id "
                  "= capital.id")

class Database:
    def __init__(self, port: str, host: str, user: str, password: str, database: str):
        self.port = port
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    @contextmanager
    def connect(self):
        try:
            connection = mariadb.connect(
                user=self.user,
                host=self.host,
                port=self.port,
                password=self.password,
                database=self.database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        try:
            cursor = connection.cursor()
            yield {'connection': connection, 'cursor': cursor}
        except Exception as e:
            print(f'an error occurred: {e}')
        finally:
            connection.close()

if __name__ == '__main__':
    database_config = {
        "user": "country_user",
        "host": "127.0.0.1",
        "port": 3306,
        "password": "qwerty",
        "database": "countries"
    }

    db = Database(**database_config)

    with db.connect() as connection:
        connection['cursor'].execute(select_all_country)
        for row in connection['cursor'].fetchall():
            print(row)

        print('')
        connection['cursor'].execute(select_all_capital)
        for row in connection['cursor'].fetchall():
            print(row)

        print('')
        connection['cursor'].execute(select_all)
        for row in connection['cursor'].fetchall():
            print(row)
