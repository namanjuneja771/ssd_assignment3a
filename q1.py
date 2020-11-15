import json
def findparent(list1,dictionary1,emp1):
	for i in dictionary1[emp1]:
		flg2=1	
		for j in list1[1:]:
			if(i not in dictionary1[j]):
				flg2=0
				break
		if(flg2==1):
			ans=i
			break
	p(ans,dictionary1,list1)
def p(ans,dictionary1,list1):
	print("{0} is the common leader".format(ans))
	for j in list1:
		print("{0} is {1} levels below the leader".format(j,dictionary1[j].index(ans)+1))
def check(list1,data,dictionary1):
	flg=0	
	for i in list1:
		if(i==data["L0"][0]["name"]):
			print("Leader not found")
			flg=1
			break
	if(flg==0):
		findparent(list1,dictionary1,list1[0])				
def main():
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
	list1=list(map(str,input().split()))
	if(int(list1[0])+1!=len(list1)):
		print("Incorrect number of users ")
		exit()
	list1=list1[1:]
	emp1=list1[0]
	ans=""
	check(list1,data,dictionary1)	
main()	

