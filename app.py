import sqlite3
import os
from app_files import login

def howToRunSQLQueries(): 
	conn = sqlite3.connect('database_files/hospital.db')
	c = conn.cursor()
	c.execute(' PRAGMA foreign_keys=ON; ')
	c.execute('select * from patients')
	c.fetchone()
	c.fetchall()

login.start()