import tkinter
from tkinter import *
from tkinter.colorchooser import *
import tkinter.font as fonts

selectedfont = "Helvetica"

def select_font(font):
    global selectedfont
    selectedfont = font

def show_fonts():
    fontroot = tkinter.Tk()
    fontroot.wm_title("Fonts")
    fontcanvas = tkinter.Canvas(fontroot, highlightthickness=0,bg="#1d1f22",height=430,width=200)
    fontbutton1 = tkinter.Button(fontcanvas,width=20,text="Helvetica",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Helvetica"),command=lambda : [fontroot.quit(),select_font("Helvetica")])
    fontbutton2 = tkinter.Button(fontcanvas,width=27,text="Times",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Times"),command=lambda : [fontroot.quit(),select_font("Times")])
    fontbutton3 = tkinter.Button(fontcanvas,width=20,text="Courier",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Courier"),command=lambda : [fontroot.quit(),select_font("Courier")])
    fontbutton4 = tkinter.Button(fontcanvas,width=23,text="Chalkboard",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Chalkboard"),command=lambda : [fontroot.quit(),select_font("Chalkboard")])
    fontbutton5 = tkinter.Button(fontcanvas,width=18,text="Papyrus",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Papyrus"),command=lambda : [fontroot.quit(),select_font("Papyrus")])
    fontbutton6 = tkinter.Button(fontcanvas,width=20,text="Copperplate",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Copperplate"),command=lambda : [fontroot.quit(),select_font("Copperplate")])
    fontbutton7 = tkinter.Button(fontcanvas,width=23,text="Impact",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Impact"),command=lambda : [fontroot.quit(),select_font("Impact")])
    fontbutton8 = tkinter.Button(fontcanvas,width=20,text="Chalkduster",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Chalkduster"),command=lambda : [fontroot.quit(),select_font("Chalkduster")])
    fontbutton9 = tkinter.Button(fontcanvas,width=27,text="Futura",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Futura"),command=lambda : [fontroot.quit(),select_font("Futura")])
    fontbutton10 = tkinter.Button(fontcanvas,width=20,text="Herculanum",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Herculanum"),command=lambda : [fontroot.quit(),select_font("Herculanum")])
    fontbutton11 = tkinter.Button(fontcanvas,width=18,text="Noteworthy",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Noteworthy"),command=lambda : [fontroot.quit(),select_font("Noteworthy")])
    fontbutton12 = tkinter.Button(fontcanvas,width=20,text="Phosphate",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Phosphate"),command=lambda : [fontroot.quit(),select_font("Phosphate")])
    fontbutton13 = tkinter.Button(fontcanvas,width=27,text="SignPainter",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("SignPainter"),command=lambda : [fontroot.quit(),select_font("SignPainter")])
    fontbutton14 = tkinter.Button(fontcanvas,width=23,text="Trattatello",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Trattatello"),command=lambda : [fontroot.quit(),select_font("Trattatello")])

    fontcanvas.create_window(100,20,window=fontbutton1)
    fontcanvas.create_window(100,50,window=fontbutton2)
    fontcanvas.create_window(100,80,window=fontbutton3)
    fontcanvas.create_window(100,110,window=fontbutton4)
    fontcanvas.create_window(100,140,window=fontbutton5)
    fontcanvas.create_window(100,170,window=fontbutton6)
    fontcanvas.create_window(100,200,window=fontbutton7)
    fontcanvas.create_window(100,230,window=fontbutton8)
    fontcanvas.create_window(100,260,window=fontbutton9)
    fontcanvas.create_window(100,290,window=fontbutton10)
    fontcanvas.create_window(100,320,window=fontbutton11)
    fontcanvas.create_window(100,350,window=fontbutton12)
    fontcanvas.create_window(100,380,window=fontbutton13)
    fontcanvas.create_window(100,410,window=fontbutton14)
    fontcanvas.pack()
    fontroot.mainloop()
    print(selectedfont)
    fontroot.destroy()
    return selectedfont

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
    entry = tkinter.Text(canvas, width=16, height=8, font=("Helvetica",20,"normal", "roman"),fg="white",bg=color, highlightthickness=0,insertbackground="white",wrap="word")
    entry.tag_configure("center", justify="center")
    entry.insert("1.0","\n\n\n")
    entry.tag_add("center","1.0","end")
    root.bind("<Command n>", main)
    root.bind("<Command w>", root.destroy)
    root.bind("<Command c>", lambda a: [entry.configure(bg=change_color()), canvas.configure(bg=entry.cget("bg"))])
    root.bind("<Command C>", lambda a: entry.configure(fg=change_color()))
    root.bind("<Command p>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])+1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command o>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])-1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command b>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), toggle_bold(str(entry.cget("font").split()[2])),entry.cget("font").split()[3])))
    root.bind("<Command i>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), entry.cget("font").split()[2],toggle_italic(entry.cget("font").split()[3]))))
    root.bind("<Command f>", lambda a: entry.configure(font=(show_fonts(),int(entry.cget("font").split()[1]), entry.cget("font").split()[2],entry.cget("font").split()[3])))
    entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas.pack(expand=YES,fill=BOTH)
    entry.focus_set()
    root.mainloop()

main(None)
