import math

def eval_loop():
    while True:
        print("You can mathmatically evaluate an expression with this app. When you are done type 'done' to quit.")
        x = input("Enter the expression to evaluate: ")
        if x == 'done' or x == 'Done':
            break
        else:
            y = eval(x)
            print(y)

eval_loop()