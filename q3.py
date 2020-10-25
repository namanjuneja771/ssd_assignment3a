f=open("employee1.txt",'r')
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
at1="["+at1+"]"
f=open("employee2.txt",'r')
str2=f.readline()
at2=""
last=""
list5=[]
list6=[]
str2=str2[str2.index(":")+1:]
date2=str2[str2.index("'")+1:str2.index(":")-1]
str2=str2[str2.index(":")+1:]
str2=str2.replace("}","")
str2=str2.replace("'","")
str2=str2.replace(" ","")
str2=str2.replace("[","")
str2=str2.replace("]","")
str2=str2.replace("-",",")
str2=str2.replace("\n","")
list2=str2.split(",")
if(list2[0]!="9:00AM"):
	at2+="'9:00AM - "+list2[0]+"'"
	list5.append(540)
	list5.append(60*int(list2[0][:list2[0].index(":")])+int(list2[0][list2[0].index(":")+1:list2[0].index(":")+3]))
if(list2[-1]!="5:00PM"):
	last+=",'"+list2[-1]+" - 5:00PM'"
	list6.append(60*int(list2[-1][:list2[-1].index(":")])+int(list2[-1][list2[-1].index(":")+1:list2[-1].index(":")+3]))
	list6.append(300)
list2=list2[1:]
list2=list2[:len(list2)-1]
for i in range(0,len(list2),2):
	at2+=",'"+list2[i]+" - "+list2[i+1]+"'"
	list5.append(60*int(list2[i][:list2[i].index(":")])+int(list2[i][list2[i].index(":")+1:list2[i].index(":")+3]))
	list5.append(60*int(list2[i+1][:list2[i+1].index(":")])+int(list2[i+1][list2[i+1].index(":")+1:list2[i+1].index(":")+3]))
at2+=last
list5.extend(list6)
at2="["+at2+"]"
hour=float(input())
req=int(hour*60)
list7=[]
for i in list3:
	if(i<540):
		list7.append(i+720)
	else:
		list7.append(i)
list8=[]
for i in list5:
	if(i<540):
		list8.append(i+720)
	else:
		list8.append(i)
i=0
j=0
start=-1
end=-1
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
		break
	if(list7[i+1]>list8[j+1]):
		j+=2
	else:
		i+=2				
f1=open("output.txt","w")
f1.write("Available slot\n")
f1.write("Employee 1:[{0}]\n".format(at1))
f1.write("Employee 2:[{0}]\n".format(at2))
f1.write("Slot duration: {0} hours\n".format(hour))
if(start!=-1 and date1==date2):
	f1.write("{1}'{0}':[".format(date1,"{"))
	q=start//60
	r=str(start%60)
	if(len(r)==1):
		r="0"+r
	if(q>=12):
		f1.write("'{0}:{1}PM - ".format(q-12,r))
	else: 
		f1.write("'{0}:{1}AM - ".format(q,r))
	end=start+req
	q=end//60
	r=str(end%60)
	if(len(r)==1):
		r="0"+r
	if(q>=12):
		f1.write("{0}:{1}PM'".format(q-12,r))
	else: 
		f1.write("{0}:{1}AM'".format(q,r))
	f1.write("]}")
else:
	f1.write("no slot available")
