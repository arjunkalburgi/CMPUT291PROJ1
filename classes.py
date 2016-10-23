from abc import ABCMeta, abstractmethod

class CareStaff:
    __metaclass__ = ABCMeta

    @abstractmethod
    def introduce(self):
          return "I'm a "
    
    # For a given patient, list all charts in the system ordered by adate (indicating also whether they are closed or open). The user 
    # should be given the option to select a chart. Once a chart is selected, all entries (symptoms, diagnoses, and medications) 
    # associated with that chart must be listed, and the result must be ordered by the date of the entries.
    def getCharts(patient): 
        print "All Charts"
        pass
    # For a given patient and an open chart of the patient add an entry for symptoms. 
    # The date obs_date should be set to the current date and time.
    def addSymptom(patient):
        print "Add symptom"
        pass

class Doctor(CareStaff):
    def introduce(self):
        return super(Doctor, self).introduce() + "Doctor"
        
class Nurse(CareStaff):
    def introduce(self):
        return super(Nurse, self).introduce() + "Nurse"
