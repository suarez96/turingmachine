from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# whenever you want to reference a function or anything from the turingforguifile, just use tm.<whateverFunction>
import turingforgui as tmclass

window = Tk()
w = Label(window, text="A Turing Machine", font=("Courier", 24), bg="#d6f9e1", fg="green")
insLabel = Label(window, text="Press/hold enter to advance, q to quit", font=("Courier", 16), bg="#d6f9e1", fg="green")
window.title("Python Turing Machine Simulator")
w.pack()
insLabel.pack()
window.geometry('800x10000')
window.configure(background='#d6f9e1')
window.attributes('-fullscreen', True)

w = Canvas(window, width=250, height=210)
filename = PhotoImage(file="BENNY.gif")
image = w.create_image(0, 0, image = filename, anchor = 'n')

w.pack()

t = tmclass.TM("samestring.txt", str(input("Enter the input string: ") + " "))
tapeLabel = Label(window, text=t.s, font=("Courier", 24), bg="#d6f9e1", fg="green")
tapeLabel.pack()


def run(f = None):
    tapeLabel.config(text=t.runTM())
window.bind('<Return>', run)


def quit(f = None):
    window.destroy()
window.bind('q', quit)

run_btn = Button(window, text="Run", bg="#70f23c", fg="black", command=run)


def openfile():
    return filedialog.askopenfilename()


loadbutton = ttk.Button(window, text="Load", command=openfile)
exit_button = Button(window, text='Quit', bg="#ffbfaf", command=window.destroy)
loadbutton.pack()
run_btn.pack()
exit_button.pack()

window.mainloop()
