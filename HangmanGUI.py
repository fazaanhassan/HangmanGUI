from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):
    """A GUI application"""

    def __init__(self, master=None): #start window instance
        Frame.__init__(self,master)
        self.master = master
        self.window()

    def window(self):
        self.master.title("Hangman GUI")

        self.final_word = ""
        self.img  = ImageTk.PhotoImage(Image.open("images/hangman11.gif"))
        self.panel = Label(image = self.img)

        self.mysteryword = Entry()
        self.mysteryword.focus()
        self.letter = Entry()


        self.instructionlabelone = Label(text="First, enter the word you want to use in the game and hit Enter:")
        self.instructionlabeltwo = Label(text="Then, enter letters and hit Enter:")
        self.labelthree = Label(text="Incorrect Letters:")

        self.mysteryword.bind('<Return>', self.store_word)
        self.letter.bind ('<Return>', self.game)
        self.textbox = Text(height=1, width=40)
        self.textbox.insert(1.0, "Output! Do Not Type Anything Here!")
        self.textbox.config(state=DISABLED)
        self.guessesBox = Text(height=10, width=2)
        self.outputBox = Text(height=1, width=50)
        self.outputBox.insert(1.0, "Message Box")

        self.instructionlabelone.grid(row=0,column=0, sticky="W")
        self.mysteryword.grid(row=0,column=1)
        self.textbox.grid(row=1, sticky="W")
        self.panel.grid(row=2, column=0, sticky="W") #image
        self.labelthree.grid(row=1, column=1) #incorrect letters label
        self.guessesBox.grid(row=2,column=1, sticky=N+S) #incorrect letters box
        
        self.instructionlabeltwo.grid(row=4, column=0, sticky="W")
        self.letter.grid(row=4,column=0, sticky="E")
        self.outputBox.grid(row=5, sticky="E")


    def store_word(self, event):
        self.textbox.config(state=NORMAL)
        self.word = self.mysteryword.get()
        assert(type(self.word) == str)
        self.word = self.word.lower()
        self.lstword = list(self.word)
        self.letterdict = {}
        self.index = 0
        self.guesses = 10
        self.usedLetters = []
        for x in self.lstword:
            if x not in self.letterdict:
                self.letterdict[x] = [self.index]
                self.index += 1
            else:
                self.letterdict[x] += [self.index]
                self.index += 1
        self.construct_word = ['_ '] * len(self.word)
        for letter in self.lstword: #input spaces in between multiple words
            if letter == ' ':
                key = self.letterdict[letter]
                for x in key:
                    self.construct_word[x] = '  ' 
        self.final_word =''.join(self.construct_word)
        self.textbox.insert(1.0, (self.final_word+"\n"))
        self.mysteryword.delete(0, END)
        self.letter.focus()

    def game(self,event):
        self.textbox.delete(1.0, END)
        letter = self.letter.get()
        self.letter.delete(0, END)
        if letter in self.usedLetters:
            msg = "You already used that letter! Try another! \n"
            self.outputBox.insert(1.0, msg)
        elif letter in self.word:
            self.usedLetters += letter
            key = self.letterdict[letter]
            for x in key:
                self.construct_word[x] = letter
            self.final_word = ''.join(self.construct_word)
            msg = "Keep going! \n"
            if self.final_word == self.word:
                msg = "Congratulations! You correctly guessed the word ! \n"
                self.outputBox.insert(1.0, msg)
                self.status = "Won"
                self.end_game() #exits game function
                msg = "Message Box \n" #reset output box text if user chooses to start new game
            self.outputBox.insert(1.0, msg)
        else:
            self.usedLetters += letter
            self.guesses -= 1
            letter = letter + '\n'
            self.guessesBox.insert(1.0, letter)
            if self.guesses == 9 :
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman09.gif"))
            elif self.guesses == 8:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman08.gif"))
            elif self.guesses == 7:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman07.gif"))
            elif self.guesses == 6:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman06.gif"))
            elif self.guesses == 5:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman05.gif"))
            elif self.guesses == 4:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman04.gif"))
            elif self.guesses == 3:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman03.gif"))
            elif self.guesses == 2:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman02.gif"))
            elif self.guesses == 1:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman01.gif"))
            else:
                self.img = ImageTk.PhotoImage(Image.open("images/Hangman00.gif"))
                self.panel = Label(image = self.img)
                self.panel.grid(row=2, column=0)
                msg = "Game Over ! \n"
                self.outputBox.insert(1.0, msg)
                self.status = "Lost"
                self.end_game() #exits game function

            self.panel = Label(image = self.img)
            self.panel.grid(row=2, column=0)
            if self.guesses == 0:
                msg = "Message Box \n" #reset message box if user chooses to play new game
            else:
                msg = "That letter is not in the word! \n"
            self.outputBox.insert(1.0, msg)
        self.textbox.insert(1.0, self.final_word)
        
    def end_game(self):
        if self.status == "Won":
            msg = ("You correctly guessed the word '" + self.word + "'. \n Would you like to play again?") #messagebox syntax = (title, msg, options)
            alert = messagebox.askquestion('You won!', msg)
            if alert == "yes":
                self.window() #start new game
            else: 
                quit() #close window
                
        else: #if self.status == "Lost"
            msg = ("The correct word was '" + self.word + "'. \n Would you like to play again?")
            alert = messagebox.askquestion('You lost!', msg)
            if alert == "yes":
                self.window() #start new game
            else:
                quit() #close window
    def client_exit(self):
        exit()
        
#create window
root = Tk()
root.geometry("530x400") #size window

app = Window(root)
root.mainloop()
