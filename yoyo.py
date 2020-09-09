word="harry potter 34"
dicta={}
def capitalaize(sityva):
    lista=sityva.split(" ")
    dasabrunebeli=""
    sia=[]
    ricxvebi=[]
    for i in lista:
        if i.isalpha():
            sia.append(i)
        else:
            ricxvebi.append(i)
    x=0
    for k in sia:
        x+=1
        dicta["found"]=x
        dasabrunebeli+=k
        dasabrunebeli+=" "

    print(dicta)
    print(dasabrunebeli)



capitalaize(word)