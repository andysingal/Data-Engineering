import smtplib, ssl,os
import certifi


# https://www.youtube.com/watch?v=dEBN1M609zk

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "andysingal@gmail.com"
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context (cafile=certifi.where ())
    receiver = "andysingal@gmail.com"

    with smtplib.SMTP_SSL (host, port, context=context) as server:
        server.login (username, password)
        server.sendmail (username, receiver, message)


