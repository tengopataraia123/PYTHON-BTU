class Health:
    def __init__(self,age,gender,pulsi):
        self.age=age
        self.gender=gender
        self.pulsi=pulsi

    def __str__(self):
        return "{} -ასაკი, {} - სქესი , {} - პულსი".format(self.age,self.gender,self.pulsi)


    def sashualo_sicocxle(self):
        return 2600000000/int(self.pulsi) * 525600

    def max_guliscema(self):
        if self.gender=="f":
            return 226-0.9*self.age
        elif self.gender=="m":
            return 223-0.9*self.age

    def max_guliscema_varjishisas(self,factor):
        return (int(self.max_guliscema())-int(self.pulsi))*int(factor)+int(self.pulsi)

teona=Health(19,"f",90)
print(teona.max_guliscema())
print(teona.sashualo_sicocxle())
print(teona.max_guliscema_varjishisas(0.5))





