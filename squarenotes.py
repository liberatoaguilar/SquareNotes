import tkinter
from tkinter import *
from tkinter.colorchooser import *

def toggle_bold(entry):
    if entry == "bold":
        return "normal"
    elif entry == "normal":
        return "bold"
def toggle_italic(entry):
    if entry == "italic":
        return "roman"
    elif entry == "roman":
        return "italic"
def change_color():
    return askcolor()[1]
def main(self,color="#1d1f22"):
    root = tkinter.Tk()
    root.wm_title("SquareNotes")
    canvas = tkinter.Canvas(root, highlightthickness=0,bg=color,height=200,width=200)
    entry = tkinter.Text(canvas, width=16, height=8, font=("Helvetica",20,"normal", "italic"),fg="white",bg=color, highlightthickness=0,insertbackground="white",wrap="word")
    entry.tag_configure("center", justify="center")
    entry.insert("1.0","\n\n\n")
    entry.tag_add("center","1.0","end")
    print(entry.cget("font").split())
    root.bind("<Command n>", main)
    root.bind("<Command w>", root.destroy)
    root.bind("<Command c>", lambda a: [entry.configure(bg=change_color()), canvas.configure(bg=entry.cget("bg"))])
    root.bind("<Command C>", lambda a: entry.configure(fg=change_color()))
    root.bind("<Command p>", lambda a: entry.configure(font=("Helvetica",int(entry.cget("font").split()[1])+1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command o>", lambda a: entry.configure(font=("Helvetica",int(entry.cget("font").split()[1])-1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command b>", lambda a: entry.configure(font=("Helvetica",int(entry.cget("font").split()[1]), toggle_bold(str(entry.cget("font").split()[2])),entry.cget("font").split()[3])))
    root.bind("<Command i>", lambda a: entry.configure(font=("Helvetica",int(entry.cget("font").split()[1]), entry.cget("font").split()[2],toggle_italic(entry.cget("font").split()[3]))))
    entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas.pack(expand=YES,fill=BOTH)
    entry.focus_set()
    root.mainloop()

main(None)
