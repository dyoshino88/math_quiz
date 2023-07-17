import tkinter
import tkinter.messagebox
import random

tmr = 0
index = 0

key = ""


def count_up():     #タイマー機能
    global tmr

    label = tkinter.Label(root, text=tmr, font=("Times New Roman", 24))
    label.place(x=340, y=167)
    
    tmr = tmr + 1    
    root.after(1000, count_up)

    

def key_down(e):
    global key, x, y

    key = e.keysym
    
    if key == "Return":     #「ENTER」キーで、入力した数字をansに入れる。
        ans = entry.get()
        
        if ans == str(x+y) and index == 1:
            tkinter.messagebox.showinfo("結果", "正解！")

        elif ans == str(x-y) and index == 2:
            tkinter.messagebox.showinfo("結果", "正解！")

        elif ans == str(x*y) and index == 3:
            tkinter.messagebox.showinfo("結果", "正解！")

        elif ans == str(x) and index == 4:
            tkinter.messagebox.showinfo("結果", "正解！")

        else:
            tkinter.messagebox.showinfo("結果", "不正解です")

    elif key == "Right":     #「→」キーを押したら問題を変更する
        
        
        label2.place_forget()
        entry.delete(0, tkinter.END)


        Question_set1()
        

def Question_set1():
    global x, y, label2

    x = random.randint(11, 30)
    y = random.randint(5, 9)       

    if index == 1:
        label2 = tkinter.Label(root, text=str(x) + " + " + str(y) + " = ", 
                               font=("Times New Roman", 36) )
    if index == 2:
        label2 = tkinter.Label(root, text=str(x) + " - " + str(y) + " = ", 
                               font=("Times New Roman", 36) )
    if index == 3:
        label2 = tkinter.Label(root, text=str(x) + " × " + str(y) + " = ", 
                               font=("Times New Roman", 36) ) 
    if index == 4:
        label2 = tkinter.Label(root, text=str(x*y) + " ÷ " + str(y) + " = ",
                               font=("Times New Roman", 36) )
            
    label2.place(x=40, y=57)

    

def Question_set2():


    label = tkinter.Label(root, text= 
                "「ENTER」キー・・・答え合わせ \n「→」キー・・・次の問題", 
                          font=("Times New Roman", 12) )
    label.place(x=50, y=160)
   

    entry.place(x=250, y=57)

    root.bind("<KeyPress>", key_down)

    count_up()
    
def button_forget():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()

    
def addition():     #足し算
    global index

    button_forget()


    index = 1


    Question_set1()
    Question_set2()


def subraction():     #引き算
    global index

    button_forget()
    

    index = 2


    Question_set1()
    Question_set2()

def multiplication():     #掛け算
    global index

    button_forget()

    
    index = 3


    Question_set1()
    Question_set2()

def division():     #割り算
    global index

    button_forget()

    index = 4



    Question_set1()
    Question_set2()
   

    
root = tkinter.Tk()
root.title("四則演算")
root.resizable(False, False)
root.geometry("500x220")

entry = tkinter.Entry(width=3, font=("Times New Roman", 36))

button1 = tkinter.Button(root, text="足し算",
                font=("Times New Roman", 24), command=addition)
button1.place(relx=0.15, y=37, width=150)

button2 = tkinter.Button(root, text="引き算", 
                font=("Times New Roman", 24), command=subraction)
button2.place(relx=0.55, y=37, width=150)

button3 = tkinter.Button(root, text="かけ算", 
                font=("Times New Roman", 24), command=multiplication)
button3.place(relx=0.15, y=127, width=150)

button4 = tkinter.Button(root, text="割り算",
                font=("Times New Roman", 24), command=division)
button4.place(relx=0.55, y=127, width=150)



root.mainloop() 
 