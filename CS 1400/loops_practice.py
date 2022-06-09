
total = 0
count = 0
while True:
  if count > 100:
    break
  else:
    total = total + count
    count += 1
print(total)



# import turtle

# t = turtle.Turtle()

# for outer_looop in range(4):
#     for inner_loop in range(4):
#         t.forward(50)
#         t.rt(90)
#     t.forward(100)
# for last_loop in range(4):
#     t.forward(50)
#     t.rt(90)

# turtle.mainloop()



constant = 4
number = 1
while constant > 0:
    while number < 6:
        print("." * constant, end = "")
        print(number)
        constant -= 1
        number += 1




for num in range(1,6):
    for dots in range(5-num, 0, -1):
        print(".", end = "")
    print(num)
