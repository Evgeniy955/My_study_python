from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

my_token = "xoxe.xoxp-1-Mi0yLTQ5OTMyMjMwNzEtNTY3MTU0NDE2Mzk2OC01NzI2NzA5MTc0OTQ1LTU4NDAzNjE2OTM2NzEtNGJiNDFmYzVhZmI3YzI3NDkxYWRmYjdhYzczNzdkNmQyOGY0OWM3ZWJiZDhhMWZkMzQ4Y2FiMTlkMTdhZjM2MA"
client = WebClient(token=my_token)

try:
    response = client.files_upload_v2(
        channel='C05LXP4R55J',
        file='C:\\Users\\halitsyn.y\\Desktop\\Postman_English.7z',
        title='Archive File',
        initial_comment='Here is the archive file!'
    )
    print(f"File uploaded successfully: {response['file']['name']}")
except SlackApiError as e:
    print(f"Error uploading file: {e.response['error']}")
