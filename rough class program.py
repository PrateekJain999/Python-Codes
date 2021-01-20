class STUDENT:
    NAME="Prateek"
    def __init__(self,NAME,__CLASS,UID):
       self.NAME=NAME
       self.__CLASS=__CLASS
       self.UID=UID

    def Getdata(self,obj):
       print(self.NAME)
       print(self.__CLASS)
       print(self.UID)
       print(obj.NAME)
       print(obj.__CLASS)
       print(obj.UID)

S=STUDENT("A","B","C")
S.Getdata(S.Getdata(S))

