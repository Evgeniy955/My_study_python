import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from requests_oauthlib import OAuth2Session

# Настройки почты
from_email = "your_email@outlook.com"
to_email = "your_slack_channel_email@slack.com"
subject = "Test email with attachment"
body = "This is the body of the email."

# OAuth2 настройки
client_id = 'your_client_id'
client_secret = 'your_client_secret'
refresh_token = 'your_refresh_token'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

# Получение токена доступа
extra = {
    'client_id': client_id,
    'client_secret': client_secret,
}
oauth2_session = OAuth2Session(client_id, token=refresh_token)
token = oauth2_session.refresh_token(token_url, **extra)

# Создание письма
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Прикрепление файла
filename = "your_archive.zip"
attachment = open("/path/to/your_archive.zip", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")
msg.attach(part)

# Отправка письма через SMTP с использованием OAuth2
with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.starttls()
    server.login(from_email, token['access_token'])
    server.sendmail(from_email, to_email, msg.as_string())

print("Email с файлом успешно отправлен")