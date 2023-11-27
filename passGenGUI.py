import random
import string
from tkinter import *
import tkinter.messagebox as tkmess

class PassGenerator:
      
    def __init__(self, root):
        root.title("Password Generator")
        root.geometry("450x230")
        
        # Initializing this variables since boxes are initially unchecked
        self.upperFlag = False
        self.numFlag = False
        self.symFlag = False
        
        title_label = Label(root, text="Password Generator", font=("Helvetica", 20))
        title_label.grid(column=1, row=1, columnspan=2, padx = 5)
        
        info_label = Label(root, text="Please check off the desired characteristics you want for this password. \nLowercase letters are included in all passwords.", font=("Helvetica", 10))
        info_label.grid(column=1, row=2, columnspan=2, padx = 5)
        
        # Password Length
        passLen_label = Label(root, text="Length of Password:", font=("Helvetica", 10))
        passLen_label.grid(column=1, row=3, padx=3, pady=5, sticky = (W)) #, sticky = (W)
        
        self.passLen = IntVar()
        passLen_entry = Entry(root, textvariable=self.passLen, font=("Helvetica", 15), width=3)
        passLen_entry.grid(column=1, row=3, padx=50, pady=5) #, sticky = (E)
        
        # Checkbox if you want the password to include uppercase letters
        self.upperFlagVar = BooleanVar()
        upperBox = Checkbutton(root, text = "Include Uppercase Letters",  
                      variable = self.upperFlagVar, 
                      command=lambda:self.setUpperFlag(),
                      height = 1, 
                      width = 20, font=("Helvetica", 10), justify="left") 
        upperBox.grid(column=1, row=4, padx = 5, sticky = (W))
        
        # Checkbox if you want the password to include numbers
        self.numFlagVar = BooleanVar()
        numBox = Checkbutton(root, text = "Include Numbers",  
                      variable = self.numFlagVar, 
                      command=lambda:self.setNumFlag(),
                      height = 1, 
                      width = 13, font=("Helvetica", 10), justify="left") 
        numBox.grid(column=1, row=5, padx = 5, sticky = (W))
        
        # Checkbox if you want the password to include symbols
        self.symFlagVar = BooleanVar()
        symBox = Checkbutton(root, text = "Include Symbols",  
                      variable = self.symFlagVar, 
                      command=lambda:self.setSymFlag(),
                      height = 1, 
                      width = 13, font=("Helvetica", 10), justify="left") 
        symBox.grid(column=1, row=6, padx = 5, sticky = (W))
        
        # Button to click to generate password
        run_button = Button(root, text="Run", command=self.genPassword, font=("Helvetica", 15))
        run_button.grid(column=2, row=4, rowspan=3, padx = 5, pady=5, sticky = (N,E,W,S))
        
        # Password output
        self.passwordPt = StringVar()
        password_label = Entry(root, bd=0, state="readonly",textvariable=self.passwordPt, width=40, justify="center", font=("Helvetica", 15))
        #password_label = Label(root, textvariable=self.passwordPt, wraplength=200)
        password_label.grid(column=1, row=7, columnspan=3, padx = 5, pady=5, sticky = (N,E,W,S))
        
        
    # Attempts to generate the password with the user's settings with a warning box if the user tries to do impossible settings
    def genPassword(self):
        try:
            passwordSz = self.passLen.get()
            print(passwordSz)
            if passwordSz <= 1:
                note = "Please use a positive integer for password length.\n"
                tkmess.showinfo(title = "Warning", message = note)
                return
        except:
            note = "Please use a positive integer for password length, not text.\n"
            tkmess.showinfo(title = "Warning", message = note)
        try: 
            password = makePassword(passwordSz, self.upperFlag, self.numFlag, self.symFlag)
            print(password)
            self.passwordPt.set(password)
        except:
            if self.upperFlag and self.numFlag and self.symFlag:
                note = "You need a longer password. Please input a bigger number. Mininum is 5.\n"
                tkmess.showinfo(title = "Warning", message = note)
            elif self.upperFlag and (self.numFlag or self.symFlag):
                note = "You need a longer password. Please input a bigger number. Mininum is 4.\n"
                tkmess.showinfo(title = "Warning", message = note)
            elif self.upperFlag or self.numFlag or self.symFlag:
                note = "You need a longer password. Please input a bigger number. Mininum is 3.\n"
                tkmess.showinfo(title = "Warning", message = note)
            
    # Changes the values of the flags if the state of the appropriate textbox changes
    def setUpperFlag(self):
        self.upperFlag = self.upperFlagVar.get()
        print(self.upperFlag)
        
    def setNumFlag(self):
        self.numFlag = self.numFlagVar.get()
        print(self.numFlag)
        
    def setSymFlag(self):
        self.symFlag = self.symFlagVar.get()
        print(self.symFlag)

# Random letter selection 
def randLetters(num, upperFlag):
    letters = string.ascii_lowercase   
    if upperFlag:
        upperLet = string.ascii_uppercase
        upperNum = random.randint(1,num-2)
        lowerNum = num - upperNum
        rand_letters = random.choices(letters,k=lowerNum) + random.choices(upperLet,k=upperNum)
    else:
        rand_letters = random.choices(letters,k=num) 
    return rand_letters

# Makes the password accounting for the different settings
def makePassword(passwordSz, upperFlag, numFlag, symFlag):
    if symFlag and numFlag:
        numLets = random.randint(3,passwordSz-2)
        numNums = random.randint(1,passwordSz-numLets-1)
        numSyms = passwordSz - numLets - numNums
    elif symFlag:
        numLets = random.randint(3,passwordSz-1)
        numNums = 0
        numSyms = passwordSz - numLets 
    elif numFlag:
        numLets = random.randint(3,passwordSz-1)
        numNums = passwordSz - numLets
        numSyms = 0
    else:
        numLets = passwordSz
        numNums = 0
        numSyms = 0
    passList = randLetters(numLets, upperFlag)  + random.choices(string.digits,k=numNums) + random.choices(string.punctuation,k=numSyms)
    random.shuffle(passList)
    password = "".join(passList)
    return password


root = Tk()
PassGenerator(root)
root.mainloop()
