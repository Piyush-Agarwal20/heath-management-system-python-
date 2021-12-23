#  DATE : 21/06/pyt

# health management system
print("WHOSE DIET YOU WANT TO LOCK 1.PIYUSH 2.DIMPLE 3.PINKY 4.GOPAL")
i= int(input())
print("WHAT YOU WANT TO LOCK 1.EXERCIE 2.DIET")
i1= int(input())


def getdate ():
    import datetime
    return datetime.datetime.now()
i=str(getdate())

def ent_data(j,i):
   f=open(j,"a")
   t3=input()
   f.write("\n")
   f.write(i)
   f.write("\t")
   f.write(t3)
   f.close()
   print("successfully entered")

print("ENTER THE NAME OF CLIENT WHOSE DIET PLAN YOU WANT TO update ",end=(" "))
print("1.d FOR DIMPLE 2.p FOR PIYUSH 3.g FOR GOPAL 4.k FOR kritika")
t=input()
print("WHAT DO YOU WANNA UPDATE  type : 1) 1 for EXERCISE 2) 2 for food ")
t2=int(input())

def calllist(a,b):
    d1= {"d":{1:"F:\python\pythonprogramming\list\\files\dimpleE.txt",2:"F:\python\pythonprogramming\list\\files\dimplef.txt"},
    "p":{1:"F:\python\pythonprogramming\list\\files\piyushe.txt",2:"F:\python\pythonprogramming\list\\files\piyushf.txt"},
    "g":{1:"F:\python\pythonprogramming\list\\files\gopale.txt",2:"F:\python\pythonprogramming\list\\files\gopalf.txt"},
    "k":{1:"F:\python\pythonprogramming\list\\files\kritikae.txt",2:"F:\python\pythonprogramming\list\\files\kritikaf.txt"}
    }
    return d1[a][b]
j=calllist(t,t2) 
print("enter 1 if you want to retrieve the data  or enter 0 if you want to eneter data ")
t4=int(input())

if t4==0:
 if t2==1:
      print("type name of the exercise and no of repetition")
 else:
      print("Mention the name of food and quantity")
 ent_data(j,i)

elif t4==1:
    k=open(j)
    print(k.read())
    k.close()
