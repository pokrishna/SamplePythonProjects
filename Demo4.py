sg={'cricket':['kri','vis','yesh'],
        'football':['kri','bha','saug'],
        'vallyball':['kri','vis','bhu']}


play=[]
for i in sg.values():
    play.extend(i)

play=set(play)
play=list(play)

new_Dict={}
for p in play:
    pl=[]
    for g in sg.keys():
	if p in sg[g]:
	    pl.append(g)
    new_Dict.update({p:pl})
print(new_Dict)

    	    
	    

