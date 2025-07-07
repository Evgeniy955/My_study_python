import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="country_user",
        password="qwerty",
        host="127.0.0.1",
        port=8080,
        database="countries"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()