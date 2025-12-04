
def sq(x):
    return x*x

def fun(fx, value):
    return 6 + fx(value)

square = lambda x : x*x     # we use lambda when we don't have to write multiple line of code
avg = lambda x, y, z : (x+y+z)/3

print(square(5))
print(avg(5,10,14))
print(fun(square, 5))       # this will first do square of 5 then add 6 in it, (passing func as a argument)
print(fun(lambda x: x*x, 5))        # same same