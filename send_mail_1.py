import smtplib

fromaddr="your email @gmail.com"
toaddr="to email @gmail.com"

message="Hi this is a sending from python script"
password="zour password"
sever=smtplib.SMTP("smtp.gmail.com:587")
server=starttls()
server.login(fromaddr, password)
server.sendmail(fromaddr, toaddr, message)
server.quit()

