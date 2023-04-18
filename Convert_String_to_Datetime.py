# Python Program to Convert String to Datetime.

# Method 1: Using DateTime Module
from datetime import datetime

date = "Jun 27 2001 4:00AM"
print(type(date))

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))


# Method 2: Using Dateutil Module
from dateutil import parser

date_time = parser.parse("Jun 27 2001 4:00AM")
print(type(date_time))
print(date_time)
