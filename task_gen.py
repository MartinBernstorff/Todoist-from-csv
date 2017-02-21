import csv
import datetime

"""
Define
    fi: Input file
    fo: Output file
    fr: Reader object
    fw: Writer object
"""

fi = open("input.csv", mode="r")
fo = open("output.csv", mode="w")  # First clear it
fo = open("output.csv", mode="a")  # Then append from now on
fr = csv.reader(fi, delimiter=",")
fw = csv.writer(fo)

fw.writerow(['TYPE', 'CONTENT', 'PRIORITY', 'INDENT', 'AUTHOR', 'RESPONSIBLE', 'DATE', 'DATE_LANG'])  # Write headers for todoist trasks

###############
## FUNCTIONS ##
###############


def todo_w(content, time=None, priority="4", indent="0", delta=None, date=None, d_pages=None, n_pages=None):
    """
        Todoist-formatted row writer

        args:
            Content: String description of task
            Priority: String [1-4]
            Indent: String [1-4]
            delta: Days from 'date' to task due_date [int]
            time: Task duration in minutes [int]
    """
    if delta != None:
        delta_date = datetime.datetime.strptime(date, "%d/%m") + datetime.timedelta(days=delta)  # Calculate time with delta
        date = datetime.datetime.strftime(delta_date, "%d/%m")

    assert date != None
    assert time != None

    fw.writerow(['task', content + " (" + str(time) + ")", priority, indent, '', '', date, 'dk', time])


####################
## RUN THE SCRIPT ##
####################


for row in fr:
    if fr.line_num == 1:  # Skip first row
        continue

    """
        n_pages: Amount of pages
        d_pages: The interval to study
    """

    category, subject, date, d_pages, n_pages = row

    # Check for empty fields
    assert category != ""
    assert subject != ""

    if category == "K":
        assert n_pages != ""
        assert d_pages != ""

    # Create the tasks
    if category == "F":  # Run this if lecture
        todo_w("Kig gennem forelæsningsslides til {subject} @fokus".format(subject=subject), priority=3, delta=-1, date=date, time=3)
        todo_w("Lav flashcards af forelæsningsnoter i {subject} @fokus".format(subject=subject), priority=2, delta=1, date=date, time=15)
    elif category == "H":  # Run this if class
        todo_w("Gennemgå noter til {subject} @fokus".format(subject=subject), priority=3, delta=1, date=date, time=10)
    elif category == "K":  # Run this if chapter
        time = int(n_pages) * 7
        todo_w("Læs og tag essentielle noter til {subject} (pp. {d_pages}) @fokus".format(subject=subject, d_pages=d_pages, time=time), priority=1, delta=-1, date=date, time=time)
