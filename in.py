def func(a,b):
    try:
        b=b+'A'
        a=b/0
        print(b)
    except ZeroDivisionError:
        print("T")
    finally:
        print("IF")
try:
    func('R',13)
except TypeError:
    print("V")
finally:
    print("OF")
