# sending email using a pytho program
import smtplib
from email.mime.text import MIMEText

# first type the body text for our mail
body = """This is my text mail. This is sent to you from a bhanu developer."""

# create MIMEText class object with body
msg = MIMEText(body)

# from which address the mail is sent
fromaddr = "senderEmail@gmail.com"

# to which address the mail is sent
toaddr = "receiverEmail@gmail.com"

# store the addresses into msg object
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Hello Message"

server = smtplib.SMTP("smtp.gmail.com", port=587)
server.starttls()

# login to the server with your correct password
server.login(fromaddr, "mypassword")

# send the message to the server
server.send_message(msg)
print("Mail sent successfully")

server.quit()
