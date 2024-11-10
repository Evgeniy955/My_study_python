import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# Настройки почты
from_email = "galitsyn.evgeniy955@gmail.com"
password = "Ks7K84Lf5z"
to_email = "test_group_for_export-aaaakmpba3frjnncjqesqxmctm@elsevier.org.slack.com"
subject = "Test email with attachment"
body = "This is the body of the email."

# Создание письма
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Прикрепление файла
filename = "Postman_English.zip"
attachment = open("/Users/halitsy.y/Downloads/IPAD 10.6.0.zip", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")
msg.attach(part)

# Отправка письма через SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())

print("Email with attachment successfully sent")