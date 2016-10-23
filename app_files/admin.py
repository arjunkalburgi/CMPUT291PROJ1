from .classes import AdminStaff

def flow(user): 

	a = AdminStaff(user)
	print("let's do it, ", a.name)	

	while True:

		action = input("\nWhat would you like to do?\n\
		(1) List drug amounts prescribed by each doctor\n \
		(2) List drug amounts prescribed recently by category\n \
		(3) List medications used for a given diagnosis\n \
		(4) List diagnoses that require a given drug\n \
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