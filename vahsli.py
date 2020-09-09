data = [
    {
        "author": "George R. R. Martin",
        "title": "A Game of thrones",
        "avaliable": True,
        "genre": ["political-novel", "fantasy"]
    },
    {
        "author": "George R. R. Martin",
        "title": "Fire & Blood",
        "avaliable": False,
        "genre": ["fantasy"]
    },
    {
        "author": "J. R. R. Tolkien",
        "title": "The fLord of the Rings",
        "avaliable": True,
        "genre": ["fantasy", "adventure-fiction"]
    },
    {
        "author": "J. R. R. Tolkien",
        "title": "The Hobbit",
        "avaliable": False,
        "genre": ["fantasy", "adventure-fiction", "childrens-literature"]
    }
]
sia=[]
book=input("romeli wigni ginda??? ")
for i in data:
    if book==i["title"] and i["avaliable"]==True:
        rezerv=input("ginda dagirezervo, mitxari ki an ara ?? ")
        if rezerv=="ki":
            i["avaliable"]=False
        else:
            print("okaaay")
    elif book==i["title"] and i["avaliable"]==False:
        another_books=input("ginda naxo sxva wigni romelic igive janrisaa/ damiwere an ki an ara???")
        if another_books=="ki":
            for k in data:
                for value in k.values():
                    if k["genre"]==value:
                        print(k["title"])

