#On a new line, print now.year. Make sure you do it after setting the now variable!
#Then, print out now.month.
#Finally, print out now.day.

from datetime import datetime

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print current_year
print current_month
print current_day
