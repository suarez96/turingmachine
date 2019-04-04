
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# whenever you want to reference a function or anything from the turingforguifile, just use tm.<whateverFunction>
import turingforgui as tm

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

# this will run until turing machine is done executing, then will open gui in background
t = tm.TM("2comp.txt", str(input("Enter the input string: ")+ " "))
while(input()!= 'x' and t.accept is False and t.reject is False):
    t.runTM()

def openfile():
    return filedialog.askopenfilename()

loadbutton = ttk.Button(window, text="Load", command=openfile) 
exit_button = Button(window, text='Quit', bg="#ffbfaf", command=window.destroy)
loadbutton.pack()
run_btn.pack()
exit_button.pack()

for i in range(2):
    w = Label(window,justify = 'left', text="adf", borderwidth = 2, relief = 'solid')
    w.pack()

window.mainloop()


'''from tkinter import *
from tkinter import ttk

class CanvasRulerDemo(ttk.Frame):

    def __init__(self, isapp=True, name='canvasrulerdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Canvas Ruler Demo')
        self.isapp = isapp
        self._create_demo_panel()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP)
        self.canvas = Canvas(width='20c', height='20c')
        self.canvas.pack(in_=demoPanel, side=TOP, fill=X)

        self._draw_ruler()


    def _draw_ruler(self):
        for i in range(15): #will be length of char array
            x = i + 1
            self.canvas.create_line('{0}c 1c {0}c 0.6c'.format(x), width=1)
            self.canvas.create_text('{}.5c 1c'.format(x), text='x', anchor='sw')

        # add tab symbol to 'well'
        x = self.canvas.winfo_pixels('15.55c')
        y = self.canvas.winfo_pixels('1.2c')
        self.canvas.addtag_withtag('well', self._draw_tab(x, y))

    def _draw_tab(self, x, y):
        # # create a filled triangle to represent a tab stop
        size = self.canvas.winfo_fpixels('.2c')
        tab = self.canvas.create_polygon(x, y, x + size, y + size, x - size, y + size)
        return tab

if __name__ == '__main__':
    CanvasRulerDemo().mainloop()'''