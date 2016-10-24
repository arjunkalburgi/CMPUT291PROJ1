from .classes import Nurse

def getChartsFlow(nur):
	patient = raw_input("Select a patient (hcno or name): ")
	returnobj = nur.getCharts(patient)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		getChartsFlow(nur)
	else:
		# show charts
		print("charts")

def addSymptomsFlow(nur):
	patient = raw_input("Select a patient (hcno or name): ")
	symptom = raw_input("Name the symptom:")
	returnobj = nur.addSymptom(patient, symptom)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		addSymptomsFlow(nur)
	else:
		print("Symptom has been added to the database.")

def newChartFlow(nur):
	patient = raw_input("Select a patient (hcno or name): ")
	returnobj = nur.newChart(patient)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		newChartFlow(nur)
	else:
		print("A new chart has been created in the database.")

def closeChartFlow(nur):
	patient = raw_input("Select a patient (hcno or name): ")
	returnobj = nur.newChart(patient)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		newChartFlow(nur)
	elif returnobj == "no_chart":
		print("There is no open chart for this patient.")
	else:
		print("The chart for this patient has been closed.")

def flow(user):

	n = Nurse(user)
	print("let's do it, ", n.name)

	while True:

		action = raw_input("\nWhat would you like to do?\n\
		(1) Read a patient's chart\n \
		(2) Report a patient's symptom\n \
		(3) Open a new chart for a patient\n \
		(4) Close a patient's chart\n \
		(5) Logout\n")

		if action == "1":
			# flow to get the patient for the chart
			getChartsFlow(n)

		elif action == "2":
			# flow to get patient and insert symptom
			addSymptomsFlow(n)

		elif action == "3":
			# flow to get patient and insert diagnosis
			newChartFlow(n)

		elif action == "4":
			# flow to get patient and insert medication
			closeChartFlow(n)

		elif action == "5":
			# logout the user
			print("Thank you. Logging out.")
			break;

		else:
			print("That is not an option, please try again")
