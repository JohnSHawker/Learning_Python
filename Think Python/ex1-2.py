"""
For exercise 2 we will use python as a calculator to calculate:
1. How many seconds in 42 minutes and 42 seconds?
2. How many miles are there in 10 kilometers?
3. If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average pace (time per mile in minutes and seconds)?
4. What is your average speed in miles per hour?
"""
minutes = int(input("Minutes > "))
seconds = int(input("Seconds > "))
kilometers = int(input("Kilometers > "))

mintosec = minutes * 60
totalseconds = mintosec + seconds
kilotomile = kilometers / 1.609344
secpermile = kilotomile / totalseconds


print(f"There are {totalseconds} seconds in {minutes} minutes and {seconds} seconds.")
print(f"There are {kilotomile} miles in {kilometers} kilometers")
