def sum(a,b):
    print(f"{a}+{b}={a+b}")
def minuse(a,b):
    print(f"{a}-{b}={a-b}")
def multpilcation(a,b):
    print(f"{a}*{b}={a*b}")
def divison(a,b):
    print(f"{a}/{b}={a/b}")




def choise():
    print("Enter + for sum","Enter - for min.","Enter * for mul.","Enter / for div.")
    c=input("enter your choise:")
    no1=int(input("Enter the number:"))
    no2=int(input("Enter the number:"))
    if c=="+":
        sum(no1,no2)
    elif c=="-":
        minuse(no1,no2)
    elif c=="*":
        multpilcation(no1,no2)
    elif c=="/":
        divison(no1,no2)


choise()