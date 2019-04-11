from datetime import datetime


def time_is():
    return("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))


def date_is():
    return("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'))


def day_is ():
    return("The day is " + datetime.strftime(datetime.now(), '%A'))
