
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
w = Label(window, text="Turing Machine", font=("Courier", 24), bg="#66ccff")
window.title("Python Turing Machine Simulator")
w.pack()
window.geometry('800x10000')
window.configure(background='#66ccff')
window.attributes('-fullscreen', True)

w = Canvas(window, width=300, height=500)
filename = PhotoImage(file = "arrow.png")
image = w.create_image(50, 50, anchor=NE, image=filename)
w.pack()

def openfile():
    return filedialog.askopenfilename()

loadbutton = ttk.Button(window, text="Load", command=openfile) 
exit_button = Button(window, text='Quit', command=window.destroy)
exit_button.pack()
loadbutton.pack()

# infinite loop
window.mainloop()