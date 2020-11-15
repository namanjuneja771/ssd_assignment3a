import os
def fetchfiles():
	listOfEmployeeFiles=[]	
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	i=1
	while(True):	
		if("Employee"+str(i)+".txt" in files):		
			listOfEmployeeFiles.append("Employee"+str(i)+".txt")
		else:
			break
		i+=1
	return listOfEmployeeFiles		
def avlslots(list1,list3,list4,at1,f1,last):
	for i in range(0,len(list1),2):
		at1+=",'"+list1[i]+" - "+list1[i+1]+"'"
		list3.append(60*int(list1[i][:list1[i].index(":")])+int(list1[i][list1[i].index(":")+1:list1[i].index(":")+3]))
		list3.append(60*int(list1[i+1][:list1[i+1].index(":")])+int(list1[i+1][list1[i+1].index(":")+1:list1[i+1].index(":")+3]))
	at1+=last
	list3.extend(list4)
	if(at1[0]==","):
		at1=at1[1:]
	at1="["+at1+"]"
	list7=[]
	for i in list3:
		if(i<540):
			list7.append(i+720)
		else:
			list7.append(i)
	f1.write("{0}\n".format(at1))
	return list7
def timeinmins(i,f1):
	f=open(i,'r')
	f1.write("{0}:".format(i[:i.index(".")]))
	str1=f.readline()
	at1=""
	last=""
	list3=[]
	list4=[]
	str1=str1[str1.index(":")+1:]
	date1=str1[str1.index("'")+1:str1.index(":")-1]
	str1=str1[str1.index(":")+1:]
	str1=str1.replace("}","")
	str1=str1.replace("'","")
	str1=str1.replace(" ","")
	str1=str1.replace("[","")
	str1=str1.replace("]","")
	str1=str1.replace("-",",")
	str1=str1.replace("\n","")
	list1=str1.split(",")
	if(list1[0]!="9:00AM"):
		at1+="'9:00AM - "+list1[0]+"'"
		list3.append(540)
		list3.append(60*int(list1[0][:list1[0].index(":")])+int(list1[0][list1[0].index(":")+1:list1[0].index(":")+3]))
	if(list1[-1]!="5:00PM"):
		last+=",'"+list1[-1]+" - 5:00PM'"
		list4.append(60*int(list1[-1][:list1[-1].index(":")])+int(list1[-1][list1[-1].index(":")+1:list1[-1].index(":")+3]))
		list4.append(300)
	list1=list1[1:]
	list1=list1[:len(list1)-1]
	return avlslots(list1,list3,list4,at1,f1,last)
def common(list7,list8,list9,req):
	i=0
	j=0
	while(i<len(list7) and j<len(list8)):
		diff1=list7[i+1]-list7[i]
		diff2=list8[j+1]-list8[j]
		if(req>diff1):
			i+=2
			continue
		elif(req>diff2):
			j+=2
			continue	
		elif(list8[j]>=list7[i+1]):
			i+=2
			continue
		elif(list7[i]>list8[j+1]):
			j+=2
			continue
		start=max(list7[i],list8[j])
		end=min(list7[i+1],list8[j+1])
		diff3=end-start
		if(diff3>=req):
			list9.append(start)
			list9.append(end)
		if(list7[i+1]<list8[j+1]):
			i+=2
		elif(list7[i+1]>list8[j+1]):
			j+=2
		else:
			i+=2	
	return list9
def compute(listOfEmployeeFiles,timeInMins,req):
	k=0
	flg=1
	while(k<len(listOfEmployeeFiles)):
		i=0
		j=0
		start=-1
		end=-1
		list7=timeInMins[0]	
		list8=timeInMins[-1]
		list9=common(list7,list8,[],req)
		if(list9==[]):
			flg=0		
			break
		timeInMins=timeInMins[1:len(timeInMins)-1]
		timeInMins.append(list9)
		k+=1
	return list9
def pr(q,r,f1):		
		if(len(r)==1):
			r="0"+r
		if(q>12):
			f1.write("{0}:{1}PM".format(q-12,r))
		elif(q==12):
			f1.write("{0}:{1}PM".format(q,r))	
		else: 
			f1.write("{0}:{1}AM".format(q,r))
def main():
	listOfEmployeeFiles=fetchfiles()
	listOfEmployeeFiles.sort()
	f1=open("output.txt","w")
	f1.write("Available slot\n")
	f2=open("Employee1.txt",'r')
	str5=f2.readline()
	str5=str5[str5.index(":")+1:]
	date1=str5[str5.index("'")+1:str5.index(":")-1]
	timeInMins=[]
	for i in listOfEmployeeFiles:
		timeInMins.append(timeinmins(i,f1))
	hour=float(input())
	req=60*hour
	k=1
	list9=compute(listOfEmployeeFiles,timeInMins,req)
	f1.write("Slot duration: {0} hours\n".format(hour))
	if(len(list9)>0):
		f1.write("{1}'{0}':['".format(date1,"{"))
		start=list9[0]	
		q=int(start//60)
		r=str(int(start%60))
		pr(q,r,f1)		
		f1.write(" - ")
		end=start+req
		q=int(end//60)
		r=str(int(end%60))
		pr(q,r,f1)
		f1.write("']}")
	else:
		f1.write("no slot available")
main()
