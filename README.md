---

# 📧 Email Sender

A simple Python script that sends an email using Gmail's SMTP server. It allows you to send plain-text or HTML emails.

⚠️ **Important** – Use this tool responsibly, and make sure to enable "App Passwords" if you're using Gmail with 2FA.

## ⚙️ Features
- Sends an email through Gmail using an SMTP connection.
- Supports plain-text or HTML body content.
- Requires Gmail account credentials, including an app password for authentication.

## 🚀 Installation

### Prerequisites

To run this project, you need Python 3.x installed and the `smtplib` library, which is part of the Python standard library.

### 🛠️ Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MainlyRogue/Email-Sender.git
   cd Email-Sender
   ```

2. Replace the placeholder values with your credentials and message content in the script :
   - `FromEmail` : Your email address (Gmail).
   - `FromPassword` : Your Gmail app password (see the instructions below).
   - `ToEmail` : The recipient's email address.
   - `Subject` : The subject of the email.
   - `Body` : The content of the email in HTML or plain text.

3. Run the script :

   ```bash
   python EmailSender.py
   ```

### 📦 Dependencies

- **No additional packages required.** This script uses Python’s built-in `smtplib` and `email.mime` libraries.

## 🛑 How It Works

1. The script connects to Gmail's SMTP server (`smtp.gmail.com` on port 465).
2. It authenticates using your email and app password (you must use an "App Password" if two-factor authentication is enabled).
3. It sends the message to the recipient with the specified subject and body content.

## 📝 Usage

1. Run the script :

   ```bash
   python EmailSender.py
   ```

2. The script will send the email, and you should see a confirmation in the terminal :
   
   ```text
   Mail Sent Successfully!
   ```

## ⚙️ Configuration

- **App Password** : If you use two-factor authentication (2FA) on Gmail, you must generate an App Password instead of using your regular account password. You can do this via your [Google Account settings](https://myaccount.google.com/security).
- **Message Format** : You can modify the `Body` variable to include either plain text or HTML content.

---
