def test():
    print ("Hello World")
test()

def abc(a):
    print(a+10)
abc(10)#parameterized function

#optional parameter
def getCountryName(name="India"):
    print(name)

getCountryName()
getCountryName("UK")
getCountryName(100)

def getNames(list):
    for x in list:
        print(x)

names=["Java","Python","DotNet"]
getNames(names)

def sum(a,b):
    c= a+b
    return c
s1= sum(10,20)
print(s1)

def login(username,password):
    print("login with %s and %s" %(username,password))
login("abbf","aas")