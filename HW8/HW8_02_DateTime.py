#Written by: Sepehr Bazyar
import datetime, jdatetime
frmt = "%Y/%m/%d - %H:%M:%S"
first_datetime = datetime.datetime.strptime(input("YYYY/MM/DD - HH:MM:SS => "), frmt)
second_datetime = datetime.datetime.strptime(input("YYYY/MM/DD - HH:MM:SS => "), frmt)

delta_datetime = abs(second_datetime - first_datetime)
print("\nDuration Second is: ", int(delta_datetime.total_seconds()), 's\n', sep = '')

first_jdate = jdatetime.GregorianToJalali(first_datetime.year, first_datetime.month, first_datetime.day)
second_jdate = jdatetime.GregorianToJalali(second_datetime.year, second_datetime.month, second_datetime.day)
#using walrus operator for simultaneous assigmenting and printing(unpack jalali date list)
print(first_datetime.date(), '=', first_jalali := jdatetime.date(*first_jdate.getJalaliList()))
print(second_datetime.date(), '=', second_jalali := jdatetime.date(*second_jdate.getJalaliList()))
