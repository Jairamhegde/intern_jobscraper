import sqlite3
import pandas as pd
db_path = 'jobs.db'
def topSkills():
    conn = sqlite3.connect(db_path)
    query = '''
    SELECT s.name, count(*) as demand
    FROM skills s
    JOIN job_skills js ON s.s_id = js.skill_id
    GROUP BY s.name
    ORDER BY demand DESC
    limit 10;
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
def roles():
    conn=sqlite3.connect(db_path)
    query='''
    SELECT j.j_title,count(*) as demand
    FROM jobs j
    GROUP BY j_title
    ORDER BY demand DESC
    LIMIT 10;
    '''
    df=pd.read_sql_query(query,conn)
    conn.close()
    return df
def topLocations():
    conn=sqlite3.connect(db_path)
    query='''
    SELECT j.location ,count(j.location) as count
    FROM jobs j
    GROUP BY j.location
    ORDER BY count DESC
    limit 10;
'''
    df=pd.read_sql_query(query,conn)
    conn.close()
    return df
# print(topSkills())
print(roles())

