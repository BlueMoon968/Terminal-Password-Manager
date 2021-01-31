#====================================================================
# PASSWORD MANAGER
# Author: Luca Mastroianni
# Description: Password Manager developed for my personal use.
# It read and parse info from a JSON dictionary. 
#
# LICENSE: MIT
#====================================================================

import os
import socket
import json
import time

#============================
# ENTRY POINT

# STATES:
# -1 - WAIT
# 0 - MAIN COMMANDS
# 1 - FIND ENTRY
# 2 - NEW ENTRY
# 3 - BYE


def waitForInput():
	print("Wait for input...")
	sec = input()

current_state = 0
with open("./database.json") as f:
	database = json.load(f)
	while(1):
		os.system("cls")
		if current_state == 0:
			print(f'== PASSWORD MANAGER == {socket.gethostname()}')
			print(" ")
			print(f'-- WHAT CAN I DO FOR YOU ?')
			print(f'1. Find Entry')
			print(f'2. New Entry')
			print(f'3. Bye')
			print(" ")
			current_state = int(input("Command (ex. 1): ").strip())
		elif current_state == 1: # Find Entry
			entry = input("Research for... ")
			print(" ")
			if entry.strip().lower() in database:
				data = database[entry.strip().lower()]
				print(f'Entry Name: {entry}')
				print(f'Username: {data["username"]}')
				print(f'Password: {data["password"]}')
				print(" ")
			else:
				print(f'No entry found for {entry}!')
				print(" ")
			waitForInput()
			current_state = 0
		elif current_state == 2: # New Entry
			print("Add new data to the database.")
			key = input("Entry name: ")
			username = input("Username: ")
			password = input("Password: ")
			database[key.lower().strip()] = {"username": username, "password": password}
			with open("./database.json", "w") as json_file:
				json.dump(database, json_file)
				print(" ")
				print("Database Saved!")
				print(" ")
				waitForInput()
				current_state = 0
		elif current_state == 3:
			exit()
			break