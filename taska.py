# class car:
#   def __init__(self,color,model,makeyear,fueltype):
#     self.color=color
#     self.model=model
#     self.makeyear=makeyear
#     self.fueltype=fueltype

#   def sell(self):
#     return "iyideba {} manqana, {} markis, gamoshvebis weli {}, sawvavi {}".format(self.color,self.model,self.makeyear,self.fueltype)

#   def insurance(self):
#     return "{},{} markis manqana gamoshvebuli {} wels, sawvavi {} aris dazgveuli".format(self.color,self.model,self.makeyear,self.fueltype)
#   def rent(self):
#     return "qiravdeba {} manqana, fasi 500$".format(self.color)
#   def buy(self):
#     return "viyidi manqanas {} {} gamoshvehuli {} wels".format(self.color,self.model,self.makeyear)

# cara=car("lurji","bmw","2001","gazi")
# print(cara.color)
# print(cara.buy())


# class rectangle:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
#
#   def perimetri(self):
#     return 2*(self.x+self.y)
#
#   def area(self):
#     return self.x*self.y
#
# objecta=rectangle(5,8)
# print(objecta.area())
# print(objecta.perimetri())


# class cugoebi:
#   def __init__(self,breed,size,age,color):
#     self.breed=breed
#     self.size=size
#     self.age=age
#     self.color=color

#   def eat(self):
#     return "{} cugo chams bevrs".format(self.breed)
#   def sleep(self):
#     return "{} cugoebs chirdebat bevri dzili".format(self.size)
#   def sit(self):
#     return "{} wlis asakshi chem cugos jdomisas fexi stkioda".format(self.age)
#   def run(self):
#     return "{} cugo ufro swrafia vidre sxvebi".format(self.color)

#class mydate:
# def __init__(self,day,month,year):
#     self.day=day
#     self.month=month
#     self.year=year
#   def __str__(self):
#     return "{}/{}/{}".format(self.day,self.month,self.year)
#   def difference(self,other):
#     return self.month-other.month

#   def howmanydays(self):
#     x=-1
#     days=[]
#     if self.year%4==0:
#       sia=[31,28,31,30,31,30,31,31,30,31,30,31]
#       while x!=self.month-2:
#         x+=1
#         dgeebi=sia[x]
#         days.append(dgeebi)
#         summ=sum(days)+self.day
#         return 365-summ

#     else:
#       sia=[31,29,31,30,31,30,31,31,30,31,30,31]
#       while x!=self.month-2:
#         x+=1
#         dgeebi=sia[x]
#         days.append(dgeebi)
#         summ=sum(days)+self.day
#         return 366-summ


# obj1=mydate(23,2,2020)
# obj2=mydate(30,1,2020)


# cugo=cugoebi("chixvava","patara","3","tetri")

# print(cugo.eat())
# print(cugo.sleep())
# print(cugo.sit())
# print(cugo.run())


# class fraction:
#   def __init__(self,top,bottom):
#     self.top=top
#     self.bottom=bottom
#   def __str__(self):
#     return "{}/{}".format(self.top,self.bottom)
#   def __add__(self,other):
#     if self.bottom==other.bottom:
#       mricxvelebi=self.top+other.top
#       mnishvnelebi=self.bottom
#       return fraction(mricxvelebi,mnishvnelebi)
#     elif self.top/self.bottom==other.top/other.bottom:
#       mricxvelebi=self.top+self.top
#       mnishvnelebi=self.bottom
#       return fraction(mricxvelebi,mnishvnelebi)

#     elif other.bottom > self.bottom  and other.bottom%self.bottom==0:
#       mnishvnelebi=other.bottom
#       mricxvelebi=other.top+self.top*other.bottom/self.bottom
#       return fraction(mricxvelebi,mnishvnelebi)

#     elif self.bottom> other.bottom and self.bottom%other.bottom==0:
#       mnishvnelebi=self.bottom
#       mricxvelebi=self.top+other.top*self.bottom%other.bottom
#       return fraction(mricxvelebi,mnishvnelebi)

#     else:
#       mnishvnelebi=self.bottom*other.bottom
#       mricxveleli1=self.bottom*other.bottom/self.bottom+self.top
#       mricxveli1i2=other.bottom*self.bottom/other.bottom+other.top
#       mricxvelebi=mricxveleli1+mricxveli1i2
#       return fraction(mricxvelebi,mnishvnelebi)


# ricxvi=fraction(1,5)
# num=fraction(2,7)

# print(num+ricxvi)

