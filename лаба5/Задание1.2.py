from tkinter import *
import time
import _thread
 
c = Canvas(width=460,height=100,bg='grey80')
c.pack()
 
oval = c.create_oval(30,10,130,80,fill="orange")
c.create_rectangle(180,10,280,80,tag="rect",fill="lightgreen")
trian = c.create_polygon(330,80,380,10,430,80,fill='white',outline="black")
 
def oval_func(event):
     c.delete(oval)
     _thread.start_new_thread(f1, ())
def rect_func(event):
     c.delete("rect")
     c.create_text(180,10,text="Здесь был\nпрямоугольник",anchor="nw")
def triangle(event):
     c.create_polygon(350,70,380,20,410,70,
         fill='yellow',outline="black")
def f1():
    cnt = 10
    while cnt > 0:
        oval = c.create_oval(30,10,130,80,fill="red")
        time.sleep(1)
        c.delete(oval)
        time.sleep(1)
        cnt -= 1
    _thread.exit()
 
c.tag_bind(oval,'<Button-1>',oval_func)
c.tag_bind("rect",'<Button-1>',rect_func)
c.tag_bind(trian,'<Button-1>',triangle)
 
mainloop()
