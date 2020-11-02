import sys
def getdifference(day1,day2,month1,month2,year1,year2):
	n1=year1*365+day1  
	for i in range(0,month1-1): 
		n1+=monthDays[i]  
	n1+=year1//4-year1//100+year1//400
	if(month1<=2 and (((year1)%4==0 and (year1)%100!=0) or (year1)%400==0)):
		n1-=1  
	n2=year2*365+day2  
	for i in range(0,month2-1): 
		n2+=monthDays[i]  
	n2+=year2//4-year2//100+year2//400
	if(month2<=2 and (((year2)%4==0 and (year2)%100!=0) or (year2)%400==0)):
		n2-=1  
	return abs(n2-n1)
flg1=0
if(len(sys.argv)==2 and (sys.argv[1][0]=="M" or sys.argv[1][0]=="m")):
	flg1=1

f=open("date_calculator.txt",'r')
str1=f.readline()
str2=f.readline()
str1=str1.strip()
str2=str2.strip()
day1=""
for i in range(len(str1)):
	if(ord(str1[i])>57 or ord(str1[i])<48):
		str1=str1[i:]
		break
	day1+=str1[i]
day1=int(day1)
day2=""
for i in range(len(str2)):
	if(ord(str2[i])>57 or ord(str2[i])<48):
		str2=str2[i:]
		break
	day2+=str2[i]
day2=int(day2)
year1=""
for i in range(len(str1)-1,-1,-1):
	if(ord(str1[i])>57 or ord(str1[i])<48):
		str1=str1[:i+1]
		break
	year1=str1[i]+year1
year1=int(year1)
year2=""
for i in range(len(str2)-1,-1,-1):
	if(ord(str2[i])>57 or ord(str2[i])<48):
		str2=str2[:i+1]
		break
	year2=str2[i]+year2
year2=int(year2)
if("Jan" in str1):
	month1=1
elif("Feb" in str1):
	month1=2
elif("Mar" in str1):
	month1=3
elif("Apr" in str1):
	month1=4
elif("May" in str1):
	month1=5
elif("Jun" in str1):
	month1=6
elif("Jul" in str1):
	month1=7
elif("Aug" in str1):
	month1=8
elif("Sep" in str1):
	month1=9
elif("Oct" in str1):
	month1=10
elif("Nov" in str1):
	month1=11
elif("Dec" in str1):
	month1=12
elif("-" in str1):
	str1=str1.strip("-")
	month1=int(str1)
elif("/" in str1):
	str1=str1.strip("/")
	month1=int(str1)
elif("." in str1):
	str1=str1.strip(".")
	month1=int(str1)
if("Jan" in str2):
	month2=1
elif("Feb" in str2):
	month2=2
elif("Mar" in str2):
	month2=3
elif("Apr" in str2):
	month2=4
elif("May" in str2):
	month2=5
elif("Jun" in str2):
	month2=6
elif("Jul" in str2):
	month2=7
elif("Aug" in str2):
	month2=8
elif("Sep" in str2):
	month2=9
elif("Oct" in str2):
	month2=10
elif("Nov" in str2):
	month2=11
elif("Dec" in str2):
	month2=12
elif("-" in str2):
	str2=str2.strip("-")
	month2=int(str2)
elif("/" in str2):
	str2=str2.strip("/")
	month2=int(str2)
elif("." in str2):
	str2=str2.strip(".")
	month2=int(str2)
monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]
if(flg1==1):
	month1,day1=day1,month1
	month2,day2=day2,month2
diff=getdifference(day1,day2,month1,month2,year1,year2)
f1=open("output.txt","w")
f1.write("Day Difference: {0} Day".format(diff))
