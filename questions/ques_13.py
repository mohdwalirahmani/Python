# WAP using func to convert Fahrenheit into Celcius
'''
C/5 = (f-32)/9
C = 5*(f-32)/9
f = (C*9)/5 + 32
'''

def F_to_C(F):
    return 5*(F-32)/9

F = float(input("Enter the temp in Fahrenheit: "))
C = F_to_C(F)
print (f"The temp in Celcius is: {round(C,2)}°C")



def C_to_F(C):
    return (C*9)/5 + 32

C = float(input("Enter the temp in Celcius: "))
F = C_to_F(C)
print(f"The temp in Fahrenheit is: {F}°F")