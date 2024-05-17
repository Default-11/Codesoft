import customtkinter
from tkinter import END,messagebox
def clear():
    entryfield.delete(0,END)
def click(number):
    entryfield.insert(END,number)
def ans():
    expression=entryfield.get()
    try:
        result=eval(expression)
        entryfield.delete(0,END)
        entryfield.insert(0,result)
    except SyntaxError:
        messagebox.showerror("Error","Invalid expression")
    except ZeroDivisionError:
        messagebox.showerror("Error","Cannot divide by zero")

root=customtkinter.CTk()
root.geometry("400x330")
root.title("Calculator")
root.config(bg='black')

entryfield=customtkinter.CTkEntry(root,font=('arial',20,'bold'),text_color='white',fg_color='black',bg_color='black',border_color='white',width=380,height=50)
entryfield.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

b7=customtkinter.CTkButton(root,font=('arial',20,'bold'),bg_color='black',text="7",cursor="hand2",width=80,command=lambda:click('7'))
b7.grid(row=1,column=0,pady=10,padx=10)
b8=customtkinter.CTkButton(root,font=('arial',20,'bold'),bg_color='black',text="8",cursor="hand2",width=80,command=lambda:click('8'))
b8.grid(row=1,column=1)
b9=customtkinter.CTkButton(root,font=('arial',20,'bold'),bg_color='black',text="9",cursor="hand2",width=80,command=lambda:click('9'))
b9.grid(row=1,column=2)
badd=customtkinter.CTkButton(root,font=('arial',20,'bold'),bg_color='black',text="-",cursor="hand2",width=100,fg_color="orange",hover_color="orange3",command=lambda:click('-'))
badd.grid(row=1,column=3)

b4=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="4",bg_color='black',cursor="hand2",width=80,command=lambda:click('4'))
b4.grid(row=2,column=0,pady=10)
b5=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="5",bg_color='black',cursor="hand2",width=80,command=lambda:click('5'))
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="6",bg_color='black',cursor="hand2",width=80,command=lambda:click('6'))
b6.grid(row=2,column=2)
badd=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="+",bg_color='black',fg_color="orange",hover_color="orange3",cursor="hand2",width=100,command=lambda:click('+'))
badd.grid(row=2,column=3)

b1=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="1",bg_color='black',cursor="hand2",width=80,command=lambda:click('1'))
b1.grid(row=3,column=0,pady=10)
b2=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="2",bg_color='black',cursor="hand2",width=80,command=lambda:click('2'))
b2.grid(row=3,column=1)
b3=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="3",bg_color='black',cursor="hand2",width=80,command=lambda:click('3'))
b3.grid(row=3,column=2)
bmul=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="*",bg_color='black',fg_color="orange",hover_color="orange3",cursor="hand2",width=100,command=lambda:click('*'))
bmul.grid(row=3,column=3)

b0=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="0",bg_color='black',cursor="hand2",width=80,command=lambda:click('0'))
b0.grid(row=4,column=0,pady=10)
bdot=customtkinter.CTkButton(root,font=('arial',20,'bold'),text=".",bg_color='black',fg_color="orange",hover_color="orange3",cursor="hand2",width=80,command=lambda:click('.'))
bdot.grid(row=4,column=1)
bdiv=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="/",bg_color='black',fg_color="orange",hover_color="orange3",cursor="hand2",width=80,command=lambda:click('/'))
bdiv.grid(row=4,column=2)
bclear=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="C",bg_color='black',fg_color="red",hover_color="red3",cursor="hand2",width=100,command=lambda:clear())
bclear.grid(row=4,column=3)

bequal=customtkinter.CTkButton(root,font=('arial',20,'bold'),text="=",bg_color='black',fg_color="green",hover_color="green3",cursor="hand2",width=380,height=40,command=lambda:ans())
bequal.grid(row=5,column=0,columnspan=4,pady=10)
root.mainloop()