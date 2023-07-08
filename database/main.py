from fastapi import FastAPI,Depends,status,HTTPException
from cls.database_check import get_db
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")

async def root():
    '''we use this part to fetch all the necessary data to show ...
    change the my_reord number to change the number of showing data ...
    '''
    try:
        new={}
        cur= get_db().cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM ramingg_monitorr')
        my_record = cur.fetchall()[-30:]
        new["data"]=my_record
        return JSONResponse(status_code=status.HTTP_200_OK, content=new)      
    except:
        raise HTTPException(status_code=404, detail="Item not found")



