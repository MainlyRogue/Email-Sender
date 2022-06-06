import smtplib
from email.message import EmailMessage
import webbrowser

def email_Details(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "YOUR EMAIL"
    password = "YOUR APP PASSWORD"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_Details("YOUR SUBJECT", "YOUR DESCRIPTION", "TARGET EMAIL")
    print("You've Got Mail!")
