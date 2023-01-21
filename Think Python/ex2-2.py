"""
1. Find the volume of the sphere with a radius of 5, using the equation (4/3)*pi*(r^3)
2. suppose the cover price of a book is $24.95, but bookstores get 40% discount. Shipping costs $3 for the first copy and $0.75 cents for each additional copy.
    What is the total wholesale cost for 60 copies?
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time
    do I get home for breakfast?
"""
import math

radius = 5
volume = (4 / 3) * math.pi * (radius ** 3)
print(f"\nThe volume of a shere with a radius of 5 is: {volume}.\n")

book = 24.95
discount = book * 0.6
nbooks = 60
shipping = ((nbooks - 1) * .75) + 3
booktotal = (nbooks * discount) + shipping
print(f"The wholesale price of 60 books plus shipping is: ${round(booktotal, 2)}\n")

easyminutetosecond = 8 * 60
easypaceinseconds = easyminutetosecond + 15
milesateasypace = 2
tempominutetosecond = 7 * 60
tempoinseconds = tempominutetosecond + 12
milesattempo = 3
easytotalinseconds = easypaceinseconds * milesateasypace
tempototalinseconds = tempoinseconds * milesattempo
totaltimeinseconds = easytotalinseconds + tempototalinseconds
totaltimeinminutes = totaltimeinseconds / 60
print(f"Total run time in minutes {totaltimeinminutes}.\n")