from .classes import Doctor

def getChartsFlow(doc): 
	patient = input("Select a patient (hcno or name): ")
	returnobj = doc.getCharts(patient)
	if returnobj == "no_patient": 
		print("That is not a patient in the database.")
		getChartsFlow(doc)
	else: 
		# show charts
		print("charts")
		pass

def addSymptomsFlow(doc): 
	patient = input("Select a patient (hcno or name): ")
	symptom = input("Name the symptom:")
	returnobj = doc.addSymptom(patient, symptom)
	if returnobj == "no_patient": 
		print("That is not a patient in the database.")
		addSymptomsFlow(doc)
	else: 
		print("Symptom has been added to the database.")

def addDiagnosisFlow(doc): 
	patient = input("Select a patient (hcno or name): ")
	diagnosis = input("Name the diagnosis:")
	returnobj = doc.addDiagnosis(patient, diagnosis)
	if returnobj == "no_patient": 
		print("That is not a patient in the database.")
		addDiagnosisFlow(doc)
	else: 
		print("Diagnosis has been added to the database.")

def addMedicationFlow(doc):
	patient = input("Select a patient (hcno or name): ")
	medication = input("Name the medication:")
	returnobj = doc.addMedication(patient, medication)
	if returnobj == "no_patient": 
		print("That is not a patient in the database.")
		addMedicationFlow(doc)
	else: 
		print("Medication has been added to the database.")

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
			# flow to get all charts for the patient
			getChartsFlow(d)

		elif action == "2":
			# flow to get patient and insert symptom 
			addSymptomsFlow(d)

		elif action == "3": 
			# flow to get patient and insert diagnosis
			addDiagnosisFlow(d)

		elif action == "4": 
			# flow to get patient and insert medication
			addMedicationFlow(d)

		elif action == "5": 
			# logout the user
			break;

		else: 
			print("That is not an option, please try again")