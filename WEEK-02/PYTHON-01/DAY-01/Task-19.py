#Print the current date and time.

import datetime

print(f"Current date and time : {datetime.datetime.now()}\nCurrent date : {datetime.date.today()}\nCurrent time : {datetime.datetime.now().strftime('%H:%M:%S')}")