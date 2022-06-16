import smtplib

sender = "bryant.logan1@gmail.com"
receiver = "brybuysandtries@gmail.com"
password = "gun99999"
subject = "Python email test"
body = "This is a test email"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)  
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email has been sent")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")