"""
For exercise 2 we will use python as a calculator to calculate:
1. How many seconds in 42 minutes and 42 seconds?
2. How many miles are there in 10 kilometers?
3. If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average pace (time per mile in minutes and seconds)?
4. What is your average speed in miles per hour?
"""
# starting values
minutes = 42
seconds = 42
kilometers = 10

# total seconds in 42 minutes and 42 seconds
totalseconds = (minutes * 60) + seconds

# miles in 10 km
miles = kilometers / 1.609344

# seconds per hour to get percentile of hour
hour = totalseconds / 3600

# hours per mile for pace
hpm = hour / miles
pace = hpm * 3600
# pace minutes
paceminutes = pace // 60
# pace seconds 
paceseconds = pace % 60

# average speed in miles per hour
mph = miles / hour

print(f"\nThere are {totalseconds} seconds in {minutes} minutes and {seconds} seconds.\n")
print(f"{kilometers} kilometers is equal to {round(miles, 2)} miles.\n")
print(f"Your average pace was {paceminutes} minutes and {round(paceseconds, 0)} seconds per mile.\n")
print(f"Your average speed was {round(mph, 2)} miles per hour.\n")
