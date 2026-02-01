import sqlite3

conn=sqlite3.connect("jobs.db")
cur=conn.cursor()
cur.execute(
    '''
CREATE TABLE IF NOT EXISTS jobs(
j_id INTEGER PRIMARY KEY AUTOINCREMENT,
J_title TEXT,
location TEXT,
salary TEXT,
status TEXT
)
'''
)
cur.execute(
    '''
CREATE TABLE IF NOT EXISTS skills(
s_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)
'''
)
cur.execute(
    '''
CREATE TABLE IF NOT EXISTS job_skills(
job_id INTEGER,
skill_id TEXT,
FOREIGN KEY (job_id) references jobs(j_id),
FOREIGN KEY (skill_id) REFERENCES skills(s_id) 
)
'''
)


conn.commit()
conn.close()