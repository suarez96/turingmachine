from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# whenever you want to reference a function or anything from the turingforguifile, just use tm.<whateverFunction>
import turingforgui as tmclass

window = Tk()
window.title("Python Turing Machine Simulator")

wlabel = Label(window, text="A Turing Machine\npress/hold enter key to advance", font=("Courier", 24), bg="#d6f9e1", fg="green")
wlabel.pack()

# load gui units
w = Canvas(window, width=400, height=220)
w.pack()

def openfile():
    t.setfile(filedialog.askopenfilename(), e.get())
    return filedialog.askopenfilename()

loadbutton = ttk.Button(window, text="Load", command=openfile)
exit_button = Button(window, text='Quit', bg="#ffbfaf", command=window.destroy)
loadbutton.pack()


def run(f = None):
    tapeLabel.config(text=t.runTM())


window.bind('<Return>', run)

run_btn = Button(window, text="Run", bg="#70f23c", fg="black", command=run)
run_btn.pack()

exit_button.pack()


window.geometry('800x10000')
window.configure(background='#d6f9e1')
window.attributes('-fullscreen', True)

t = tmclass.TM("samestring.txt", str(input("input a string: ") + " "))
tapeLabel = Label(window, text=t.s, font=("Courier", 18), bg="#d6f9e1")
tapeLabel.pack()

e = Entry(window)
e.pack()
e.delete(0, END)
e.insert(0, "Enter an input string (remember to load an input file too!)")


filename = PhotoImage(file="BENNY.gif")
image = w.create_image(0, 0, image=filename, anchor='nw')


tapeLabel.pack()

# start running
window.mainloop()