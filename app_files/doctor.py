from .classes import Doctor
from .database import *

def getChartsFlow(doc): 
	patient = raw_input("What patient are you working with today? (hcno)")
	returnobj = doc.getCharts(patient)
	if returnobj == "no_patient":
		print("That is not a patient in the database. Please use hcno.")
		getChartsFlow(doc)
	else:
		print("charts")
	return patient

def selectChart(doc, patient): 
	chartId = raw_input("Which chart would you like to open? (select id)")
	returnobj = doc.openCharts(patient, chartId)
	if returnobj == "no_chart": 
		print("That is not a chart id, please select again.")
		doc.getCharts(patient)
		selectChart(doc, patient)
	else: 
		print("chart!")
	return returnobj

def addSymptomsFlow(doc, patient, chart):
	symptom = raw_input("Name the symptom:")
	returnobj = doc.addSymptom(patient, symptom)
	# if returnobj == "no_patient":
	# 	print("That is not a patient in the database.")
	# 	addSymptomsFlow(doc)
	# else:
	print("Symptom has been added to the database.")

def addDiagnosisFlow(doc, patient, chart):
	diagnosis = raw_input("Name the diagnosis:")
	returnobj = doc.addDiagnosis(patient, diagnosis)
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
	print("chart id")

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