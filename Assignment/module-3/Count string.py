def count(s):
    s=s.split()
    if len(s)>2 and s[0]==s[-1] :
        print(len(s))

s=("this is string newly made this")

count(s)