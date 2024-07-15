from random import randrange
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame, Label

def pressButton(color="black"):
    
    if color=="red":
        canvas.itemconfigure(redLamp, fill="red")
        canvas.itemconfigure(yellowLamp, fill="black")
        canvas.itemconfigure(greenLamp, fill="black")
        
    elif color=="gold":
        canvas.itemconfigure(yellowLamp, fill="gold")
        canvas.itemconfigure(redLamp, fill="black")
        canvas.itemconfigure(greenLamp, fill="black")
        
    elif color=="lime green":
        canvas.itemconfigure(greenLamp, fill="lime green")
        canvas.itemconfigure(redLamp, fill="black")
        canvas.itemconfigure(yellowLamp, fill="black")

def randomValue():
    
    bil=randrange(1,4)
    
    if bil==1:
        return "Rock"
    
    elif bil==2:
        return "Paper"
    
    elif bil==3:
        return "Scissors"

def playerInput(ply=0):
    
    if ply==1:
        return "Rock"
    
    elif ply==2:
        return "Paper"
    
    elif ply==3:
        return "Scissors"
            
def rockPaperScissors(ply):
    
    computer=randomValue()
    player=playerInput(ply)
    
    if player=="Rock" and computer=="Paper":
        winner="computer"
        
    elif player=="Rock" and computer=="Scissors":
        winner="player"
        
    elif player=="Rock" and computer=="Rock":
        winner="draw"
        
    elif player=="Paper" and computer=="Scissors":
        winner="computer"
        
    elif player=="Paper" and computer=="Rock":
        winner="player"
        
    elif player=="Paper" and computer=="Paper":
        winner="draw"
        
    elif player=="Scissors" and computer=="Rock":
        winner="computer"
        
    elif player=="Scissors" and computer=="Paper":
        winner="player"
        
    elif player=="Scissors" and computer=="Scissors":
        winner="draw"

    etiket3=Label(text= "Player: " + player)
    etiket3.pack()
    etiket4=Label(text= "Computer: " + computer)
    etiket4.pack()
    
    if winner=="player":
        pressButton("lime green")
        print("Player won")
    elif winner=="computer":
        pressButton("red")
        print("Computer Won")
    elif winner=="draw":
        pressButton("gold")
        print("Draw")

color="black"
root=Tk()
root.title("Rock-Paper-Scissors")
frame=Frame(root)
frame.pack()
canvas=Canvas(frame, width=150, height=300)
canvas.create_rectangle(50, 20, 150, 280, fill="gray")
redLamp=canvas.create_oval(70, 40, 130, 100, fill="black")
yellowLamp=canvas.create_oval(70, 120, 130, 180, fill="black")
greenLamp=canvas.create_oval(70, 200, 130, 260, fill="black")

button1=Button(frame, text="Rock",command=lambda: rockPaperScissors(1))
button1.grid(row=1, column=0)
canvas.grid(row=0, column=1)
button2=Button(frame, text="Paper", command=lambda: rockPaperScissors(2))
button2.grid(row=2, column=0)
canvas.grid(row=0, column=1)
button3=Button(frame, text="Scissors", command=lambda: rockPaperScissors(3))
button3.grid(row=3, column=0)
canvas.grid(row=0, column=1)
root.mainloop()
