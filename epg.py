import datetime
import string
import math
def ToDay():
    global year
    year = datetime.datetime.now().year
    global month
    month = '%02d' % datetime.datetime.now().month
    global day
    day = '%02d' % datetime.datetime.today().day
    global hour
    hour = '%02d' % datetime.datetime.now().hour
    global minute
    minute = '%02d' % datetime.datetime.now().minute
    global second
    second = '%02d' % datetime.datetime.now().second
    global numbers
    numbers = str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + "00"
ToDay()
def DoubleDigit(Integer):
    return "%02d"%Integer
def PlusOneDay():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    global numbers
    if day is 30:
        day = DoubleDigit(0)
    else:
        day = DoubleDigit(day + 1)
    month = DoubleDigit(month)
    numbers = str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + "00"
def RetPlusOneDay():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    global numbers
    if day is 30:
        day = DoubleDigit(0)
    else:
        day = DoubleDigit(day + 1)
    month = DoubleDigit(month)
    return str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + "00"
PlusOneDay()
print numbers
PlusOneDay()
print numbers
DoubleDigit(8)

def ABC1():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    i = 0
    Program = []
    for i in range(0, 365):
        Program.append('<programme start="' + str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + '00 -0400" stop=' + RetPlusOneDay() + '00 -0400" channel="ABCN1"><title lang="en">Now on ABC News</title><category lang="en">News</category></programme>')
        i = i + 1
        print "%" + str(round(float(i)/365*100, 1)) + " of ABC News Digital 1 Schedule Complete."
    return Program
ABC1 = ABC1()
def ABC2():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    i = 0
    Program = []
    for i in range(0, 365):
        Program.append('<programme start="' + str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + '00 -0400" stop=' + RetPlusOneDay() + '00 -0400" channel="ABCN2"><title lang="en">Regularly Scheduled Programming</title><category lang="en">News</category></programme>')
        i = i + 1
        print "%" + str(round(float(i)/365*100, 1)) + " of ABC News Digital 2 Schedule Complete."
    return Program
ABC2 = ABC2()
def ABC3():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    i = 0
    Program = []
    for i in range(0, 365):
        Program.append('<programme start="' + str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + '00 -0400" stop=' + RetPlusOneDay() + '00 -0400" channel="ABCN3"><title lang="en">Regularly Scheduled Programming</title><category lang="en">News</category></programme>')
        i = i + 1
        print "%" + str(round(float(i)/365*100, 1)) + " of ABC News Digital 3 Schedule Complete."
    return Program
ABC3 = ABC3()
def ABC4():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    i = 0
    Program = []
    for i in range(0, 365):
        Program.append('<programme start="' + str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + '00 -0400" stop=' + RetPlusOneDay() + '00 -0400" channel="ABCN4"><title lang="en">Regularly Scheduled Programming</title><category lang="en">News</category></programme>')
        i = i + 1
        print "%" + str(round(float(i)/365*100, 1)) + " of ABC News Digital 4 Schedule Complete."
    return Program
ABC4 = ABC4()
def ABC5():
    global year
    year = int(year)
    global month
    month = int(month)
    global day
    day = int(day)
    global hour
    hour = int(hour)
    global minute
    minute = int(minute)
    global second
    second = int(second)
    i = 0
    Program = []
    for i in range(0, 365):
        Program.append('<programme start="' + str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + '00 -0400" stop=' + RetPlusOneDay() + '00 -0400" channel="ABCN5"><title lang="en">Regularly Scheduled Programming</title><category lang="en">News</category></programme>')
        i = i + 1
        print "%" + str(round(float(i)/365*100, 1)) + " of ABC News Digital 5 Schedule Complete."
    return Program
#File = open('workfile', 'w')
Filee = '<?xml version="1.0" encoding="utf-8" ?><!DOCTYPE tv SYSTEM "http://www.teleguide.info/download/xmltv.dtd"><tv generator-info-name="TVH_W/0.751l" generator-info-url="http://www.teleguide.info/"><channel id="300093"><display-name lang="en">France 24</display-name></channel><channel id="ABCN1"><display-name lang="en">ABC News Digital 1</display-name></channel><channel id="ABCN2"><display-name lang="en">ABC News Digital 2</display-name></channel><channel id="ABCN3"><display-name lang="en">ABC News Digital 3</display-name></channel><channel id="ABCN4"><display-name lang="en">ABC News Digital 4</display-name></channel><channel id="ABCN5"><display-name lang="en">ABC News Digital 5</display-name></channel>'
i = 0
for object in ABC1:
    Filee = Filee + ABC1[i]
    i = i + 1
