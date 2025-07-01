#Avery Sledz
#4-1 lab
#6-25-25
def ftoc(temper):
    c_temp = (temper * 1.8) +32
    print (f'The current temperature is {temper} fahrenheit this temperature in celsius is {c_temp}:')

def ctof(temper):
    f_temp = (temper - 32) * .556

    return(f_temp) 

def main():
    
    temp = float(input("what is the current temperature? "))
    deg = (input("Did you enter the tempurature in (c)elsius or (f)ahrenheit "))
    if deg == "c":
       c_temp = ctof(temp)
       print(f'The current temperature is {temp} celsius this temperature in fahrenheit is {c_temp}:')


    elif deg == "f":
        ftoc(temp)
    else:
        print("Invalid input, please try again!")
  
main()
