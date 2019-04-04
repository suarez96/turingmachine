
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
w = Label(window, text="A Turing Machine", font=("Courier", 24), bg="#d6f9e1", fg="green")
window.title("Python Turing Machine Simulator")
w.pack()
window.geometry('800x10000')
window.configure(background='#d6f9e1')
window.attributes('-fullscreen', True)

w = Canvas(window, width=360, height=480)
filename = PhotoImage(file = "BENNY.gif")
image = w.create_image(120, 110, image=filename)

w.pack()

def run():
    os.system('turingmachine.py')

run_btn = Button(window, text="Run", bg="#70f23c", fg="black",command=run)

def openfile():
    return filedialog.askopenfilename()

loadbutton = ttk.Button(window, text="Load", command=openfile) 
v = StringVar()
e = Entry(window, textvariable=v)
e.pack()

v.set("Enter your string:")
s = v.get()
exit_button = Button(window, text='Quit', bg="#ffbfaf", command=window.destroy)
loadbutton.pack()
run_btn.pack()
exit_button.pack()
#kk = Label(window, text="By A & K fo' CS2333", font=("Courier", 12), bg="#d6f9e1", fg="green")
#kk.pack()

# infinite loop
window.mainloop()