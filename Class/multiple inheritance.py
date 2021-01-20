# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:52:49 2019

@author: prateek jain
"""
class Person():                  
      def __init__(self, name, idnumber): 
            self.name = name 
            self.idnumber = idnumber 
  
# second parent class       
class Employee():                 
      def __init__(self, salary, post): 
            self.salary = salary 
            self.post = post 
  
# inheritance from both the parent classes       
class Leader(Person, Employee):         
      def __init__(self, name, idnumber, salary, post, points): 
            self.points = points 
            Person.__init__(self, name, idnumber) 
            Employee.__init__(self, salary, post) 
            print(self.salary) 
        
ins = Leader('Rahul', 882016, 'Assistant Manager', 75000, 560)
print(ins.name)


#class ABC1:   
#    def print1(self):
#        print('hi')
#    def print2(self):
#        print('hi')
#
#class ABC2():
#    def print3(self):
#        print('hi')
#    def print4(self):
#        print('hi')
#        
#class ABC3(ABC1,ABC2):
#    def print5(self):
#        print('hi')
#
#
#A1=ABC1()
#A2=ABC2()
#A3=ABC3()
#
#A1.print1()
##A2.print1()
##A2.print2()
#A3.print1()
#A3.print2()
#A3.print3()
#A3.print4()
#A3.print5()
