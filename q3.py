import os
listOfEmployeeFiles=[]
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if(f[:8]=="Employee"):
		j=8
		while(ord(f[j])>=48 and ord(f[j])<=57):
			j+=1
		if(f[j:]==".txt"):
			listOfEmployeeFiles.append(f)
listOfEmployeeFiles.sort()
f1=open("output.txt","w")
f1.write("Available slot\n")
timeInMins=[]
for i in listOfEmployeeFiles:
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
	timeInMins.append(list7)
	f1.write("{0}\n".format(at1))

hour=float(input())
req=60*hour
k=1
flg=1
while(k<len(listOfEmployeeFiles)):
	i=0
	j=0
	start=-1
	end=-1
	list7=timeInMins[0]	
	list8=timeInMins[-1]
	list9=[]
	while(i<len(list7) and j<len(list8)):
		diff1=list7[i+1]-list7[i]
		diff2=list8[j+1]-list8[j]
		if(req>diff1):
			i+=2
			continue
		if(req>diff2):
			j+=2
			continue	
		if(list8[j]>=list7[i+1]):
			i+=2
			continue
		if(list7[i]>list8[j+1]):
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
		if(list7[i+1]>list8[j+1]):
			j+=2
		else:
			i+=2	
	if(list9==[]):
		flg=0		
		break
	timeInMins=timeInMins[1:len(timeInMins)-1]
	timeInMins.append(list9)
	k+=1
f1.write("Slot duration: {0} hours\n".format(hour))
if(flg==1):
	f1.write("{1}'{0}':[".format(date1,"{"))
	start=timeInMins[0][0]	
	q=int(start//60)
	r=str(int(start%60))
	if(len(r)==1):
		r="0"+r
	if(q>12):
		f1.write("'{0}:{1}PM - ".format(q-12,r))
	elif(q==12):
		f1.write("'{0}:{1}PM - ".format(q,r))	
	else: 
		f1.write("'{0}:{1}AM - ".format(q,r))
	end=start+req
	q=int(end//60)
	r=str(int(end%60))
	if(len(r)==1):
		r="0"+r
	if(q>12):
		f1.write("{0}:{1}PM'".format(q-12,r))
	elif(q==12):
		f1.write("{0}:{1}PM'".format(q,r))	
	else: 
		f1.write("{0}:{1}AM'".format(q,r))
	f1.write("]}")
else:
	f1.write("no slot available")
