Here is your **README.md** file in simple English for better understanding 👇

---

# 📧 Working With Email in Python

Using `smtplib` (Send Email) and `imaplib` (Read Email)

---

## 📌 Introduction

In Python, we can work with emails using built-in libraries:

* `smtplib` → Used to **send emails**
* `imaplib` → Used to **receive/read emails**
* `email` module → Used to format email messages

---

# ✉️ Part 1: Sending Email Using `smtplib`

## 🔹 What is `smtplib`?

`smtplib` means **Simple Mail Transfer Protocol Library**.
It is used to send emails from Python.

---

## 🛠 Steps to Send Email

1. Enable 2-Step Verification in Gmail
2. Create App Password
3. Use `smtplib` in Python

---

## ✅ Example: Send Simple Email

```python
import smtplib
from email.message import EmailMessage

# Create email
msg = EmailMessage()
msg['Subject'] = "Test Email"
msg['From'] = "your_email@gmail.com"
msg['To'] = "receiver_email@gmail.com"
msg.set_content("Hello, This is a test email from Python!")

# Connect to Gmail SMTP Server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.send_message(msg)

print("Email Sent Successfully!")
```

---

## 🔎 Explanation

| Code                              | Meaning                          |
| --------------------------------- | -------------------------------- |
| `SMTP_SSL("smtp.gmail.com", 465)` | Connect securely to Gmail        |
| `server.login()`                  | Login using email & app password |
| `send_message()`                  | Send email                       |

---

# 📥 Part 2: Receiving Email Using `imaplib`

## 🔹 What is `imaplib`?

`imaplib` is used to **read emails from inbox**.

IMAP = Internet Message Access Protocol

---

## ✅ Example: Read Latest Email

```python
import imaplib
import email

# Connect to Gmail IMAP Server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login("your_email@gmail.com", "your_app_password")

# Select Inbox
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")

mail_ids = messages[0].split()

# Get latest email
latest_email_id = mail_ids[-1]

status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

raw_email = msg_data[0][1]
msg = email.message_from_bytes(raw_email)

print("Subject:", msg["Subject"])
print("From:", msg["From"])
```

---

## 🔎 Explanation

| Code              | Meaning           |
| ----------------- | ----------------- |
| `IMAP4_SSL()`     | Secure connection |
| `select("inbox")` | Open inbox        |
| `search()`        | Find emails       |
| `fetch()`         | Get email data    |

---

# 🔐 How To Create Gmail App Password (Important)

⚠️ Normal Gmail password will NOT work.
You must create **App Password**.

---

## ✅ Step 1: Turn On 2-Step Verification

1. Go to your Google Account.
2. Click **Security**.
3. Find **Signing in to Google**.
4. Click **2-Step Verification**.
5. Turn it ON.
6. Add your phone number.

---

## ✅ Step 2: Create App Password

1. Go to **Security** section again.
2. Click **App passwords**.
3. Select:

   * App → Mail
   * Device → Windows Computer (or Other)
4. Click **Generate**.
5. Google will give you **16-character password**.
6. Copy that password.

Example:

```
abcd efgh ijkl mnop
```

👉 Remove spaces when using in Python:

```
abcdefghijklmnop
```

---

# 🔐 Important Gmail Settings

If email is not working:

* Make sure IMAP is enabled:

  * Gmail → Settings → See All Settings → Forwarding and POP/IMAP → Enable IMAP

---

# 📦 Common Errors

### ❌ 1. 535 Authentication Failed

👉 Wrong app password

### ❌ 2. IMAP not enabled

👉 Enable IMAP in Gmail settings

---

# 🧠 Summary

| Library   | Work         |
| --------- | ------------ |
| `smtplib` | Send Email   |
| `imaplib` | Read Email   |
| `email`   | Format Email |

---

# 🚀 Bonus: Send Email With Attachment

```python
from email.message import EmailMessage
import smtplib

msg = EmailMessage()
msg['Subject'] = "File Attachment"
msg['From'] = "your_email@gmail.com"
msg['To'] = "receiver_email@gmail.com"

msg.set_content("Please find attached file.")

with open("file.txt", "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename="file.txt")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.send_message(msg)

print("Email with attachment sent!")
```

---

# 🎯 Final Notes

✔ Always use App Password
✔ Never share your password
✔ Use `SMTP_SSL` and `IMAP4_SSL` for security

