import sqlite3
import os
conn = sqlite3.connect('database_files/hospital.db')
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON; ')
c.execute('select * from patients')
c.fetchone()
c.fetchall()
