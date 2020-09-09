unknown_list = ["toby", "James", "kate", "George", "James", "rick", "Alex", "Jein", "Alex", "Alex", "George", "Jein",
                "kate", "medelin"]

def custom_function(unknown_list):
    dict={}
    for i in unknown_list:

        dict[i]=unknown_list.count(i)

    print(dict)



    for b in unknown_list:
        sia=[]
        a=b.title()
        sia.append(a)
        print(set(sia))

g=["me","me","kata"]
io=custom_function(g)







