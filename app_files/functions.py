import sys

def getUser(username, password): 
	# execute sql statement to get user

	# THIS IS TEMPORARY
	if username == 'd': 
		return {'staff_id': '37225', 'role': 'D', 'name': 'Joy'}
	elif username == 'n': 
		return {'staff_id': '37225', 'role': 'N', 'name': 'Joy'}
	elif username == 'a': 
		return {'staff_id': '37225', 'role': 'A', 'name': 'Joy'}
	else: 
		return None