from tkinter import *
from tkinter import ttk
from sagamocdo import Health
win=Tk()
win.geometry('400x350')
win.resizable(0,0)
win.title("Heart rate calculator")
asaki=Label(text="ასაკი                             ")
asaki.grid(row=0,column=0,padx=0,pady=5)

wlis=Label(text="წლის                         ")
wlis.grid(row=0,column=2,padx=0,pady=5)


veli1=Entry(width=20)
veli1.grid(row=0,column=1,padx=0,pady=5)

sqesi=Label(text="სქესი                           ")
sqesi.grid(row=1,column=0,padx=0,pady=5)

gender1=IntVar()
gender1.set(2)

female=ttk.Radiobutton(win,text="f",variable=gender1,value=1)
female.grid(row=1,column=1,sticky="w",padx=10)

male=ttk.Radiobutton(win,text="m",variable=gender1,value=2)
male.grid(row=1,column=1,sticky="w",padx=40)


n_puls=Label(text="ნორმ.პულსი             ")
n_puls.grid(row=2,column=0,padx=0,pady=5)

wutshi=Label(text="წუთში                      ")
wutshi.grid(row=2,column=2,padx=0,pady=5)

veli2=Entry(width=20)
veli2.grid(row=2,column=1,padx=0,pady=5)

workout=Label(text="  ვარჯიშის ტიპი            ")
workout.grid(row=3,column=0,padx=0,pady=5)

sityva=StringVar()
sityva.set("აირჩიეთ")
combo = ttk.Combobox(win, values=["Intensive","Average","Begginer"],textvariable=sityva,state="readonly")
combo.grid(row=3,column=1)

sash_sicocxle=Label(text="       სიც. საშ. ხანგრძლივობა:")
sash_sicocxle.grid(row=5,column=0,pady=10,padx=0)

max_puls=Label(text=" მაქსიმალური პულსი:")
max_puls.grid(row=6,column=0,pady=10,padx=0)

varjishi=Label(text="  მაქს.პულსი ვარჯიისას: ")
varjishi.grid(row=7,column=0,pady=10,padx=0)

var1=StringVar()
var2=StringVar()
var3=StringVar()

lab1=ttk.Label(win, textvariable=var1)
lab2=ttk.Label(win, textvariable=var2)
lab3=ttk.Label(win, textvariable=var2)

lab1.grid(row=6, column=1)
lab2.grid(row=5, column=1)
lab3.grid(row=5, column=1)



def funqcia():
    asak=veli1.get()
    genderi=gender1.get()
    puls=veli2.get()
    workout_type=combo.current()


    gamotvla=Health(asak,genderi,puls)

    var1.set(gamotvla.sashualo_sicocxle())
    var2.set(gamotvla.max_guliscema())
    var3.set(gamotvla.max_guliscema_varjishisas(workout_type))

buttona=ttk.Button(text="გამოთვლა",command=funqcia)
buttona.grid(row=4,column=0,padx=10,pady=10)


mainloop()