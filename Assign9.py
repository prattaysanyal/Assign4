#question1
class circle():
    def __init__(self,r):
        self.radius=r
    def getarea(self):
        return(3.14*self.radius*self.radius)
    def getcircumference(self):
        return(2*3.14*self.radius)

r1=int(input("enter radius"))
x=circle(r1)
print(x.getarea())
print(x.getcircumference())

#question2
class student():
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def display(self):
        return("name of student is %s and roll is %d"%(self.name,self.roll))
x=input("enter name")
y=int(input("enter roll"))
obj=student(x,y)
print(obj.display())

#question3
class temperature():
    def __init__(self,f,c):
        self.fah=f
        self.cel=c
    def convertfahrenheit(self):
        return("after converting to fehrenheit=",self.cel*9/5+32)
    def convertcelcius(self):
        return("after converting to celcius=",(self.fah-32)*5/9)

x=int(input("enter faherenheit"))
y=int(input("enter celcius"))
obj=temperature(x,y)
print(obj.convertfahrenheit())
print(obj.convertcelcius())

#question4
class moviedetails():
    def __init__(self,m,a,y,r):
        self.movie=m
        self.artist=a
        self.year=y
        self.rating=r
    def display(self):
        return("name of the movie is %s,artist is %s released in year %d with raitng of %d"%(self.movie,self.artist,self.year,self.rating))
    def update(self,new):
        self.movie=new
x=input("enter name of movie")
y=input("enter name of artist")
z=int(input("enter year"))
k=int(input("enter rating"))
obj=moviedetails(x,y,z,k)
print(obj.display())
j=input("enter new movie")
obj.update(j)
print(obj.display())

#question5
class expen():
    def __init__(self,e,s):
        self.exp=e
        self.sav=s
    def display(self):
        return("expenditure is %d and saving is %d"%(self.exp,self.sav))
    def total(self):
        return("total salary is %d"%(self.exp+self.sav))

x=int(input("enter expenditure"))
y=int(input("enter saving"))
obj=expen(x,y)
print(obj.display())
print(obj.total())




        
