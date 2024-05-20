from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_len=int(length.get())
    
    if choice.get()==1:
        passw.delete(0,END)
        passw.insert(0,random.sample(small_alphabets,password_len))
    elif choice.get()==2:
        passw.delete(0,END)
        passw.insert(0,random.sample(small_alphabets+capital_alphabets,password_len))
    elif choice.get()==3:
        passw.delete(0,END)
        passw.insert(0,random.sample(all,password_len))
    
def copy():
    password=passw.get()
    pyperclip.copy(password)

root=Tk()
root.config(bg='black')
Font=('arial',15,'bold')
choice=IntVar()
Plabel=Label(root,text="Password Generator",font=('verdana',20,'bold'),bg='black',fg='white')
Plabel.grid(pady=5)
weakb=Radiobutton(root,text='Weak',font=Font,variable=choice,value=1,bg='green')
weakb.grid(pady=5)
mediumb=Radiobutton(root,text='Medium',font=Font,variable=choice,value=2,bg='yellow')
mediumb.grid(pady=5)
strongb=Radiobutton(root,text='Strong',font=Font,variable=choice,value=3,bg='red')
strongb.grid(pady=5)
lenlabel=Label(root,text="Password length",font=Font,fg='white',bg='black')
lenlabel.grid(pady=5)
length=Spinbox(root,from_=5,to_=15,font=Font,width=5)
length.grid(pady=5)
generateb=Button(root,text="Generate",font=Font,command=generator)
generateb.grid(pady=5)
passw=Entry(root,width=28,bo=2,font=Font)
passw.grid()
copyb=Button(root,text='Copy',font=Font,command=copy)
copyb.grid(pady=5)
root.mainloop()