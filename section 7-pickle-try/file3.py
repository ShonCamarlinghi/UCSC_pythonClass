def inv(a,b):
    c = 0
    d = 0
    try:
        c = 1.0/a
        d = 1.0/b
    except ZeroDivisionError:
        print "Either a or b is zero"
        print "this is raised in file3.py"
        raise ZeroDivisionError("One or more numbers is zero.")
    return (c,d)

def insum(c,d):
    e = c + d
