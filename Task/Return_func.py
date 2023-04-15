'''def getsum(a,b):
    return a+b

x=getsum(23,54)
def answer():
    print("Sum:",x)

answer()'''

def getdata(id,name):
    return [id,name]

stid=(input('enter the id:'))
stnm=(input("enter the name:"))
x=[id,name]=getdata(stid,stnm)

def printdata():
    print("ID:",x[0])
    print("Name:",x[1])


printdata()