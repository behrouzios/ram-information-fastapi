from database_folder.database import checking
import time
while(True):
    '''
    this is a loop to read data from RAM.
    to make the time about 30 minuts , you can change the to time.sleep(1600)
    '''
    incoming=checking()
    print("it is done")
    time.sleep(5)