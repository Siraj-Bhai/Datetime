from datetime import *
from pytz import timezone

print("1.Convert Into GMT Timezone And US EST Timezone:")
print("\n")
ist = datetime.now()
print('IST TIME : ',ist)

#to Print GMT Time
gmt = datetime.now(timezone('GMT'))
print('GMT TIME : ',gmt)

# to Print US EST Time
est = datetime.now(timezone('US/Eastern'))
print('US EST TIME : ',est)
print("__________________________________________")

print("2.Add And Subract 5 Hours From Current Date:")
print("\n")
hours=int(input("Enter The No Of Hours : "))
# to add 5 hours
add = ist+timedelta(hours=hours)
print("Current Date: ",ist)
print("After Adding 5 Hours : ",add)
# to subract 5 hours
sub = ist-timedelta(hours=hours)
print("Current Date: ",ist)
print("After Subracting 5 Hours : ",sub)
print("__________________________________________")

print("3.Add And Subract 2 Days From Current Date:")
print("\n")
days=int(input("Enter The No Of Days : "))
# to add 2 days
add = ist+timedelta(days=days)
print("Current Date: ",ist)
print("After Adding 2 Days : ",add)
# to subract 2 days
sub = ist-timedelta(days=days)
print("Current Date: ",ist)
print("After Subracting 2 Days : ",sub)
print("__________________________________________")

print("4.Add And Subract 4 Months From Current Date:")
print("\n")
# no of days per month
days = 30.5
months = int(input("Enter The No Of Months : "))
# to add 4 Months
add = ist+timedelta(days=(days*months))
print("Current Date: ",ist)
print("After Adding 4 Months : ",add)
# to subract 4 Months
sub = ist-timedelta(days=(days*months))
print("Current Date: ",ist)
print("After Subracting 4 Months : ",sub)
print("__________________________________________")

print("5.Subract a Year From Current Date:")
print("\n")
# no of days per year
days = 365.25
years = int(input("Enter The No Of Years : "))
# to subract a year
sub = ist-timedelta(days=(days*years))
print("Current Date: ",ist)
print("After Subracting a Year : ",sub)
print("__________________________________________")

print("6.Convert Current Date Into Unix Format:")
print("\n")
print("Current Date : ",ist)
unix = datetime.timestamp(ist)
print("UNIX Time Is : ",unix)
print("__________________________________________")

print("7.Convert Local Time Into Unix Time And Vice Versa:")
print("\n")
date = input("Enter Date :")
local_time = datetime.strptime(date,"%d-%m-%y")
print(datetime.timestamp(local_time))
unix = float(input("Enter UNIX Timestamp : "))
lt = datetime.utcfromtimestamp(unix)
print(lt)