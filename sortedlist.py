from random import randrange

class sortedList():                                                                                                     
    def __init__(self, list):                                                                                           
        self._list = list                                                                                                
                                                                                                                        
    def shuffle(self):                                                                                                  
        for i in range(0, len(self._list)):                                                                                  
            random = randrange(0, len(self._list))
            self._list.insert(i, self._list.pop(random))
                                                                                                                        
    def mergeSort(self):
        self._list = self._split(self._list)

        while(len(self._list) > 1):
            r = []; i = 0

            while(i < len(self._list)):
                left = self._list[i:i+1]; 
                right = self._list[i+1:i+2]

                r.append(self.merge(left[0], right[0] if(len(right) > 0) else []))
                i += 2
            self._list = r
        
        self._list = [] if(len(self._list) == 0) else self._list[0]

    def merge(self, left, right): 
        merge = []

        while(len(left) > 0 or len(right) > 0): 
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
            a = [list[i]]
            s.append(a)
        return s

    def getList(self):                                                                                                  
        return self._list                                                                                               
                                                                                                                        
a = sortedList([1])                                                                                                      
print(f'original: {a.getList()}')                                                                                                      

a.shuffle()                                                                                                             
print(f'shuffle: {a.getList()}')                    

a.mergeSort()
print(f'sorted: {a.getList()}')                    
