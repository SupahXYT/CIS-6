from random import randrange

class sortedList():                                                                                                     
    def __init__(self, list):                                                                                           
        self._list = list                                                                                                
                                                                                                                        
    def shuffle(self):                                                                                                  
        for i in range(0, len(self._list)):                                                                                  
            random = randrange(0, len(self._list))
            self._list.insert(i, self._list.pop(random))
                                                                                                                        
   def mergeSort(self):                                                                                                   
       max = int(len())

    def _merge(self, left, right): # Returns merged list
        merge = []

        while(len(left) > 0 or len(right) > 0): # While there exists elements in either list
            while(len(left) > 0):
                if(len(right) > 0 and left[0] < right[0]):
                    merge.append(left.pop(0))
                elif(not(len(right) > 0)):
                    merge.append(left.pop(0))
                else:
                    merge.append(right.pop(0))
            while(len(right) > 0):
                if(len(left) > 0 and right[0] < left[0]):
                    merge.append(right.pop(0))
                elif(not(len(left) < 0)):
                    merge.append(right.pop(0))
                else:
                    merge.append(left.pop(0))

        return merge
       
    def _split(self, list):
        s = []
        for i in range(0, len(list)):
            a = []
            a.append(list[i])
            s.append(a)
        return s

    def getList(self):                                                                                                  
        return self._list                                                                                               
                                                                                                                        
a = sortedList([1, 2, 3, 4, 5, 6])                                                                                                      
                                                                                                                        
print(a.getList())                                                                                                      
a.shuffle()                                                                                                             
print(a.getList())                    
print("main:" + str(a._merge([11230], [9, 11, 99, 100, 235])))

