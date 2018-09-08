"""
    Created by RishabhBhatnagar on 08/09/2018.
"""
from collections import Counter
from operator import itemgetter

STRING = "".join([str(ord(char)) for char in "string"])
NUMBER = "".join([str(ord(char)) for char in "number"])
IMAGE = "".join([str(ord(char)) for char in "image"])

data_types = {}
data_types[type("")] = STRING
data_types[type(1)] = NUMBER
data_types[type(1.1)] = NUMBER
        
"assuming only three types of data."

class _Data:
    
    class_bound_variales = ["cap", "data", "dominant_data_type", "_is_mixed"]
    class_bound_methods = ["__init__", "auto_detect_data", "is_mixed", "get_index_mixed"]
    
    def __init__(self, data, cap = 100):
        """
        this class is to store data of only one 'column'
        """
        self.cap = cap                  #max 100 rows of data will be checked by default
        self.data = data
        self.dominant_data_type = self.auto_detect_data(data)
         
    def auto_detect_data(self, data):
        "sets the type of data the column contains"
        
        """
          #Workflow : 
           1) pick chunks of data 
           2) traverse the chunk and wrt to maximum type, set the data type.
        """
        
        
        chunk_size = min([self.cap, len(data), len(data)//3])
        chunk = data[ : chunk_size]
        result = []
        for element in chunk :
            try :
                # element is either number or string 
                result.append(data_types[type(element)])
            except : 
                try : 
                    #checking if element is an image by checking nested lists of depth = 2
                    element[0][0]
                    result.append(IMAGE)
                except:
                    raise ValueError("unhandled data type")
                    
        counter = dict(Counter(result))
        return max(counter.items(), key = itemgetter(1))[0]

    def is_mixed(self):
        try : 
            return self._is_mixed
        except:
            print("traversing")
            for element in self.data : 
                if data_types[type(element)] != self.dominant_data_type:
                    self._is_mixed = True
                    return True
            self._is_mixed = False
            return False
    
    def get_index_mixed(self):
        for i, element in enumerate(self.data) : 
            if data_types[type(element)] != self.dominant_data_type:
                self._is_mixed = True
                yield i
        self._is_mixed = False
           
d = _Data([1,2,3]+[''])
print(d.get_index_mixed())
