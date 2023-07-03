def avg(par1, par2):
    try:
        return(par1 + par2) / 2
    except TypeError:
        return("Please use two numbers as parameters")