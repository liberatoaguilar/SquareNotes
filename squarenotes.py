import tkinter
from tkinter import *
from tkinter.colorchooser import *
import tkinter.font as fonts

selectedfont = "Helvetica"
count = 0
alpha = 1.0
bulletoraster = " • "

def aster_or_num(text):
    print(text)
    if text[0][0] == "1" and text[0][1] == ".":
        return "1. "
    elif text[0][0] == " " and text [0][1] == "•":
        return " •"

def isint(text):
    try:
        test = int(text.replace(".","").replace(" ",""))
        return True
    except:
        return False

def add_bullet(entry):
    for x in range(int(float(entry.index("end")))):
        if entry.get("0.0","0.0+3char") == " • ":
            if entry.get(float(x),str(float(x))+"+2char") != " •":
                entry.insert(float(x)," • ")
    for x in range(int(float(entry.index("end")))-1):
        if entry.get("0.0","0.0+3char") == "1. ":
            if entry.get(float(x+1),str(float(x+1))+"+2char") != str(int(x+1))+".":
                entry.insert(float(x+1),str(int(x+1))+". ")
                if isint(entry.get(str(float(x+1))+"+3chars",str(float(x+1))+" lineend")):
                    entry.delete(str(float(x+1))+"+3chars",str(float(x+1))+" lineend")

def delete_aster(text):
    global bulletoraster
    bulletfound = "None"
    if text.split()[0][0] == "*":
        bulletfound = "4.0 + 1 chars"
        bulletoraster = " • "
    if text.split()[0][0] == "1" and text.split()[0][1] == ".":
        bulletfound = "4.0 + 1 chars"
        bulletoraster = "1. "
    return bulletfound

def check_for_aster(text):
    bulletfound = "None"
    try:
        if text.split()[0] == "*" or text.split()[0] == "1" and text.split()[1] == ".":
            bulletfound = "center"
    except:
        bulletfound = "center"
    return bulletfound

def select_font(font):
    global selectedfont
    selectedfont = font

def set_alpha(num,root):
    global alpha
    alpha = num
    root.attributes("-alpha",str(num))

def show_prefs(entry,root):
    global alpha
    prefsroot = tkinter.Tk()
    prefsroot.wm_title("Preferences")
    prefscanvas = tkinter.Canvas(prefsroot, highlightthickness=0,bg="#1d1f22",height=300,width=440)
    title = tkinter.Entry(prefscanvas,bd=0,bg="#cecece",highlightbackground="#cecece",highlightcolor="#cecece")
    titlelabel = tkinter.Label(prefscanvas,text="Set Title",bg="#1d1f22",fg="white")
    title.insert("end","SquareNotes")
    titlebutton = tkinter.Button(prefscanvas,width=10,text="Set",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Helvetica"),command=lambda : root.wm_title(title.get()))
    translucent_number = Scale(prefscanvas, from_=0.1, to=1.0, orient=HORIZONTAL, resolution=0.1, length=170, label="Translucency",bd=0,bg="#1d1f22",activebackground="#1d1f22",fg="white",command= lambda a: set_alpha(a,root))
    translucent_number.set(alpha)
    prefscanvas.create_window(120,40,window=translucent_number)
    prefscanvas.create_window(70,120,window=titlelabel)
    prefscanvas.create_window(120,155,window=title)
    prefscanvas.create_window(120,195,window=titlebutton)
    prefscanvas.pack()
    prefsroot.mainloop()

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
    fontroot.destroy()
    return selectedfont

def toggle_lock(entry):
    if entry == "disabled":
        return "normal"
    elif entry == "normal":
        return "disabled"

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

def change_bg_color():
    return askcolor()[1]

def change_color(entry):
    global count
    color = askcolor()[1]
    if entry.tag_ranges('sel'):
        entry.tag_add('colortag_' + str(count), SEL_FIRST,SEL_LAST)
        entry.tag_configure('colortag_' + str(count), foreground=color)
        count += 1
    else:
        entry.config(foreground=color)

def main(self,color="#1d1f22"):
    root = tkinter.Tk()
    root.wm_title("SquareNotes")
    canvas = tkinter.Canvas(root, highlightthickness=0,bg=color,height=200,width=200)
    entry = tkinter.Text(canvas, width=16, height=8, font=("Helvetica",20,"normal", "roman"),fg="white",bg=color, highlightthickness=0,insertbackground="white",wrap="word")
    entry.tag_configure("center", justify="center")
    entry.insert("1.0","\n\n\n")
    entry.tag_add("center","0.0","end")
    root.bind("<Command n>", main)
    root.bind("<Command w>", root.destroy)
    root.bind("<Command c>", lambda a: [entry.configure(bg=change_bg_color()), canvas.configure(bg=entry.cget("bg"))])
    root.bind("<Command C>", lambda a: change_color(entry))
    root.bind("<Command p>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])+1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command o>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])-1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command b>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), toggle_bold(str(entry.cget("font").split()[2])),entry.cget("font").split()[3])))
    root.bind("<Command i>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), entry.cget("font").split()[2],toggle_italic(entry.cget("font").split()[3]))))
    root.bind("<Command f>", lambda a: entry.configure(font=(show_fonts(),int(entry.cget("font").split()[1]), entry.cget("font").split()[2],entry.cget("font").split()[3])))
    root.bind("<space>", lambda a: [entry.tag_delete(check_for_aster(entry.get("2.0","2.0+3char"))),entry.delete("0.0",delete_aster(entry.get("0.0","end"))),entry.replace("0.0","0.0+1char",bulletoraster)])
    root.bind("<Return>", lambda a: add_bullet(entry))
    root.bind("<Command l>", lambda a: entry.config(state=toggle_lock(str(entry.cget("state")))))
    root.bind("<Command ,>", lambda a: show_prefs(entry,root))
    entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas.pack(expand=YES,fill=BOTH)
    entry.focus_set()
    root.mainloop()

main(None)
