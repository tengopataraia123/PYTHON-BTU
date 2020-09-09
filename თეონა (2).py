class book:
    def __init__(self,name,price,amount=1):
        self.__name=name
        self.__price=price
        self.__amount=amount

    def __str__(self):
        return "წიგნის სათაური {},ფასი-{} ლარი ,დარჩენილია{} ცალი ".format(self.__name,self.__price,self.__amount)
    def get_name (self):
        return self.__name
    def set_name(self,text):
        self.__name=text
    name=property(get_name,set_name)
    def sell(self,question):
        question=int(input("რამდენი წიგნი გინდა?"))
        if question<self.__amount:
            self.__amount=self.__amount-question
            print("გვაქვს საკმარისი რაოდენობა")
        elif question>self.__amount:
            print("არ გვაქვს საკმარისი წიგნის რაოდენობა")
    @staticmethod
    def bonus(number):
        return number/250


obj1=book("harry potter",25,2)
print(obj1.name)
obj1.name="witelquda"
print(obj1.name)
print(obj1.sell(1))

print(book.bonus(500))




