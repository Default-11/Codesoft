#Add the item then click on item then press cross item#
from tkinter import *
from tkinter.font import Font

def del_item():
    listbox.delete(ANCHOR)
def add_item():
    listbox.insert(END,entry.get())
    entry.delete(0,END)
def cross_item():
    listbox.itemconfig(listbox.curselection(),fg="#dedede")
    listbox.selection_clear(0,END)
def uncross_item():
    listbox.itemconfig(listbox.curselection(),fg="#464646")
    listbox.selection_clear(0,END)

root=Tk()
root.title("To Do List")
root.geometry("400x400")

font=Font(family="Algerian",size=20,weight="bold")
frame=Frame(root)
frame.pack(pady=10)

listbox=Listbox(frame,font=font,height=5,width=20,bg="systembuttonface",fg="#464646",bd=0,highlightthickness=0,selectbackground="#a6a6a6",activestyle="none")
listbox.pack(side="left",fill="both")

scroll=Scrollbar(frame)
scroll.pack(side="right",fill="both")

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

entry=Entry(root,font=('arial',24),width=18)
entry.pack(pady=20)

button_frame=Frame(root)
button_frame.pack(pady=20)
del_button=Button(button_frame,text="Delete Item",command=del_item)
del_button.grid(row=0,column=0,padx=10)
add_button=Button(button_frame,text="Add Item",command=add_item)
add_button.grid(row=0,column=1,padx=10)
cross_button=Button(button_frame,text="Cross Item",command=cross_item)
cross_button.grid(row=0,column=2,padx=10)
uncross_button=Button(button_frame,text="uncross Item",command=uncross_item)
uncross_button.grid(row=0,column=3,padx=10)
# list=['xyz','abc','abbb','afdajf']
# for a in list:
#     listbox.insert(END,a)
root.mainloop()