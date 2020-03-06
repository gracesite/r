'''
source\
  __init__.py  
  ex1.py
  util\
      __init__.py  
      report.py
'''
# file source/util/report.py
class Report:
    def __init__(self, name):
	    self.name = name

    def __str__(self):
        return self.name

# file source/ex1.py 
from util.report import Report

class Ex1:
    def __init__(self):
        pass

    def __str__(self):
        report1 = Report('MyReport')
        print('instantiatoig...', report1)
        return self.__class__.__name__


my = Ex1()
print(my)

# output:
#   from instantiatoig... MyReport
#   Ex1