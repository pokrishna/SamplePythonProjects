a='123456789'
b='abc'
c='abcdefgh'
def Merge_str():
    
    merge=[]
    for i in range(len(a)):
       result = ""
       if len(b) > i:
             result=result+b[i]
       if len(c) > i:
            result=result+c[i]
       result=result+a[i]
       merge.append(result)
    print(",".join(merge))

