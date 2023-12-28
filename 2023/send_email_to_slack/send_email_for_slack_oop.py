import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

source_folder = 'C:\\Users\\halitsyn.y\\Desktop\\backup_original\\Archive'
output_filename = 'Postman_English'
output_path = 'C:\\Users\\halitsyn.y\\Documents\\Archives'

# Mail settings
from_email = "galitsyn.evgeniy955@gmail.com"
password = "zy63Xa5pf"
to_email = "test_group_for_export-aaaakmpba3frjnncjqesqxmctm@elsevier.org.slack.com"
subject = "Invalid cases for regress"
body = "Table with links"
filename = f"{output_filename}.zip"


class SendMail:
    def __init__(self, source_folder, output_filename, output_path):

        try:
            os.listdir(source_folder)
            shutil.make_archive(os.path.join(output_path, output_filename), 'zip', source_folder)
        except FileNotFoundError:
            print("\033[91mThe folder path isn't correct\033[0m")

    # Attaching a file
    def attaching_a_file(self):
        attachment = open(f"{output_path}\\{filename}", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        return part

    # Sending email via SMTP
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(SendMail.attaching_a_file(self))
        try:
            with smtplib.SMTP('smtp.office365.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())

            print("Email sent successfully")
        except smtplib.SMTPAuthenticationError:
            print("\033[91mAuthentication unsuccessful, the user credentials were incorrect\033[0m")
        finally:
            archive_file = os.path.join(output_path, filename)
            os.remove(archive_file)

SendMail(source_folder, output_filename, output_path).send_mail()
