class Person:
    def __init__(self,name,deposit=1000,loan=0): #loan - სესხი
        self.name=name
        self.deposit=deposit
        self.loan=loan

    def __str__(self):
        return "მომხმარებელი- {}, დეპოზიტი {}, სესხი {}".format(self.name,self.deposit,self.loan)

class House:
    def __init__(self,id,price,owner,status):
        self.id=id
        self.price=price
        self.status=status
        self.owner=owner

    def sell(self,myidveli,number=None):
        if number is not None:
            #ვერ მივხვდი როგორ გინდოდათ ანუ ჯერ ფული გადაეხადა და დეპოზიტი რო დაერიცხებოდა ოუნერში
            #თვითონ ოუნერი შეცვლილიყო თუ ცალ-ცალკე სახელები სტატუსი მოკლე ორივე ნაირად დავწერე და
            # რომელიც უფრო სწორად ჩავთვალე ის დავტოვე "#" ამის გარეშე.
            # self.owner.name=myidveli.name
            # self.owner.deposit=self.owner.deposit+self.price
            # self.status="gayidulia sesxit"
            # myidveli.loan=myidveli.loan+self.price
            # return self.owner.name,self.owner.deposit,self.status,myidveli.loan
            self.owner.deposit = self.owner.deposit + self.price
            self.status = "გაყიდული სესხით"
            self.owner = myidveli
            return "ბინა არის - {} , მისი მფლობელია  ქალბატონი {} ".format(self.status,self.owner.name)

        else:
            # self.owner.deposit=self.owner.deposit + self.price
            # self.status="gayiduli"
            # self.owner.name=myidveli.name
            self.owner.deposit = self.owner.deposit + self.price
            self.status = "გაყიდული"
            self.owner= myidveli


            return "ბინა არის - {} , მისი მფლობელია  ქალბატონი {} ".format(self.status,self.owner.name)




gamyidveli_naziko=Person("ნაზიკო")
myidveli_ciala=Person("ციალა")
bina=House(120,10000,gamyidveli_naziko,"gasayidi")
print(bina.sell(myidveli_ciala,4))
print(str(gamyidveli_naziko.deposit) + " ქალბატონმა ნაზიკომ მიიღო კუთვნილი ფული და აღარაა სახლის პატრონი ")