class currency:
    lari={"USD":1/2,"EURO":1/4}
    def __init__(self,value,unit="GEL"):
        self.value=value
        self.unit=unit

    def __str__(self):
        return str(self.value/1)+" "+self.unit

    def ChangeTo(self,valuta):
        for k,v in currency.lari.items():
          if k==valuta:
            return self.value*v
          else:
            pass


    def __add__(self,other):
        if isinstance(other,currency):
          if other.unit==self.unit:
            summa=self.value+other.value
          else:
            summa=self.value+other.ChangeTo(other.unit)
        else:
          summa=self.value+other
        return summa

    def __mul__(self,other):
        try:
          return self.value*other
        except TypeError :
          print("გამრავლება სრულდება რიცხვებზე")

    def __gt__(self,other):
        if self.unit==other.unit:
            if self.value>other.value:
                return True
            else:
                return False
        else:
            if self.unit==other.ChangeTo(other.unit):
                if self.value > other.ChangeTo(other.unit):
                    return True
                else:
                    return False



f1=currency(500)
f2=currency(200)
print(f1.__add__(90))
print(f1.ChangeTo("EURO"))
print(f1.__add__(f2))
print(f1*5)
print(f1.__gt__(f2))


