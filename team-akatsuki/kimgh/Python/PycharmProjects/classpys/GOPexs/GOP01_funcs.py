print("=" * 20, "argsfunc", "=" * 20)


def argsfunc(*args):
    i = 0
    for x in args:
        i += 1
    print("argsnum %d" % i)
    print(args)


argsfunc(1, 2, (3, 4, 5))
argsfunc(1, [7, 55], "test", {'a': 1, 'b': 100})

a = 1;
b = (3, 6, 9);
c = {'x': 0, 'y': 99}
argsfunc(a, b, c)

print("=" * 20, "dictsfunc", "=" * 20)


def dictsfunc(**dicts):
    i = 0
    for x in dicts.keys():
        i += 1
    print("keysnum %d" % i)
    print(dicts)


dictsfunc(a=1, b=2, c=3)
dictsfunc(**{'a': 1, 'b': 2, 'c': 3})

print("=" * 20, "returnTuple", "=" * 20)


def return_tuple(x, y, z):
    return x, y, z


print(return_tuple(1, 2, 3))

a, b = (1, 2)
print(a)
print(b)


print("=" * 20, "global_variable", "=" * 20)

var = 987

def func():
    global var
    var = 100
    print(locals())

func()
print(var)

print("=" * 20, "local_variable", "=" * 20)

def local_func():
    var = 100
    print(locals())

local_func()

print("=" * 20, "doubled_func", "=" * 20)

def outter():
    def inner():
        print('inner')
    print(locals())
    inner()

outter()

print("=" * 20, "tripled_func", "=" * 20)

def tres():
    a = 1

    def dos():
        b = 2

        def uno():
            c = 3
            print(a, b, c)

        uno()

    dos()

tres()

print("=" * 20, "generator", "=" * 20)

a = [1, 2, 3, 4, 5]
it = iter(a)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

print("=" * 20, "yield", "=" * 20)

def gen():
    n = 0
    while n <= 10:
        yield n
        n += 1

a = gen()
type(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())