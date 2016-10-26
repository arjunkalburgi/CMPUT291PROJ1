from database import *
from abc import ABCMeta, abstractmethod

def printRow(row):
    for key, value in row.iteritems():
        print '- ' + str(key) + ': ' + str(value)

class CareStaff:
    __metaclass__ = ABCMeta

    @abstractmethod
    def introduce(self):
          return "I'm a "

    def getCharts(self, patient):
        print 'Charts for patient with health care number ' + patient + ':'
        charts = getChartsForPatient(patient)
        if len(charts) == 0:
            print 'No results!'
            return
        for idx, row in enumerate(charts):
            print 'Chart ' + str(idx + 1) + ':'
            printRow(row)

    def printChartEntries(self, patient, chart_id):
        symptoms = symptomsForPatientAndChart(patient, chart_id)
        diagnoses = diagnosesForPatientAndChart(patient, chart_id)
        medications = medicationsForPatientAndChart(patient, chart_id)
        for idx, row in enumerate(symptoms):
            print 'Symptom ' + str(idx + 1) + ':'
            printRow(row)
        for idx, row in enumerate(diagnoses):
            print 'Diagnosis ' + str(idx + 1) + ':'
            printRow(row)
        for idx, row in enumerate(medications):
            print 'Medication ' + str(idx + 1) + ':'
            printRow(row)

    def addSymptom(self, hcno, chart_id, staff_id, symptom):
        addSymptomToChart(hcno, chart_id, staff_id, symptom)

class Doctor(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Doctor, self).introduce() + "Doctor"

    def addDiagnosis(self, hcno, chart_id, staff_id, diagnosis):
        addDiagnosisToChart(hcno, chart_id, staff_id, diagnosis)

    def checkMedicationAmountValid(self, drug_name, amount, age_group):
        return isMedicationAmountValid(drug_name, amount, age_group)

    def getValidMedicationAmount(self, drug_name, age_group):
        return getValidMedicationAmount(drug_name, age_group)

    # returns true if patient is allergic to drug
    def checkPatientAllergicToDrug(self, hcno, drug_name):
        return isPatientAllergicToDrug(hcno, drug_name)

    # returns the drug that causes the inferred allergy if there is one. else returns none
    def checkInferredAllergyToDrug(self, hcno, drug_name):
        return inferredAllergy(hcno, drug_name)

    def addMedication(self, hcno, chart_id, staff_id, start_med, end_med, drug_name):
        addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name)

class Nurse(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Nurse, self).introduce() + "Nurse"

    # returns the new chart's id
    def newChart(self, hcno, name, age_group, address, phone, emg_phone):
        return createPatient(hcno, name, age_group, address, phone, emg_phone)

    def checkIfPatientHasOpenChart(self, hcno):
        return isChartOpenForPatient(hcno)

    def closeChart(self, chart_id):
        closeChartWithId(chart_id)

class AdminStaff():
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    # Create a report, that lists for each doctor the name and the total amount of each drug that the doctor prescribed in a
    # specified period of time. (Drugs that he did not prescribe in that period of time should not be listed.)
    def listDrugAmtForEachDoctor(self):
        pass

    # For each category of drugs, list the total amount prescribed for each drug in that category in a specified period of time.
    # The report should also contain a total for each category.
    def listDrugAmtForEachCategory(self, start, end):
        pass

    # List for a given diagnosis all possible medications that have been prescribed over time after that diagnosis (over all charts).
    # The list should be ordered by the frequency of the medication for the given diagnosis.
    def listMedicationsForDiagnosis(self, diagnosis):
        pass

    # List for a given drug all the diagnoses that have been made before prescribing the drug (over all charts). The list should be
    # ordered by the average amount of the drug prescribed for the diagnoses.
    def listDiagnosisesForDrug(self, drug):
        pass
