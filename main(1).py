from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")
window.geometry("200x400")

N = 0
p1 = ["1","2","3","4","5","6","7","8","9"]
p2 = ["1","2","3","4","5","6","7","8","9"]
 



def clicked(Button,text):
   
    global N
    if p1[0]==p1[1]==p1[2] or p1[3]==p1[4]==p1[5] or p1[6]==p1[7]==p1[8] or p1[2]==p1[4]==p1[6] or p1[0]==p1[4]==p1[8] or  p1[0]==p1[3]==p1[6] or p1[1]==p1[4]==p1[7] or p1[2]==p1[5]==p1[8] :
        return  messagebox.showinfo("The end","Game Ends With Player 1 as the winner!")
    elif p2[0]==p2[1]==p2[2] or p2[3]==p2[4]==p2[5] or p2[6]==p2[7]==p2[8] or p2[2]==p2[4]==p2[6] or p2[0]==p2[4]==p2[8] or p2[0]==p2[3]==p2[6] or p2[1]==p2[4]==p2[7] or p2[2]==p2[5]==p2[8]:
        return  messagebox.showinfo("The end","Game Ends With Player 2 as the winner!")
       
    if N == 7:
        messagebox.showinfo("The last move","Game Ends With This Next Move!")
   
    if N%2==0:
        Button.config(text="X", fg = "white")
        p1[int(text)-1]="X"
       
    else:
        Button.config(text="O", fg = "white")
        p2[int(text)-1]="O"
       
    N+=1
    if N == 9:
        messagebox.showinfo("The last move","Draw")
        return
   
 
Button0 = Button(window,width=8, height= 8,text="1", fg= "blue",  bg = "blue", command = lambda:clicked(Button0,text="1"))
Button0.grid(row =0, column =0)

Button1 = Button(window,width=8, height= 8,text="2", fg= "blue",  bg = "blue", command = lambda:clicked(Button1,text="2"))
Button1.grid(row =0, column =1)    

Button2 = Button(window,width=8, height= 8, text="3", fg= "blue",  bg = "blue", command = lambda:clicked(Button2,text="3"))
Button2.grid(row =0, column =2)



Button3 = Button(window,width=8, height= 8, text="4", fg= "blue",  bg = "blue", command = lambda:clicked(Button3,text="4"))
Button3.grid(row =1, column =0)

Button4 = Button(window,width=8, height= 8, text="5", fg= "blue",  bg = "blue", command = lambda:clicked(Button4,text="5"))
Button4.grid(row =1, column =1)

Button5 = Button(window,width=8, height= 8, text="6", fg= "blue",  bg = "blue", command = lambda:clicked(Button5,text="6"))
Button5.grid(row =1, column =2)



Button6 = Button(window,width=8, height= 8, text="7", fg= "blue",  bg = "blue", command = lambda:clicked(Button6,text="7"))
Button6.grid(row =2, column =0)

Button7 = Button(window,width=8, height= 8, text="8", fg= "blue",  bg = "blue", command = lambda:clicked(Button7,text="8"))
Button7.grid(row =2, column =1)

Button8 = Button(window,width=8, height= 8, text="9", fg= "blue",  bg = "blue", command = lambda:clicked(Button8,text="9"))
Button8.grid(row =2, column =2)







window.mainloop()