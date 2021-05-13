# Written by: Sepehr Bazyar
from jdatetime import date
from typing import Generator, Literal

def normalize(day: date, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> date:
    counter = day
    while counter.weekday() != w_day:
        try:
            counter = date(counter.year, counter.month, counter.day + 1)
        except:
            try:
                counter = date(counter.year, counter.month + 1, 1)
            except:
                counter = date(counter.year + 1, 1, 1)
    return counter

def weekday_gen(s_day: date, e_day: date, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> Generator:
    counter = normalize(s_day, w_day)
    while counter <= e_day:
        yield counter
        try:
            counter = date(counter.year, counter.month, counter.day + 7)
        except:
            try:
                counter = normalize(date(counter.year, counter.month + 1, 1), w_day)
            except:
                counter = normalize(date(counter.year + 1, 1, 1), w_day)
