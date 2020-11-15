import sys
def leapyaer(year1):
	if(((year1)%4==0 and (year1)%100!=0) or (year1)%400==0):
		return True
	return False
def ncal(day1,month1,year1):
	monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]
	n1=year1*365+day1  
	for i in range(0,month1-1): 
		n1+=monthDays[i]  
	n1+=year1//4-year1//100+year1//400
	if(month1<=2 and leapyear(year1)):
		n1-=1
	return n1  
def getdifference(day1,day2,month1,month2,year1,year2):
	n1=ncal(day1,month1,year1)  
	n2=ncal(day2,month2,year2)  
	return abs(n2-n1)
def daycal(str1):
	for i in range(len(str1)):
		if(ord(str1[i])>57 or ord(str1[i])<48):
			break
	return i
def yearcal(str1):
	for i in range(len(str1)-1,-1,-1):
		if(ord(str1[i])>57 or ord(str1[i])<48):
			break
	return i
def monthcal4(str1):
	if("-" in str1):
		str1=str1.strip("-")
		month1=int(str1)
	elif("/" in str1):
		str1=str1.strip("/")
		month1=int(str1)
	elif("." in str1):
		str1=str1.strip(".")
		month1=int(str1)
	return month1
def monthcal3(str1):
	if("Sep" in str1):
		month1=9
	elif("Oct" in str1):
		month1=10
	elif("Nov" in str1):
		month1=11
	elif("Dec" in str1):
		month1=12
	else:
		return monthcal4(str1)	
	return month1
def monthcal2(str1):
	if("May" in str1):
		month1=5	
	elif("Jun" in str1):
		month1=6
	elif("Jul" in str1):
		month1=7
	elif("Aug" in str1):
		month1=8
	else:
		return monthcal3(str1)
	return month1
def monthcal1(str1):
	if("Jan" in str1):
		month1=1
	elif("Feb" in str1):
		month1=2
	elif("Mar" in str1):
		month1=3
	elif("Apr" in str1):
		month1=4
	else:
		return monthcal2(str1)
	
	return month1
def main():
	flg1=0
	if(len(sys.argv)==2 and (sys.argv[1][0]=="M" or sys.argv[1][0]=="m")):
		flg1=1
	f=open("date_calculator.txt",'r')
	str1=f.readline()
	str2=f.readline()
	str1=str1.strip()
	str2=str2.strip()
	i1=daycal(str1)
	i2=daycal(str2)
	day1=int(str1[:i1])
	day2=int(str2[:i2])
	str1=str1[i1:]
	str2=str2[i2:]
	i1=yearcal(str1)
	i2=yearcal(str2)
	year1=int(str1[i1+1:])
	year2=int(str2[i2+1:])	
	str1=str1[:i1+1]
	str2=str2[:i2+1]	
	month1=monthcal1(str1)
	month2=monthcal1(str2)
	if(flg1==1):
		month1,day1=day1,month1
		month2,day2=day2,month2
	diff=getdifference(day1,day2,month1,month2,year1,year2)	
	f1=open("output.txt","w")
	f1.write("Day Difference: {0} Day".format(diff))
main()
