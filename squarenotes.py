import tkinter
from tkinter import *
from tkinter.colorchooser import *

def change_color():
    return askcolor()[1]
def main(self,color="#1d1f22"):
    root = tkinter.Tk()
    root.wm_title("SquareNotes")
    canvas = tkinter.Canvas(root, bg=color, borderwidth=0, highlightthickness=0,)
    entry = tkinter.Text(canvas, width=16, height=8, font=(" ",20," "),fg="white",bg=color, highlightthickness=0)
    entry.tag_configure("center", justify="center")
    entry.insert("1.0","\n\n\n")
    entry.tag_add("center","1.0","end")
    root.bind("<Command n>", main)
    root.bind("<Command w>", root.destroy)
    root.bind("<Command c>", lambda a : entry.configure(bg=change_color()))
    root.bind("<Command C>", lambda a : entry.configure(fg=change_color()))
    root.bind("<Command p>", lambda a: entry.configure(font=(" ",int(entry.cget("font").split()[2])+1, " ")))
    root.bind("<Command o>", lambda a: entry.configure(font=(" ",int(entry.cget("font").split()[2])-1, " ")))
    canvas.pack(expand=YES, fill=BOTH)
    entry.pack(expand=YES, fill=BOTH)
    entry.focus_set()
    root.mainloop()

main(None)
