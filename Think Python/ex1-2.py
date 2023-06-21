"""
For exercise 2 we will use python as a calculator to calculate:
1. How many seconds in 42 minutes and 42 seconds?
2. How many miles are there in 10 kilometers?
3. If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average pace (time per mile in minutes and seconds)?
4. What is your average speed in miles per hour?
"""

minutes = 42
seconds = 42
kilometers = 10

minutes_to_seconds = minutes * 60
total_seconds = minutes_to_seconds + seconds
total_minutes = total_seconds / 60
total_hours = total_minutes / 60
miles = kilometers / 1.609344
rounded_miles = round(miles, 2)
minutes_per_mile = int(total_minutes // miles)
seconds_per_mile = ((total_minutes / miles) - minutes_per_mile) * 60
rounded_seconds_per_mile = round(seconds_per_mile, 3)
miles_per_hour = miles / total_hours
rounded_miles_per_hour = round(miles_per_hour, 1)

print(f"There are {total_seconds} seconds in {minutes} minutes and {seconds} seconds.")
print(f"There are {rounded_miles} miles in {kilometers} kilometers.")
print(f"Your average pace (minutes per mile) when running a 10 kilometer race in 42 minutes and 42 seconds will be: {minutes_per_mile} minutes and {rounded_seconds_per_mile} seconds per mile.")
print(f"Your average speed will be: {rounded_miles_per_hour} miles per hour.")