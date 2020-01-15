from tkinter import *
root=Tk()
# def func1(event):
#     print(event.x,event.y)
def fe(event):
    l4.config(bg='red', fg='black')
def f2(event):
    l4.config(bg='black', fg='black')
def f1(event):
    exec(t.get(1.0,END))#get() funkcian entry u text meji gracn vercnuma
def print(*args):
    for i in args:
        l3['text']+=str(i)+' '
    l3['text']+='\n'
l1=Label(text='click 1', width=10, height=2)
l2=Label(text='click 2', width=10, height=2)
l3=Label(text=' ', width=100, height=5, anchor=W)
l4=Label(text='Enteri funkcia', width=100, height=8, anchor=W)
b=Button(text='Enter', width=20, height=3)
t=Text()
t.pack()
l1.pack()
l2.pack()
l3.pack()
l4.pack()
root.bind('<Control-Return>', f1)
# root.bind('<Key>', func1) #bind funkcian patasxanatua te knopkin sexmeluc inch pti ani
#root.bind('<Button-1>', func1) #bind Button-1  mkan dzax klikna
l4.bind('<Enter>', fe) 
l4.bind('<Leave>', f2)
root.mainloop()
