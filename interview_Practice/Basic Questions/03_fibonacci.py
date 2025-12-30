num = int(input())
a,b = 0,1

for _ in range(num):
    print(a, end=" ")       # After printing a, don’t go to a new line, just add a space.
    a,b = b, a+b


'''
new a = old b
new b = old a + old b
Dry Run (n = 5)
Iteration	a (printed) 	b	    After Update (a, b)
1       	0	            1       	a=1, b=1
2       	1           	1       	a=1, b=2
3       	1           	2       	a=2, b=3
4       	2           	3       	a=3, b=5
5       	3           	5       	a=5, b=8
'''