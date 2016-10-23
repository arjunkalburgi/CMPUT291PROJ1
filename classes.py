from abc import ABCMeta, abstractmethod

class CareStaff:
    __metaclass__ = ABCMeta

    @abstractmethod
    def introduce(self):
          return "I'm a "

class Doctor(CareStaff):
    def introduce(self):
        return super(Doctor, self).introduce() + "Doctor"
        
class Nurse(CareStaff):
    def introduce(self):
        return super(Nurse, self).introduce() + "Nurse"
