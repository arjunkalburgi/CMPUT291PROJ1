from .classes import Nurse
from . import database as db
from .classes import login

def getChartsFlow(nur): 
	patient = raw_input("What patient are you working with today? (hcno or 'new')")
	if patient == "new": 
		nur.newChart(raw_input("Patient HCNO: "), raw_input("Patient name: "), raw_input("Patient age group: "), raw_input("Patient address: "), raw_input("Patient phone number: "), raw_input("Patient emergency number: "))
	else: 
		returnobj = nur.getCharts(patient)
		if returnobj == "no_patient":
			print("That is not a patient's hcno that we have registered. Please use hcno for the patient.")
			patient = getChartsFlow(nur)
	return patient

def selectChart(nur, patient): 
	if nur.checkIfPatientHasOpenChart(patient): 
		if raw_input("This patient already has an open chart, would you like to open it (y or n)? ") == "y":
			pass
			# return open chart's chart ID

	while(True):
		chartId = raw_input("Which chart would you like to open? (type chart's id or 'new')")
		if chartId == "new": 
			newChartFlow(nur, patient)
		else: 
			if not nur.printChartEntries(patient, chartId): 
				print("There was a problem, please type the chartid.")
			else: 
				return chartId

def newChartFlow(nur, patient):
	pass
	# way to get patient info
	# newChart(self, hcno, name, age_group, address, phone, emg_phone):
	# NEED CHART ID

def addSymptomsFlow(nur, patient, chart):
	symptom = raw_input("Name the symptom:")
	nur.addSymptom(patient, chart, nur.id, symptom)
	print("Symptom has been added to the database.")

def closeChartFlow(nur, chart):
	nur.closeChart(chart)
	print("The chart for this patient has been closed.")

def main_nurse(n):
	# select a patient and show their charts
	patient = getChartsFlow(n)
	
	# select chart 
	chartId = selectChart(n, patient)
	print(chartId)

	action = ""
	while True:
		action = raw_input("\nWhat would you like to do with this chart?\n\
		(1) Report this patient's symptom\n \
		(2) Close the patient's chart\n \
		(3) Logout\n")

		if action == "1":
			addSymptomsFlow(n) # flow to get patient and insert symptom

		elif action == "2":
			closeChartFlow(n) # flow to get patient and insert medication

		elif action == "3":
			# logout the user
			break;

		else:
			print("That is not an option (e.g.: 1), please try again")

	if action == "2:
		main_nurse(n)
	else: 
		print("Bye")
		login.start()

def flow(user):

	n = Nurse(user)
	print("let's do it, ", n.name)

	main_nurse(n)
