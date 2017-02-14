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


def todo_w(content, priority="4", indent="0", delta=None, date=None, d_pages=None, n_pages=None):
    """
        Todoist-formatted row writer

        args:
            Content: String description of task
            Priority: String [1-4]
            Indent: String [1-4]
            delta: Int delta for task due_date in days from date
    """
    if delta != None:
        delta_date = datetime.datetime.strptime(date, "%d/%m") + datetime.timedelta(days=delta)  # Calculate time with delta
        date = datetime.datetime.strftime(delta_date, "%d/%m")

    assert date != None

    if time != None:
        fw.writerow(['task', content, priority, indent, '', '', date, 'dk', time])
    else:
        fw.writerow(['task', content, priority, indent, '', '', date, 'dk'])

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
        time = 5
        todo_w("Gennemgå noter til forelæsning om {subject} og lav flashcards af det (5) @fokus".format(subject=subject), priority=2, delta=1, date=date)
        todo_w("Gennemgå forelæsningsslides til {subject} (5) @fokus".format(subject=subject), priority=3, delta=2, date=date)
    elif category == "H":  # Run this if class
        pass
    elif category == "K":  # Run this if chapter
        time = int(n_pages) * 5
        todo_w("Læse og lave løbende flashcards til {subject} (pp. {d_pages}) ({time}) @fokus".format(subject=subject, d_pages=d_pages, time=time), priority=1, delta=-1, date=date)
