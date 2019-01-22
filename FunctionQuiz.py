X = 'Spam'
def func0():
    print(X)

def func1():
    X = 'NI!'
    
#func1()
#print(X)

def func2():
    X = 'NI'
    print(X)
    
#func2()
#print(X)

def func3():
    global X
    X = 'NI'

#func3()
#print(X)

X = 'Spam'
def func4():
    X = 'NI'
    def nested():
        print(X)
    nested()
func4()
print(X)
