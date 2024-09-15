import os

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('API_KEY')
print(key)
print(f'Hello {os.getenv("NAME")}')
print(os.getenv('PASSWORD'))