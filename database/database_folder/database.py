import time
import psycopg2
import os 
from dotenv import load_dotenv
from cls.cls import ExtractingMachine,UsedMemoryInterface,FreedMemoryInterface,TotalInterface

load_dotenv()

def checking():
    
        '''this is the python code to make -connect and writ code in database'''

        try:
            global cur  
            print("here")
            conn=psycopg2.connect(os.environ["DATABASE_URL"]) 
            cur=conn.cursor()
            create_script='''CREATE TABLE IF NOT EXISTS ramingg_monitorr(
            id SERIAL PRIMARY KEY,
            freed varchar(40),
            used varchar(40),
            total varchar(40))
            '''
            cur.execute(create_script)
            insert_script='''INSERT INTO ramingg_monitorr( freed, used, total) VALUES(%s,%s,%s)'''
            insert_value=(ExtractingMachine().free_memory,ExtractingMachine().used_memory,ExtractingMachine().total_memory)
            cur.execute(insert_script,insert_value)
            conn.commit()  
            return ()
        except Exception as error:
            raise error        
        finally:
            if cur is not None:
                cur.close()             
            if conn is not None:
                conn.close()
               
        
                
