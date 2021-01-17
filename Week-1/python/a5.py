from itertools import groupby
  
def compress(l):
    res = [i[0] for i in groupby(l)] 
    return res