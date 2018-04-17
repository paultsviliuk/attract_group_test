import smtplib

smpt_host = 'smtp.gmail.com'
smpt_port = 587

login = 'yellow-jacket33@mail.ru'
password = 'pirat93satis'

send_from = "paultsvilyuk@mail.ru"
password_subject = "Password Generation"
password_message = "Here is your password.\n Password: "


def send_password(send_to, user_password):
    smtp=smtplib.SMTP(smpt_host, smpt_port)
    smtp.starttls()
    smtp.login(login, password)
    smtp.sendmail(send_from, send_to, password_message+user_password)
    smtp.quit()
