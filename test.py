import sqlite3
import os
import app_files.login as login
import app_files.database as database
from app_files.classes import *

database.connectDB()

user = getUser('PugLove8', 'These Need Hashing')
admin = AdminStaff(user)
print database.isChartOpenForPatient('79024')
print database.listMedicationsForDiagnosis("Ebola")
