count =0
while(count<10):
    print("Hello World")
    print(count)
    count=count + 1
    #In python with while loop you can use if else condition
num=0
while(num<=3):
    print("Hello WOrld")
    num=num+1
else:
    print("Bye python")

name=["java","c","C#","Dotnwt"]
for i in name:
    print(i)

str = " I love ress"

for i in str:
    print(i)
    print("---------")

    lang =("Eng","Urdi","Hindi","Spanish","Pip")
    for index in range(len(lang)):
        print(lang[index])
        if(lang[index]=="Spanish"):
            print("Spanish is lowest lang")
            break