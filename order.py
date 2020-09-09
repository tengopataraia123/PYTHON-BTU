def getorder(a):
    from datetime import date
    today = date.today()

    products=[]
    amounts=[]
    prices=[]



    product = input("enter which food u want ")
    amount = int(input("enter amount of ur product"))
    money=input("if u pay in GEL write GEL and if you pay with USD write USD")
    more=input("do you want more products? write yes or no")

    products.append(product)
    amounts.append(amount)
    for i in a:
        if product==i["product"] and int(i["amount"])>amount and today.strftime("%d/%m/%Y")>=i["validity"]:
            for c in i["price"]:
                price=i["price"]
                if c==money:
                    prices.append(price[c])

    if more=="yes":
        for d in range(len(a)-1):
            product = input("enter which food u want ")
            amount = int(input("enter amount of ur product"))
            money = input("if u pay in GEL write GEL and if you pay with USD write USD")

            products.append(product)
            amounts.append(amount)
            prices.append(money)
    elif more=="no":
        print("sooo.....okay")
    for i in range(len(prices)):
        pay=int(amounts[i])*int(prices[i])
        print("you have to pay {}".format(pay))


    user={}

    for b in range(len(products)):
        user[products[b]]=amounts[b]





