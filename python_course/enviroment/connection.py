import os
from dotenv import load_dotenv


def connect(password):
    if password == 'supersecret1':
        return "Connected successfully"
    else:
        return "Wrong password"


load_dotenv()

PASSWORD = os.getenv("PASS")
print(type(PASSWORD))

result = connect(PASSWORD)

print(result)
