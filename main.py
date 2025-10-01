# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi,{name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

hello  = 'kj'
world = 'world'
# name = input('name:')
# print(hello,name, 'you are old')

x = 10
y = 3
print(x%y)

# num = input('Num:')
# print(int(num) - 5)

print(type(hello))
print (world.lower())
print(hello*5)
print(ord('b') > ord('a'))

x = [4, True, 'hi']
x.extend([2,4,1])
print (len(x))
print(x[1])
y = x[:]
print(y)

# for i in range(2,-10,-2):
#     print(i)

l = [2,3,6,1,21,2,3,4,23,231]
for i in l:
    print (i)

sliced  = l[0:8:2]
print (sliced )
print (l[::-1])

x = ()
m = {}
s = {4,43,2,2,2}
print (type(x))
print (type(m))
print (type(s))


# dictionaries
d = {'k': 'kkkkkkk', 'a' : 'aaaaaaa'}
print (d)
print(list(d.keys()))
print(list(d.values()))
# del d['k']
# print(list(d.keys()))
print(list(d.items()))
for k,v in d.items():
    print (k+'dod'+v)

print('aaaaaaaaaaaaaaa')
y = [y*y for y in range(1,10,2)]
print(y)

y = [y for y in range(100) if y%3==0]
print(y)


def func(x, y):
    print('run',x,y)
    return x*x, x**y

a,b = func(3,1)
print (a, b)


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func (1,2,3,4,5, one=0, two = 1)

try:
    x = 7/0
except Exception as e:
    print(e)

x = lambda x: x+5
print (x(2))

x = [1,2,4,62,234,6,31,43,11]
mp = map(lambda i: i*2, x)
print (list(mp))

mp = map(lambda i: i*2 if i%2==0 else None,  x)
print (list(mp))

mp = filter(lambda i: i*2 if i%2==0 else None,  x)
print(list(mp))
