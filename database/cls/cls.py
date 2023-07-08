from abc import abstractmethod
import psutil

'''
psutil is a library we use to record the activites of RAM!

'''


class UsedMemoryInterface:
    """
    used memory interface according to dependency inversion desing pattern
    """
    @abstractmethod
    def used_memory(self):
        raise NotImplementedError
class FreedMemoryInterface:
    """
    freememory interface according to dependecy inversion design patter
    """
    @abstractmethod
    def free_memory(self):
        raise NotImplementedError
class TotalInterface:
    """
    totalmemory interface according to dependency inversion design patter
      """
    @abstractmethod
    def total_memory(self):
        raise NotImplementedError
        

        
class ExtractingMachine(UsedMemoryInterface, FreedMemoryInterface, TotalInterface):
    @property
    def used_memory(self):
   
        return(str(psutil.virtual_memory()[3]))
    @property
    def free_memory(self):
        return(str(psutil.virtual_memory()[4]))
    @property
    def total_memory(self):
        return(str(psutil.virtual_memory()[0]))
