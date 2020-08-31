from tkinter import *
import random
from tkinter import messagebox

def labelslider():
    global count,sliderwords
    text = 'Welcome to JAK Typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelslider)

def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timerLabelCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timerLabelCount.configure(text=timeleft)
        timerLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Missed = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','To Play Again Hit Retry')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timerLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

words = ['Grapes','Mango','Apple','Orange','Cool','Game','PUBG','Gun','Fan','Door','Laptop','Buds','Computer','Mobile','Vishnu','Laxmi','Ganesh',
         'Mahesh','Brahma','Pradumna','Saraswati','Parvati','Jonak','FRAG','Morning','Afternoon','Night','Indra','Mathematics','Python','Pycharm',
         'JavaScript','C++','Intelli J']

######################################## Root Method ###################################
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('JAK Typing Speed Increaser Game')
root.iconbitmap('Hydrattz-Multipurpose-Alphabet-Letter-J-blue.ico')

######################################## Variables ###################################
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0

######################################## Label Method ###################################
fontLabel = Label(root,text='',font=('arial',25,'italic bold'),bg='powder blue',fg='Red',width=40)
fontLabel.place(x=10,y=10)
labelslider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('arial',25,'bold'),bg='powder blue',fg='black')
wordLabel.place(x=335,y=200)

scoreLabel = Label(root,text='Your Score: ',font=('arial',25,'italic bold'),bg='powder blue',fg='Black')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('arial',25,'italic bold'),bg='powder blue',fg='Green')
scoreLabelCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left:',font=('arial',25,'italic bold'),bg='powder blue',fg='Black')
timerLabel.place(x=600,y=100)

timerLabelCount = Label(root,text=timeleft,font=('arial',25,'italic bold'),bg='powder blue',fg='Green')
timerLabelCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),bg='powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=80,y=450)

######################################## Entry Method ###################################
wordEntry = Entry(root,font=('arial',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=200,y=300)
wordEntry.focus_set()

######################################## Binding ###################################
root.bind('<Return>',startGame)
root.mainloop()
######################################## Done ###################################
