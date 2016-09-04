'''Unpacking a Sequence into Separate Variables
Problem
    You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
Solution
    You can unpack any iterable or sequence in variables using simple assignment operator.
'''

p = (4,5,6,7)
a,b,c,d = p
print(a)
print(b)
print(c)
print(d)

q = [1,2,3,(4,5,6)]
w,x,y,z = q
print (w)
print (x)
print (y)
print (z)

'''
This works with any iterable like strings
'''
s = 'Hello'
f,g,h,i,j = s

print (f)
print (g)
print (h)
print (i)
print (j)
