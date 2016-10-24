from abc import ABCMeta, abstractmethod

class CareStaff:
    __metaclass__ = ABCMeta

    @abstractmethod
    def introduce(self):
          return "I'm a "
    
    # For a given patient, list all charts in the system ordered by adate (indicating also whether they are closed or open). The user 
    # should be given the option to select a chart. Once a chart is selected, all entries (symptoms, diagnoses, and medications) 
    # associated with that chart must be listed, and the result must be ordered by the date of the entries.
    def getCharts(self, patient): 
        print("All Charts")
        pass
    # For a given patient and an open chart of the patient add an entry for symptoms. 
    # The date obs_date should be set to the current date and time.
    def addSymptom(self, patient, symptom):
        print("Add symptom")
        pass

class Doctor(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Doctor, self).introduce() + "Doctor"
    
    def getCharts(self, patient):
        return super(Doctor, self).getCharts(patient)
    
    def addSymptom(self, patient, symptom):
        return super(Doctor, self).addSymptom(patient, symptom)
    
    # For a given patient and an open chart of the patient add an entry for diagnosis. 
    # The date ddate should be set to the current date and time.
    def addDiagnosis(self, patient, diagnosis): 
        pass
    
    # For a given patient and an open chart of the patient add an entry for medications. The date mdate should 
    # be set to the current date and time. Additional checks should be performed before adding the entry: 
    # (1) if the prescribed amount for the patient is larger than the recommended amount sug_amount for that
        # drug and the patient's age group, a warning should be issued that contains the information about recommended 
        # amount for a patient for that age group, and the doctor should be given the choice to confirm his prescription 
        # or to change the amount. 
    # (2) If the patient could be allergic to the prescribed drug drug_name, a warning should be issued that contains 
        # the information about the reported allergy; the warning should display the name of the drug that the patient 
        # reported being allergic to, and, if that is not directly drug_name, the name of the drug D  should be dsiplayed,
        # which the patient reported being allergic to and from which it can be "inferred" that the patient may also be 
        # allergic to drug_name.
    def addMedication(self, patient, medication): 
        pass
        
class Nurse(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Nurse, self).introduce() + "Nurse"
    
    def getCharts(self, patient):
        return super(Nurse, self).getCharts(patient)
    
    def addSymptom(self, patient, symptom):
        return super(Nurse, self).addSymptom(patient, symptom)
    
    # Create a new chart for a patient at the time of admission to the hospital. At that point in time, the adate is filled 
    # with the current date and time, and the edate is filled with a NULL value, indicating an "open" chart. Before creating
    # a new chart, the system should check whether there is already an open chart for that patient, and if so, provide the 
    # options to either close this chart before creating a new one, or not creating a new one. When creating a new chart, the
    # system also must provide the functionality to add the patient information, if the patient information is not already in
    # the system (from a previous stay in the hospital).
    def newChart(self, patient):
        pass
    
    # Close a chart when a patient is dismissed from the hospital. At that point in time, the edate is filled with the current 
    # date and time, indicating that the chart is closed.
    def closeChart(self, patient):
        pass
    
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
