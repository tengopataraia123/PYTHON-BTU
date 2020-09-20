import requests
#ვებგვერდების უმეტესობა ჯავასკრიპტს იყენებს, რექუესთი კიდე არ არენდერებს ჯავასკრიპტს
#ამიტო ჯობია სელენიუმი გამოიყენო, თუ მაინდამაინც ბრაუზერი არ გინდა იყოს გახსნილი phantomJS driver შეგიძლია გამოიყენო

#ვაიმპორტებთ რექსუესთს საიტზე წვდომისთვის
from bs4 import BeautifulSoup
#გვჭირდება პარსინგისთვის ბიუთიფულ სუპი BeautifulSoup


url="https://srulad.com/"



connection=requests.get(url)
html=connection.text


soup = BeautifulSoup(html, 'html.parser')


s=soup.find_all("div",{"class":'col-md-4 col-lg-3'})
file=open('srulad_com.csv','w',encoding='utf-8_sig')
head=file.write("თარიღი;სახელი,ჟანრი;IMDB\n")  # <----------

for i in s:
    joina=" "
    tarigi_da_saxeli=i.h2.text.strip()
    tarigi_da_saxeli=tarigi_da_saxeli.split(" ")
    date=tarigi_da_saxeli[0]
    name=tarigi_da_saxeli[1:]
    name=joina.join(name)
    janri=i.find("div",{'class':"card-genre"}).text
    imdb=i.find("span",{'class':"imdb_rating"}).text.split(":")
    imdb=imdb[1]
    file.write(date+";"+name+";"+janri+";"+imdb+"\n")   # <----------


file.close()









