import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print("\nPython Setup Script By ST.\n")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pkg install openssl')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = 14913603
cpass.set('cred', 'id', xid)
xhash = 'c3eb6c57a275655da516fd300c615d27'
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Enter Phone Number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Setting Up Python Completed!")
print(gr+"[+] Now, You Can Run The Tools You Need!")
