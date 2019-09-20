import tkinter
import tkinter.ttk as ttk
from tkinter import *
root = tkinter.Tk()

P=dict()
P['Критерий_1']={}
P['Критерий_2']={}
P['Критерий_3']={}
P['Критерий_4']={}
P['Критерий_5']={}
P['Критерий_6']={}
tkinter.Label(root, text='Критерий/Банк', borderwidth=8).grid(row=0,column=0)#borderwith - отступ от границ, row - номер строки, column - номер столбца
for i in range(len(list(P))):
    tkinter.Label(root, text=list(P)[i], borderwidth=8).grid(row=i+1,column=0)
   


tkinter.Label(root, text='Банк_1', borderwidth=8).grid(row=0,column=1)
numberofP1=[tkinter.StringVar() for i in range(len(list(P)))]
for i in range(len(list(P))):
    tkinter.Spinbox(root, values=('0','0,05','0,1','0,15','0,2','0,25','0,3','0,35', '0,4','0,45', '0,5','0,55', '0,6','0,65', '0,7','0,75', '0,8','0,85', '0,9', '0,95','1'),textvariable=numberofP1[i]).grid(row=i+1,column=1)

tkinter.Label(root, text='Банк_2', borderwidth=8).grid(row=0,column=2)
numberofP2=[tkinter.StringVar() for i in range(len(list(P)))]
for i in range(len(list(P))):
    tkinter.Spinbox(root, values=('0','0,05','0,1','0,15','0,2','0,25','0,3','0,35', '0,4','0,45', '0,5','0,55', '0,6','0,65', '0,7','0,75', '0,8','0,85', '0,9', '0,95','1'),textvariable=numberofP2[i]).grid(row=i+1,column=2)

tkinter.Label(root, text='Банк_3', borderwidth=8).grid(row=0,column=3)
numberofP3=[tkinter.StringVar() for i in range(len(list(P)))]
for i in range(len(list(P))):
    tkinter.Spinbox(root, values=('0','0,05','0,1','0,15','0,2','0,25','0,3','0,35', '0,4','0,45', '0,5','0,55', '0,6','0,65', '0,7','0,75', '0,8','0,85', '0,9', '0,95','1'),textvariable=numberofP3[i]).grid(row=i+1,column=3)

def f():
    q=min([float(i.get().replace(",", ".")) for i in numberofP1])
    w=min([float(i.get().replace(",", ".")) for i in numberofP2])
    e=min([float(i.get().replace(",", ".")) for i in numberofP3])
    
    l=[q,w,e]
    a=l.index(max(l))
    if a==0:
        z='Банк_1 - лучший выбор'
    elif a==1:
        z='Банк_2 - лучший выбор'
    else:
        z='Банк_3 - лучший выбор'
    label=tkinter.Label(root,text=z).grid(row=9,column=2)
        
 
button=tkinter.Button(root, text='Выбрать лучший банк',command=lambda:f(),borderwidth=5).grid(row=8,column=2)

button2=tkinter.Button(root, text='Выйти', command=root.destroy,borderwidth=5).grid(row=9,column=4)

root.mainloop()
