from tkinter import *
from PIL import ImageTk,Image 

root = Tk()

root.title('Xoleza')
root.geometry('500x320')

img = ImageTk.PhotoImage(Image.open('assistantt.png'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')


userText = StringVar()
#Helps to manage the value of a widget such as Labels or Entry more effeciently

userText.set("Your Voice Assistant")
userFrame = LabelFrame(root, text="Xoleza", font=('Railways',24,'bold'))
userFrame.pack(fill='both', expand='yes')

top = Message(userFrame, textvariable=userText, bg='black', fg='white')
top.config(font=("Century Gothic",15,'bold'))
top.pack(side='top', fill='both', expand='yes')

button_run = Button(root, text='Run', font=('railway',10,'bold'), bg='red', fg='white').pack(fill='x', expand='no')
button_close = Button(root, text='Close', font=('railway',10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')





root.mainloop()
