"""
import smtplib
import ssl
from email.message import EmailMessage
sender_email="jaswanthande98@gmail.com"
password="davuhrktrhopqyfw"
reciver_email="sanjay43650@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciver_email
message["Subject"] = "Birthday Wishes"
message.set_content("Many More Happy Returns Of The Day")
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
"""
#USING TRY EXCEPT AND FINALLY BLOCK
import smtplib
from email.message import EmailMessage
sender_email="jaswanthande98@gmail.com"
password="davuhrktrhopqyfw"
reciver_email="yaswanthpilla55@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciver_email
message["Subject"] = "WARNING"
message.set_content(f"""
HELLO YASWANTH!!!!!
WELCOME TO TRIO
REGARDS,
JASWSANTH ANDE
""")
try:
    smtp= smtplib.SMTP("smtp.gmail.com",port = 587)
    smtp.starttls()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    print("Email sent sucessfully")
except Exception as  e:
    print("Error: ",e)
finally:
    smtp.quit()
    

