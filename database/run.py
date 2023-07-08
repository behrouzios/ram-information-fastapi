import uvicorn
import check
import time

if __name__=="__main__":
    ''' use this section to run all the code...
        it mus be mentioned that it is one of the several ways to run the code
    '''
    uvicorn.run(
        
   
        reload=True,
        # debug=True,
        app="main:app"

    )
