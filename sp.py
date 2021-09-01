
   def _split(self, m, r): # m is list to be split, r is recursive memory
        max = int(len(m)/2)
        left = m[0:len(m)-max]
        right = m[len(m)-max:len(m)]

        if(len(left) > 1): # depth first
            self._split(left, r)
        if(len(right) > 1):
            self._split(right, r)

        if(len(left) == 1):
            r.append(left)
        if(len(right) == 1):
            r.append(right)

        print("asd" + str(r))

    def split(self, list):
        s = []
        for i in range(0, len(list)):
            a = []
            a.append(list[i])
            s.append(a)
        return s

