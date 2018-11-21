import csv
import datetime
import arrow
from ics import Calendar, Event

"""
Define
    fi: Input file (from belastningsfordeling)
    fo: Output file
"""

#####################
# Establish handles #
#####################
c = Calendar()

fi = open("input_cal.csv", mode="r")
fo = open("output.ics", mode="w")  # First clear it

reader = csv.reader(fi, delimiter=',')

###############
## FUNCTIONS ##
###############
def event_w(title, begin, duration):
    """
        Takes:
            Title: str
            Begin: Start-date in arrow format
            Duration: int (minutes)
    """
    e = Event()
    e.name = title
    e.begin = begin
    e.duration = datetime.timedelta(minutes=int(duration))
    c.events.add(e)

####################
## RUN THE SCRIPT ##
####################
i = 1 # Start on the first line

arrow_date = ""

for row in reader:
    day = row[6][0:2]
    month = row[6][3:5]
    duration = row[8]

    if i == 1:
        date = "2018-{}-{} 10:00:00".format(month, day)
        arrow_date = arrow.get(date, 'YYYY-MM-DD HH:mm:ss')

    print("Processing line {i}".format(i=i))
    print("Start_date {}".format(arrow_date))

    content = row[1]

    event_w(content, date, duration)

    arrow_date = arrow_date.replace(minutes=+int(duration))
    print("New start_date {}".format(arrow_date))
    i+=1

fo.writelines(c)

print(c.events)
