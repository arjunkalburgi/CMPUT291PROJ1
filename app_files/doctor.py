from .classes import Doctor

def getChartsFlow(doc): 
	patient = raw_input("What patient are you working with today? (hcno)")
	returnobj = doc.getCharts(patient)
	if returnobj == "no_patient":
		print("That is not a patient's hcno that we have registered. Please use hcno for the patient.")
		patient = getChartsFlow(doc)
	return patient

def selectChart(doc, patient): 
	chartId = raw_input("Which chart would you like to open? (select id)")
	if !doc.printChartEntries(patient, chartId): 
		print("There was a problem, please type the chartid.")
	return chartId

def addSymptomsFlow(doc, patient, chart):
	symptom = raw_input("Name the symptom:")
	doc.addSymptom(patient, chart, doc.id, symptom)
	print("Symptom has been added to the database.")

def addDiagnosisFlow(doc, patient, chart):
	diagnosis = raw_input("Name the diagnosis:")
	returnobj = doc.addDiagnosis(patient, chart, doc.id, diagnosis)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		addDiagnosisFlow(doc)
	else:
		print("Diagnosis has been added to the database.")

def addMedicationFlow(doc, patient, chart):
	medication = raw_input("Name the medication:")
	returnobj = doc.addMedication(patient, medication)
	if returnobj == "no_patient":
		print("That is not a patient in the database.")
		addMedicationFlow(doc)
	else:
		print("Medication has been added to the database.")

def flow(user):

	d = Doctor(user)
	print("let's do it, ", d.name)

	# select a patient and show their charts
	patient = getChartsFlow(doc)
	
	# select chart 
	chartId = selectChart(doc, patient)
	print(chartId)

	while True:

		action = raw_input("\nWhat would you like to do with this chart?\n\
		(1) Report a patient's symptom\n \
		(2) Report your diagnosis of a patient\n \
		(3) Report your medication prescription to a patient\n \
		(4) Logout\n")

		if action == "1":
			addSymptomsFlow(d) # flow to get patient and insert symptom

		elif action == "2":
			addDiagnosisFlow(d) # flow to get patient and insert diagnosis

		elif action == "3":
			addMedicationFlow(d) # flow to get patient and insert medication

		elif action == "4":
			# logout the user
			break;

		else:
			print("That is not an option (e.g.: 1), please try again")

	print("Bye")
	start()
