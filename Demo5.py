scores={'eng':[11,21,31],
	'math':[12,22,32],
	'scie':[13,23,33]}
student=['bob','rob','ram']

#new_dict={'bob':{'eng':11,'math':12,'scie':31},
#	   'rob':{'eng':12,'math':22,'scie':32},
#	   'scie':{'eng':13,'math':23,'scie':33}}

subjects=list(scores.keys())
new_dict={}
i=0
for st in student:
    val={}
    for sub in subjects:
         val.update({sub:scores[sub][i]})
    i+=1
    new_dict.update({st:val})

print(new_dict)
