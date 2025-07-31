def devide(total_hrs, effort):
    quo = total_hrs // effort
    rem = total_hrs % effort
    return quo, rem

total_hrs = int(input("enter the total hrs to complete the task: "))
effort = int(input("enter the daily effort: "))

days, hrs     = devide(total_hrs, effort)
weeks, days   = devide(days, 7)
months, weeks = devide(weeks, 4)
years, months = devide(months, 12)


if hrs == 0:
    print(years, "years", months, "months", weeks, 
    "weeks", days, "days", "required to complete the task" )
elif days == 0:
    print(years, "years", months, "months", weeks, 
    "weeks", hrs, "hrs required to complete the task" )
elif weeks == 0:
    print(years, "years", months, "months", days, "days", 
            hrs, "hrs required to complete the task" )
elif years == 0:
    print(months, "months", weeks, 
    "weeks", days, "days", hrs, "hrs required to complete the task" )
else:
    print(years, "years", months, "months", weeks, 
    "weeks", days, "days", hrs, "hrs required to complete the task" )
