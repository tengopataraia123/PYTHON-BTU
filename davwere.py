books = [
 { "author": "John Doe", "book": { "title": "Getting started with Golang", "rating": 4.2, "category": "programming" } } ,
{ "author": "John Doe", "book": { "title": "Best practices with Reactjs", "rating": 4.4, "category": "front-end" } } ,
 { "author": "Ann Hunter", "book": { "title": "React over Angular", "rating": 4.2, "category": "front-end" } } ,
 { "author": "Ann Hunter", "book": { "title": "Progressive web apps", "rating": 4.1, "category": "front-end" } } ,
 { "author": "David Kviloria", "book": { "title": "I’m terrible at programming", "rating": 2.1, "category": "programming" } }
]

author=input("write authors name ")
for d in books:
    if d["author"]==author:
        print(author)
        print("books by"+ "["+author+"]")
        print("category"+":"+d["book"]["category"])
        print("1) title :"+ d["book"]["title"],d["book"]["rating"])




