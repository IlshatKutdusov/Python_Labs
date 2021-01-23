from tkinter import *
import time
import _thread
 
c = Canvas(width=280,height=460,bg='grey80') #создание холста с размерами и цветом
c.pack() #расположить виджеты в окне
 
oval = c.create_oval(30,30,80,80,fill="blue") #создание эллипса с координатами и цветом
 
def oval_func(event):
     c.delete(oval) #удаление эллипса
     _thread.start_new_thread(f1, ()) #создание нового потока
def f1():
    oval = c.create_oval(30,30,80,80,fill="orange") #создание эллипса с координатами и цветом
    time.sleep(1) #приостановить таймер на 1с
    cnt = 450
    while cnt > 0:
        if (cnt<=450)and(cnt>300):
            k = 1
        else:
            if (cnt>=200)and(cnt<300):
                k = -1
                c.itemconfig(oval, fill='yellow')
            else:
                if (cnt>=100)and(cnt<200):
                    k = 1
                    c.itemconfig(oval, fill='white')
                else:
                    k = -1
                    c.itemconfig(oval, fill='red')
        c.move(oval,k,1) #перемещение эллипса
        time.sleep(0.01) #приостановить таймер на 0.01с
        cnt -= 1
    _thread.exit() #закрытие потока
 
c.tag_bind(oval,'<Button-1>',oval_func) #выполнение функции при нажатии на эллипс

mainloop() #приостановить выполнение программы
