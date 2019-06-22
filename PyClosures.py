def make_multiplication(n):
    def multiple(x):
        return x * n
    return multiple

def Closure_fun():
    def nested_fun():
        print("welcome to closure")
    return nested_fun

def closureFunc(n):
    def nestedFunc():
        print("welcome to Closures")
        print("you have sent argument %d + 10=%d"%(n,n+10))
    return nestedFunc

def closureFun3(sum):
    def nestedFunc():
         print("welcome to Closure")
         print("you have sent arguments %s " %sum)
    return nestedFunc

