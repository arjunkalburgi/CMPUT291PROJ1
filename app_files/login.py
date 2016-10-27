import sys
from .database import getUser

def encrypt(s):
	r = ""
	for char in s:
		r = r + chr(ord(char) + 2)
	return r

def decrypt(s):
	r = ""
	for char in s:
		r = r + chr(ord(char) - 2)
	return r

def start():
	username = raw_input('Please login with your username: ')
	password = raw_input('And password: ')

	user = getUser(encrypt(username), encrypt(password)) # return obj of user info, or None if can't be found
	if user is not None:
		if user['role'] == 'D':
			doctor.flow(user)
		if user['role'] == 'N':
			nurse.flow(user)
		if user['role'] == 'A':
			admin.flow(user)
	else:
		print('Invalid username or password! Please try again')
		start()
