sia=[]
lista=[]
while len(sia)!= 50:
    number=int(input("enter number "))
    sia.append(number)

    if sia.index(number) % 2 != 0:
        if number % 2 == 0:
            lista.append(number)
            x=0
            for i in lista:
                x+=1
            print("element is "+ str(i) + " " + "index is"+" " + str(lista.index(i)))
            print("amount is " + str(len(lista)))

