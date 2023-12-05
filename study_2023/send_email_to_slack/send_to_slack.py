import os

import requests
import json

# Замените этот URL на URL вашего вебхука Slack
webhook_url = 'https://hooks.slack.com/services/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'
# webhook_url = os.environ.get("SLACK_WEBHOOK", None)

message = {'text': 'test message'}

response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print(response.status_code)
else:
    print(response.status_code)


#For Drone.yaml file
# - name: send_message
#   image: python:3
#   environment:
#     SLACK_WEBHOOK:
#       from_secret: slack_webhook_test_channel
#   commands:
#   - pip3 install requests
#   - python3 Testrail_utils/send_to_slack.py