def  powerOfSum (y,x):
    sumOfPower = (x+y)**2
    return sumOfPower

int1 = int(input("give the firt int:"))
int2 = int(input("Give the second int:"))

total = powerOfSum(int1, int2)

print("({0} + {1})*2 = {2}".format(int1, int2, total))
