#Written by: Sepehr Bazyar
from jdatetime import date, datetime #jalali datetime: date ad datetime to converting
from typing import Generator, Literal #for highlighting input and output functions

def normalize(day: date, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> date: #fixing weekday date
    counter = day
    while counter.weekday() != w_day: #maximum 6 day to fixing
        try: #next day
            counter = date(counter.year, counter.month, counter.day + 1)
        except:
            try: #next month(first day of next month)
                counter = date(counter.year, counter.month + 1, 1)
            except: #next year(first day of first month new year)
                counter = date(counter.year + 1, 1, 1)
    return counter

def weekday_gen(s_day: str, e_day: str, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> Generator:
    start = datetime.strptime(s_day, "%Y/%m/%d").date() #parse datetime from the string
    end = datetime.strptime(e_day, "%Y/%m/%d").date() #convert to date for remove time
    counter = normalize(start, w_day) #find starting day that right weekday
    while counter <= end: #less than for date object is correct comparison
        yield counter.strftime("%d %B %Y") #yield keyword generator(fix formatting)
        try: #7 day later this week day in next week
            counter = date(counter.year, counter.month, counter.day + 7)
        except:
            try: #next month(because maybe 31 or 30 day can't use % operation)
                counter = normalize(date(counter.year, counter.month + 1, 1), w_day)
            except:
                counter = normalize(date(counter.year + 1, 1, 1), w_day)
