import os
fname=input("enter the name")
if os.path.isfile(fname):
    f=open(fname,'r')
    for line in f:
       lcount+= 1
       words+=line.split()
       wcount=wcount+len(words)
       count=count+len(line)
else:
    print("file not found")
print(lcount+" : "+wcount+" : "+count)
