from tkinter import *
import time
import _thread
 
c = Canvas(width=200,height=460,bg='grey80') #создание холста с размерами и цветом
c.pack() #расположить виджеты в окне

red = c.create_oval(50,50,150,150,fill="red") #создание эллипса с координатами и цветом
redline = c.create_oval(50,50,150,150, outline="black") #создание эллипса с координатами и цветом
yellow = c.create_oval(50,150,150,250,fill="yellow") #создание эллипса с координатами и цветом
yellowline = c.create_oval(50,150,150,250, outline="black") #создание эллипса с координатами и цветом
green = c.create_oval(50,250,150,350,fill="green") #создание эллипса с координатами и цветом
greenline = c.create_oval(50,250,150,350, outline="black") #создание эллипса с координатами и цветом
svetofor = c.create_rectangle(45,45,155,355, outline="black") #создание прямоугольника с координатами и цветом
start = c.create_rectangle(30,400,170,450,fill="white") #создание прямоугольника с координатами и цветом
starttxt = c.create_text(86,419,text="Start!",anchor="nw") #создание текста с координатами

def start_func(event):
    c.delete(start) #удаление квадрата
    c.delete(starttxt) #удаление теста
    c.delete(red) #удаление эллипса
    c.delete(yellow) #удаление эллипса
    c.delete(green) #удаление эллипса
    _thread.start_new_thread(f1, ()) #создание нового потока
def f1():
    cnt = 300
    while cnt >= 0:
        if cnt==300:
            red = c.create_oval(50,50,150,150,fill="red") #создание эллипса с координатами и цветом
        if cnt==200:
            yellow = c.create_oval(50,150,150,250,fill="yellow") #создание эллипса с координатами и цветом
        if cnt==100:
            c.delete(red) #удаление эллипса
            c.delete(yellow) #удаление эллипса
            green = c.create_oval(50,250,150,350,fill="green") #создание эллипса с координатами и цветом
        if cnt == 0:
            cnt = 301
            c.delete(green) #удаление эллипса
            cnt2 = 250
            while cnt2 >= 0:
                if (cnt2==250)or(cnt2==150)or(cnt2==50):
                    green = c.create_oval(50,250,150,350,fill="green") #создание эллипса с координатами и цветом
                if (cnt2==200)or(cnt2==100)or(cnt2==0):
                    c.delete(green) #удаление эллипса
                time.sleep(0.02) #приостановить таймер
                cnt2 -= 1
            cnt2 = 100
            while cnt2 >= 0:
                if cnt2 == 100:
                    yellow = c.create_oval(50,150,150,250,fill="yellow") #создание эллипса с координатами и цветом
                if cnt2 == 0:
                    c.delete(yellow) #удаление эллипса
                time.sleep(0.02) #приостановить таймер
                cnt2 -= 1
        time.sleep(0.02) #приостановить таймер
        cnt -= 1
    _thread.exit() #приостановить таймер
    
c.tag_bind(start,'<Button-1>',start_func) #выполнение функции при нажатии на квадрат
c.tag_bind(starttxt,'<Button-1>',start_func) #выполнение функции при нажатии на прямоугольник

mainloop() #приостановить выполнение программы
