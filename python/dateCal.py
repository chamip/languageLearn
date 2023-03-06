from datetime import date

startDay = date(2021, 7, 11)
now = date.today()
totalDays = now - startDay
print("Total days we have been together is", totalDays.days)