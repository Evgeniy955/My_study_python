import requests
import json
import base64

webhook_url = 'https://hooks.slack.com/services/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'

# Прочитать файл и закодировать его в base64
file_name = "C:\\Users\\halitsyn.y\\Desktop\\test_file.txt"
with open(file_name, "rb") as file:
    file_data = base64.b64encode(file.read()).decode("utf-8")

message = {'text': file_data,
           "file_name": file_name,
           "file_data": file_data
}

response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print('Сообщение успешно отправлено на Slack!')
else:
    print('Произошла ошибка при отправке сообщения на Slack.', response.status_code)
