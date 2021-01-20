a=eval(input("enter the no to check it is armstrong or not :"))
res=0
c=a
while a>0:
    r=a%10
    a=a//10
    res=res+r*r*r

if(res+r*r*r==res):
    print("it is a armstrong no")
else:
    print("it is not a armstrong no")
