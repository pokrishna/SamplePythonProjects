def Chr_count(str1):
    dict1={}
    for n in str1:
        keys=dict1.keys()
        if n in keys:
            dict1[n] +=1
        else:
            dict1[n] =1
    return dict1

