import sys
from .database import getUser
from doctor import flow as d_flow
from nurse import flow as n_flow
from admin import flow as a_flow

def encrypt(s):
	# r = ""
	# for char in s:
	# 	r = r + chr(ord(char) + 2)
	# return r
	return s

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
			d_flow(user)
		if user['role'] == 'N':
			n_flow(user)
		if user['role'] == 'A':
			a_flow(user)
	else:
		print('Invalid username or password! Please try again')
		start()
