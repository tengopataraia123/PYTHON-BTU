import sqlite3 as sql
conn = sql.connect('market.sqlite')
c = conn.cursor()


result=c.execute("""SELECT * FROM products WHERE amount >=120 """)
for i in result:
    print(i[1])


def amount(num):
    answer=c.execute("""SELECT * FROM products WHERE unit_price<"""+str(num))
    for i in answer:
        print(i[3])

def producti_and_currency(producti, currency):
    c.execute('''SELECT (unit_price/rate) FROM products join currency 
    WHERE product_name="{}" and currency_name="{}" '''.format(producti, currency))
    return c.fetchone()[0]


class Product:
    def __init__(self,id,product_name,amount,unit_price):
        self.id=id
        self.product_name=product_name
        self.amount=amount
        self.unit_price=unit_price

example=Product(123,"lenovo 9",2000,34)
print(example.product_name)
print(example.amount)
print(example.unit_price)
print(example.id)











