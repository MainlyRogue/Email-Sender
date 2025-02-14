import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

FromEmail = "YOUR EMAIL"
FromPassword = "YOUR APP PASSWORD"
ToEmail = "RECIPIENT EMAIL"

Message = MIMEMultipart()
Message["From"] = FromEmail
Message["To"] = ToEmail
Message["Subject"] = "YOUR SUBJECT"

Body = "YOUR HTML MESSAGE"
Message.attach(MIMEText(Body, "plain"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as Server:
    Server.login(FromEmail, FromPassword)
    Server.sendmail(FromEmail, ToEmail, Message.as_string())

print("Mail Sent Successfully!")