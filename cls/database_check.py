import psycopg2
from dotenv import load_dotenv
import os 
load_dotenv()



def get_db():
    '''this is the code we use to make connection with database for using in fastapi'''
    conn=psycopg2.connect(os.environ["DATABASE_URL"])
    cur=conn.cursor()
    try:
        return conn
    except:
        conn.close()
