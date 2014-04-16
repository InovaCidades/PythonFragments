#Similar to the last exercise, print the current time in the pretty form of hh:mm:ss.

#Change the string that you are printing so that you have a : character in between the %s placeholders.
#Change the three things that you are printing from month, day, and year to now.hour, now.minute, and now.second.

from datetime import datetime

now = datetime.now()

print '%s:%s:%s' % (now.hour, now.month, now.second)
