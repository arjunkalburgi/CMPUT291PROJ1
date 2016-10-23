from .classes import Doctor

def flow(user): 

	d = Doctor(user)
	print("let's do it, ", d.name)	

	while True:

		action = input("\nWhat would you like to do?\n\
		(1) Read a patient's chart\n \
		(2) Report a patient's symptom\n \
		(3) Report your diagnosis of a patient\n \
		(4) Report your medication prescription to a patient\n \
		(5) Logout\n")
		
		if action == "1": 
			# flow to get the patient for the chart
			print("Your task has been completed.")

		elif action == "2":
			# flow to get patient and insert symptom 
			print("Your task has been completed.")

		elif action == "3": 
			# flow to get patient and insert diagnosis
			print("Your task has been completed.")

		elif action == "4": 
			# flow to get patient and insert medication
			print("Your task has been completed.")

		elif action == "5": 
			# logout the user
			print("Thank you. Logging out.")
			break;

		else: 
			print("That is not an option, please try again")