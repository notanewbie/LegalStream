import datetime
year = datetime.datetime.now().year
month = '%02d' % datetime.datetime.now().month
day = '%02d' % datetime.datetime.today().day
hour = '%02d' % datetime.datetime.now().hour
minute = '%02d' % datetime.datetime.now().minute
second = '%02d' % datetime.datetime.now().second
numbers = str(year) + str(month) + str(day) + str(day) + str(hour) + str(second) + "00"
print numbers
#
#File = open('workfile', 'w')
#File.write('<?xml version="1.0" encoding="utf-8" ?><!DOCTYPE tv SYSTEM "http://www.teleguide.info/download/xmltv.dtd"><tv generator-info-name="TVH_W/0.751l" generator-info-url="http://www.teleguide.info/"><channel id="300093"><display-name lang="en">France 24</display-name></channel><channel id="ABCN1"><display-name lang="en">ABC News Digital 1</display-name></channel><channel id="ABCN2"><display-name lang="en">ABC News Digital 2</display-name></channel><channel id="ABCN3"><display-name lang="en">ABC News Digital 3</display-name></channel><channel id="ABCN4"><display-name lang="en">ABC News Digital 4</display-name></channel><channel id="ABCN5"><display-name lang="en">ABC News Digital 5</display-name></channel>')
#
