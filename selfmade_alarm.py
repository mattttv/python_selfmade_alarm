import time, os, webbrowser, datetime
while(True):
	startTime = datetime.datetime.now();
	if startTime.hour == 23:
		endHour = 0
	else :
		endHour = startTime.hour + 1;
	endTime = datetime.datetime(startTime.year,startTime.month,
		startTime.day,endHour, startTime.minute, startTime.second)
	print("start Time = " + str(startTime))
	print("end Time = " + str(endTime))	
	while (datetime.datetime.now() < endTime):
		minutes_left = int(abs((datetime.datetime.now() - endTime).total_seconds()) / 60)
		print("wait " + str(minutes_left) + " minutes until break")
		time.sleep(1200)
	webbrowser.get('epiphany').open('break_website.html',new=1, autoraise=True)
	print("press key")
	input()

