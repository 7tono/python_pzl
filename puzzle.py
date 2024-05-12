import tkinter as tk
import random

blocks = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
global canvas

w = tk.Tk()
w.geometry('1200x700')




def btn_click():
   
    count=0
    n=0
    while count < 16:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if blocks[x][y] == 0:
            count=count+1
            n=n+1
        else:
            continue
        pc =random.randint(1, 25) #パネル数上限
        mc=0#動く数
        while mc < pc:    
            blocks[x][y] = n
         
            s = random.randint(0,3)#上下左右を決める
            
            if s==0:#左
                if y!=0:
                    if blocks[x][y-1]==0:
                        blocks[x][y-1]=n
                        y=y-1
                        mc=mc+1
                        count=count+1
            if s==1:#下
                if x!=3:
                    if blocks[x+1][y]==0:
                        blocks[x+1][y]=n
                        x=x+1
                        mc=mc+1
                        count=count+1
            if s==2:#右
                if y!=3:
                    if blocks[x][y+1]==0:
                        blocks[x][y+1]=n
                        y=y+1
                        mc=mc+1
                        count=count+1
            if s==3:#上
                if x!=0:
                    if blocks[x-1][y]==0:
                        blocks[x-1][y]=n
                        x=x-1
                        mc=mc+1
                        count=count+1
        
            mc=mc+1
    print(blocks[0])
    print(blocks[1])
    print(blocks[2])
    print(blocks[3])

    #canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10,fill="orange",tag="b1")

    #canvas.create_rectangle(110, 10, 390, 290)
    for x in range(4):
        for y in range(4):
            if blocks[y][x]==1:
                canvas.create_rectangle(x*50+50, y*50+10, x*50+50+50, y*50+50+10,fill="orange",tag="b1")
            if blocks[y][x]==2:
                canvas.create_rectangle(x*50+50, y*50+240, x*50+100, y*50+50+240,fill="blue",tag="b2")
            if blocks[y][x]==3:
                canvas.create_rectangle(x*50+900, y*50+10, x*50+50+900, y*50+50+10,fill="yellow",tag="b3")
            if blocks[y][x]==4:
                canvas.create_rectangle(x*50+50, y*50+440, x*50+100, y*50+50+440,fill="red",tag="b4")
            if blocks[y][x]==5:
                canvas.create_rectangle(x*50+900, y*50+240, x*50+50+900, y*50+50+240,fill="green",tag="b5")
            if blocks[y][x]==6:
                canvas.create_rectangle(x*50+900, y*50+440, x*50+50+900, y*50+50+440,fill="black",tag="b6")  

def Frame_write():
    canvas.create_rectangle(500, 200, 700, 400)

    canvas.create_line(500, 250, 700, 250)
    canvas.create_line(500, 300, 700, 300)
    canvas.create_line(500, 350, 700, 350)

    canvas.create_line(550, 200, 550, 400)
    canvas.create_line(600, 200, 600, 400)
    canvas.create_line(650, 200, 650, 400)


btn = tk.Button(w, text="OK", command=btn_click).pack()
# Canvasの作成
canvas = tk.Canvas(w, width = 1200,height = 650,bg = "white")
#canvas = tk.Canvas(w, background="#fff", width=500, height=300).pack()
canvas.pack()
Frame_write()
w.mainloop()



