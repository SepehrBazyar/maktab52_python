#Written by: Sepehr Bazyar
import datetime, jdatetime
frmt = "%Y/%m/%d - %H:%M:%S"
first_datetime = datetime.datetime.strptime(input("YYYY/MM/DD - HH:MM:SS => "), frmt)
second_datetime = datetime.datetime.strptime(input("YYYY/MM/DD - HH:MM:SS => "), frmt)

delta_datetime = abs(second_datetime - first_datetime)
print("Duration Second is: ", int(delta_datetime.total_seconds()), 's', sep = '')