import salat
from datetime import date
import pytz
import tabulate


# set up calculation methods
pt = salat.PrayerTimes(salat.CalculationMethod.MWL, salat.AsrMethod.STANDARD)

# Date Today
date = date.today()

# using ZH
longitude = 47.3766 # degrees East
latitude = 8.5326 # degrees North
eastern = pytz.timezone('Europe/Zurich')

# calculate times
prayer_times = pt.calc_times(date, eastern, longitude, latitude)

# print in a table
table = [["Name", "Time"]]
for name, time in prayer_times.items():
    readable_time = time.strftime("%m/%d/%Y, %I:%M:%S %p %Z")
    table.append([name, readable_time])
print(tabulate.tabulate(table, headers='firstrow'))
