class STUDENT:
    NAME="Prateek"
    def __init__(self):
       self.NAME='PK'
       self.__CLASS="1st"
       self.UID="1"

    def Getdata(self):
       NAME="P"
       print(self.NAME)
       print(self.__CLASS)
       print(self.UID)

S=STUDENT()
S.Getdata()
print(S.NAME)
