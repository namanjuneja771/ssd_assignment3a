import json
f=open("org.json",)
data=json.load(f)
dictionary1={}
dictionary1[data["L0"][0]["name"]]=[]
for i in data.keys():
	if(i=="L0"):
		continue
	for j in range(len(data[i])):
		dictionary1[data[i][j]["name"]]=[data[i][j]["parent"]]
		dictionary1[data[i][j]["name"]].extend(dictionary1[data[i][j]["parent"]])
emp1,emp2=map(str,input().split())
if(emp1==data["L0"][0]["name"] or emp2==data["L0"][0]["name"]):
	print("not found")
else:
	for i in dictionary1[emp1]:
		if(i in dictionary1[emp2]):
			print("{0} is the common leader".format(i))
			print("{0} is {1} levels below the leader".format(emp1,dictionary1[emp1].index(i)+1))
			print("{0} is {1} levels below the leader".format(emp2,dictionary1[emp2].index(i)+1))
			break

