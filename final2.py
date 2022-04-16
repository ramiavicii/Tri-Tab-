import tkinter as  tk
window=tk.Tk()
window.title("sort table")

def fin():
      window.destroy()

#initialisation des donnees
tab=[]
def permute(tab,x,y):
    inter=tab[x]
    tab[x]=tab[y]
    tab[y]=inter
    
def tri():
    nb = int(e.get())
    tab2=[]
    for k in tab:
        tab2.append(int(k.get()))
    for i in range(0,nb-1):
        min=i
        for j in range(i+1,nb):
            if tab2[j]<tab2[min]:
                min=j
        permute(tab2,min,i)            
    
    for v in range (nb):
         eee=tk.Entry(width=10,bg="blue",fg="white",borderwidth=5)
         eee.insert(0,tab2[v])
         eee.grid(row=9,column=v)
    #bouton pour sortir 
    buttonfinal=tk.Button(window,text="finish",fg="white", bg="purple",command=fin)     
    buttonfinal.grid(row=10,column=1,columnspan=3)  


#fonction lors du click sur le bouton du nb de cases 
def affich():
    nb = int(e.get())
    tabchar=["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","s","y","z"]
    for v in range(nb):
        ee=tk.Entry(width=10,bg="blue",fg="white",borderwidth=5)
        ee.grid(row=4,column=v)
        if (ee.get()) in tabchar:
            labelerror=tk.label(window,text="error")
            labelerror.grid(row=8,column=1)
        else:
            tab.append(ee)   
    sortbutton=tk.Button(window,text="click to sort", fg="white", bg="purple",command=tri)
    sortbutton.grid(row=7,column=1,columnspan=3) 



#affichage du premier msg
mylabel1=tk.Label(text="enter the table's number of boxes: ",pady=5)
mylabel1.grid(row=0,column=1,columnspan=3)

#case pour donner le nb de cases du tableau 
e=tk.Entry(width=20,borderwidth=5)
e.grid(row=2,column=1,columnspan=3)


#bouton aprés le saisie du nb de cases du tableau
tabButton=tk.Button(window,text="click here please", fg="white", bg="purple",command=affich) 
tabButton.grid(row=3,column=1,columnspan=3) 

   
window.mainloop()