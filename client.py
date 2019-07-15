#created by eyalb.s
import random
import tkinter as tk
from PIL import Image,ImageTk
import socket


HOST = "localhost"
PORT = 4445
window=tk.Tk()
window.geometry("300x500")
window.title("Scissor Paper Rock @Diwas ")
player_points = 0
computer_points = 0


image=Image.open('aa.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=15,row=0)

#global variables
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""
PRINTABLE = {'t':"Its A Tie", 'p': "Player Won!" , 'c': "Computer Won!"}


def choice_to_number(choice):
    rps={'scissor':0,'paper':1,'rock':2}
    return rps[choice]

def number_to_choice(number):
    rps={0:'scissor',1:'paper',2:'rock'}
    return rps[number]
     
def player_won():
    global player_points
    global computer_points
    player_points += 1
    print("Player:" + str(player_points) + "\nComputer:"+str(computer_points))
def computer_won():
    global computer_points
    global player_points
    computer_points += 1
    print("Player:" + str(player_points) + "\nComputer:"+str(computer_points))
    



def send(your):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(str(your), 'utf-8'))
        won = ""
        while won == "":
            won = sock.recv(1024)
        won = won.decode("utf-8")
        print(PRINTABLE[won])
        if won == 'p':
            player_won()
        elif won  == 'c':
            computer_won()
        

#Event Handling
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='r'
    send(USER_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='p'
    send(USER_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='s'
    send(USER_CHOICE)
    
#buttons
button1=tk.Button(text="       Scissor         ",bg="red",command=scissor, height=1,width=8,font=('arial',15,'bold'))
button1.grid(column=15,row=1)
button2=tk.Button(text="        Paper          ",bg="pink",command=paper, height=1,width=8,font=('arial',15,'bold'))
button2.grid(column=15,row=2)
button3=tk.Button(text="         Rock          ",bg="yellow",command=rock, height=1,width=8,font=('arial',15,'bold'))
button3.grid(column=15,row=3)  


window.mainloop()
