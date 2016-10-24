import sys
import sqlite3
from classes import *
from time import strftime

conn = None # global for db connection
c = None # global for cursor

# start sqlite database connection
def connectDB():
    global conn
    global c
    conn = sqlite3.connect('database_files/hospital.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

# dict_factory turns query result into a dict with {col_name: value}
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getCurrentTime():
    return strftime("%Y-%m-%d %H:%M:%S")

def getUser(username, password):
    c.execute("SELECT * FROM staff WHERE login=? AND password=?", (username, password))
    return c.fetchone()

def getChartsForPatient(patient):
    c.execute("SELECT * FROM patients, charts WHERE patients.hcno = charts.hcno AND name=? ORDER BY adate", patient)
    return c.fetchall()

def symptomsForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM symptoms WHERE hcno=? AND chart_id=?", (hcno, chart_id))
    return c.fetchall()

def diagnosesForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM diagnoses WHERE hcno=? AND chart_id=?", (hcno, chart_id))
    return c.fetchall()

def medicationsForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM medications WHERE hcno=? AND chart_id=?", (hcno, chart_id))
    return c.fetchall()

def addSymptomToChart(hcno, chart_id, staff_id, symptom):
    c.execute("INSERT INTO symptoms VALUES (?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), symptom))
    conn.commit()

def addDiagnosisToChart(hcno, chart_id, staff_id, diagnosis):
    c.execute("INSERT INTO diagnosis VALUES (?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), diagnosis))
    conn.commit()

def isMedicationAmountValid(drug_name, amount, age_group):
    c.execute("SELECT * FROM dosage WHERE drug_name=? AND age_group=? AND sug_amount >= ?", (drug_name, age_group, amount))
    return c.fetchone() != None

def isPatientAllergicToDrug(hcno, drug_name):
    c.execute("SELECT * FROM drugs WHERE hcno=? AND drug_name=?", (hcno, drug_name))
    return c.fetchone() != None

# returns tuple if patient has an inferred allergy to drug_name
def inferredAllergy(hcno, drug_name):
    c.excute("SELECT * FROM reportedallergies, inferredallergies WHERE hcno=? AND reportedallergies.drug_name = inferredallergies.alg AND inferredallergies.canbe_alg=?", (hcno, drug_name))
    return c.fetchone()

def addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name):
    c.execute("INSERT INTO diagnosis VALUES (?,?,?,?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), start_med, end_med, drug_name))
    conn.commit()

def createPatient(hcno, name, age_group, address, phone, emg_phone):
    c.execute("INSERT INTO diagnosis VALUES (?,?,?,?,?,?)", (hcno, name, age_group, address, phone, emg_phone))
    conn.commit()

def isChartOpenForPatient(hcno):
    c.execute("SELECT * FROM charts WHERE hcno=? AND edate IS NULL", (hcno,))
    return c.fetchone() != None

# returns the id of the new chart
def createNewChartForPatient(hcno):
    c.execute("SELECT MAX(chart_id) as max_id FROM charts")
    new_id = int(c.fetchone()['max_id']) + 1
    c.execute("INSERT INTO charts VALUES (?,?,?,?)", (new_id, hcno, getCurrentTime(), None))
    conn.commit()
    return new_id

def closeChartWithId(chart_id):
    c.execute("UPDATE charts SET edate=? WHERE chart_id=?", (getCurrentTime(), chart_id))
    conn.commit()
