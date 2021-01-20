obj=open("pk.txt","r")
obj.seek(0)
c=0
for i in obj.read():
    if i==(("a")or("e")or("i")or("o")or("u")):
       c+=1

print("total vowels : ",c)
obj.close()
