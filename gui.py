from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# whenever you want to reference a function or anything from the turingforguifile, just use tm.<whateverFunction>
import turingforgui as tmclass

window = Tk()
w = Label(window, text="A Turing Machine", font=("Courier", 24), bg="#d6f9e1", fg="green")
window.title("Python Turing Machine Simulator")
w.pack()
window.geometry('800x10000')
window.configure(background='#d6f9e1')
window.attributes('-fullscreen', True)

w = Canvas(window, width=720, height=360)
filename = PhotoImage(file = "BENNY.gif")
image = w.create_image(, 180, image=filename, anchor ='n')

w.pack()

def run():
    os.system('turingforgui.py')

run_btn = Button(window, text="Run", bg="#70f23c", fg="black",command=run)

# this will run until turing machine is done executing, then will open gui in background
t = tmclass.TM("2comp", str(input("Enter the input string: ")+ " "))

while(input()!= 'x' and t.accept is False and t.reject is False):
    t.runTM()
    
def openfile():
    return filedialog.askopenfilename()

loadbutton = ttk.Button(window, text="Load", command=openfile) 
exit_button = Button(window, text='Quit', bg="#ffbfaf", command=window.destroy)
loadbutton.pack()
run_btn.pack()
exit_button.pack()

for i in range(len(t.tapeString)):
    x = i + 1
    w.create_line('{0}c 7c {0}c 7.6c'.format(x+2), width=1, offset = '10c, 10c', fill = "#00f")
    w.create_text('{}.5c 7.5c'.format(x+2), text=t.tapeString[i], anchor='e', fill = "#00f")            
    w.pack()

window.mainloop()