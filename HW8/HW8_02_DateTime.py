#Written by: Sepehr Bazyar
import datetime, jdatetime

frmt = "%m/%d/%Y - %H:%M:%S" #string for format type of date & time parse from user input
first_datetime = datetime.datetime.strptime(input("MM/DD/YYYY - HH:MM:SS => "), frmt)
second_datetime = datetime.datetime.strptime(input("MM/DD/YYYY - HH:MM:SS => "), frmt)

delta_datetime = abs(second_datetime - first_datetime) #calculate difference between two times
print("\nDuration Second: ", int(delta_datetime.total_seconds()), 's\n', sep = '') #to seconds
#GregorianToJalali Convert to Jalali Date and get numbers in tuple and create Jalali Date Object
first_jalali = jdatetime.date(*(jdatetime.GregorianToJalali(first_datetime.year, 
first_datetime.month, first_datetime.day).getJalaliList())) #* for unpacking tuple pass to date
second_jalali = jdatetime.date(*(jdatetime.GregorianToJalali(second_datetime.year, 
second_datetime.month, second_datetime.day).getJalaliList()))
#write my format for output in console print(%B refrence to month full name)
print(first_datetime.date().strftime("%d %B %Y"), ' = ', first_jalali.strftime("%d %B %Y"), '\n',
second_datetime.date().strftime("%d %B %Y"), ' = ', second_jalali.strftime("%d %B %Y"), sep = '')

leap_year, back_forth = 0, 0 #sal kabise va tedad aqab jelo saat
for counter in range(first_jalali.year, second_jalali.year + 1): #loop in years range
    if first_jalali <= jdatetime.date(counter, 1, 1) <= second_jalali: back_forth += 1 #jelo
    if first_jalali <= jdatetime.date(counter, 7, 1) <= second_jalali: back_forth += 1 #aqab
    try: #try for create a object 30 esfand if counter year is a leap year
        intercalary = jdatetime.date(counter, 12, 30)
        if(first_jalali <= intercalary <= second_jalali): leap_year += 1 #if between to dates
    except: pass

print(f"\nNumber of Clock Changes: {back_forth} Times\nNumber of Leap Years: {leap_year}")
