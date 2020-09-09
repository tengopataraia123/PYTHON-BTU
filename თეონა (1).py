# class celsius:
#   def __init__(self,__temperature):
#     self.__temperature=__temperature
#
#   def get_temp(self):
#     return self.__temperature
#   def set_temp(self,text):
#     self.__temperature=text
#   def del_temp(self):
#     del self.__temperature
#   temp=property(get_temp,set_temp,del_temp)
#
#   def sxvaoba(self,other):
#       if self.__temperature>other.__temperature:
#           return self.__temperature-other_temperature
#       else:
#           return other.__temperature-self.__temperature
#
#
#   @staticmethod
#   def farengeiti(c):
#       return f'{9/5*c+32}'
#
#
# obj1=celsius(2)
# print(obj1.temp)
# obj1.temp=4
# print(obj1.temp)
# print(celsius.farengeiti(obj1.temp))
# obj2=celsius(5)
# print(obj1.sxvaoba(obj2))
# del obj1.temp
#

#
# class employee:
#     organizacia="Google"
#     def __init__(self,__name,__age,__salary):
#         self.__name=__name
#         self.__age=__age
#         self.__salary=__salary
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,text):
#         self.__name=text
#     @name.deleter
#     def name(self):
#         del self.__name
#     @property
#     def email(self):
#         return self.__name+"@gmail.com"
#     @email.setter
#     def email(self,new):
#         self.__name=new
#     def xelfasis_gazrda(self,xexe):
#         return self.__salary+xexe
#     @staticmethod
#     def convert_to_usd(lari):
#         return lari/3.1
#     def salary_in_usd(self):
#         return employee.convert_to_usd(self.__salary)
#
#
# obj1=employee("teona",18,500)
#
# print(obj1.name)
#
# print(obj1.salary_in_usd())
# print(obj1.email)
# obj1.name="nino"
# print(obj1.email)

#
# class Bank_Account:
#     def __init__(self,__Account_name,__balance=0):
#         self.__Account_name=__Account_name
#         self.__balance=__balance
#     def get_name(self):
#         return self.__Account_name
#     def set_name(self,xoxo):
#         self.__Account_name=xoxo
#     Accountname=property(get_name,set_name)
#
#     def deposit(self,tanxa):
#         return "თანხის შეტანა დასრულებულია. ამჟამად თქვენ გაქვთ {} ლარი ".format(self.__balance+tanxa)
#
#     def withdraw(self,fuli):
#         return "თანხის გამოტანა შესრულებულია. ამჟამად თქვენ გაქვთ {} ლარი".format(self.__balance-fuli)
# name=input("შეიყვანეთ კლიენტის სახელი და გვარი : ")
# money=int(input("შეიყვანეთ რა თანხა გაქვთ ამჟამად ანგარიშზე : "))
# code=int(input("შეიყვანეთ შესაბამისი კოდი, რომლის შესრულებაც გსურთ, თანხის შეტანა 1 , გამოტანა 2 "))
#
# person=Bank_Account(name,money)
#
# if code==1:
#     shetana=int(input("რა თანხის შეტანა გსურთ? "))
#     print("თანხის შეტანა დასრულდა თქვენ გაქვთ {} ლარი".format(person.deposit(shetana)))
# elif code==2:
#     gamotana=int((input("რა თანხის გამოტანა გსურთ? ")))
#     print("თანხის გამოტანა დასრულდა თქვენ გაქვთ {} ლარი".format(person.withdraw(gamotana)))
#
