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

def delete_aster(text,entry):
    global bulletoraster
    bulletfound = "None"
    print(text.split())
    if text.split()[0][0] == "*":
        bulletfound = "4.0 + 1 chars"
        bulletoraster = " • "
    if text.split()[0][0] == "1" and text.split()[0][1] == "." and len(text.split()) <= 1:
        print('del')
        bulletfound = "4.0 + 1 chars"
        bulletoraster = "1."
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

def show_prefs(entry,root,checklist):
    global alpha
    prefsroot = tkinter.Tk()
    prefsroot.wm_title("Preferences")
    prefscanvas = tkinter.Canvas(prefsroot, highlightthickness=0,bg="#1d1f22",height=300,width=240)
    title = tkinter.Entry(prefscanvas,bd=0,bg="#cecece",highlightbackground="#cecece",highlightcolor="#cecece")
    titlelabel = tkinter.Label(prefscanvas,text="Set Title",bg="#1d1f22",fg="white")
    title.insert("end","SquareNotes")
    titlebutton = tkinter.Button(prefscanvas,text="Set",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Helvetica"),command=lambda : root.wm_title(title.get()))
    translucent_number = Scale(prefscanvas, from_=0.1, to=1.0, orient=HORIZONTAL, resolution=0.1, length=170, label="Translucency",bd=0,bg="#1d1f22",activebackground="#1d1f22",fg="white",command= lambda a: set_alpha(a,root))
    translucent_number.set(alpha)
    convert_to_checklist = Button(prefscanvas,width=20,text="Convert to Checklist",bg="#1d1f22",fg="white",bd=0,highlightthickness=0,activebackground="#1d1f22",highlightbackground="#1d1f22",font=("Helvetica"),command=lambda : checklist_main(entry))
    prefscanvas.create_window(120,40,window=translucent_number)
    prefscanvas.create_window(70,120,window=titlelabel)
    prefscanvas.create_window(120,155,window=title)
    prefscanvas.create_window(120,195,window=titlebutton)
    if checklist == "normal":
        prefscanvas.create_window(120,240,window=convert_to_checklist)
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

def change_all_colors(canvas,bgfg):
    color = change_bg_color()
    for x in canvas.winfo_children():
        if bgfg == "bg":
            x.configure(bg=color)
        elif bgfg == "fg":
            x.configure(activeforeground=color)

def checklist_main(entry,color="#1d1f22"):
    if entry.get('0.0','0.0+2char') == " •":
        text = entry.get('0.0','end')
        text = text.replace('•',"").split("\n")
        del text[-1]
        for x in range(len(text)):
            if text[-1] == '  ':
                del text[-1]
        print(text)

        counter = 0
        root = tkinter.Tk()
        root.wm_title("Checklist")
        canvas = tkinter.Canvas(root, highlightthickness=0,bg=entry.cget("bg"),height=200,width=200)
        for x in text:
            state = BooleanVar()
            state.set(True)
            check = Checkbutton(canvas, text=x, var=state,bg=entry.cget("bg"),font=(entry.cget("font").split()[0],20,entry.cget("font").split()[2],entry.cget("font").split()[3]))
            check.place(x=20,y=10+(counter*27))
            counter += 1
        root.bind("<Command n>", main)
        root.bind("<Command w>", root.destroy)
        root.bind("<Command c>", lambda a: [change_all_colors(canvas,"bg"), canvas.configure(bg=check.cget("bg"))])
        root.bind("<Command ,>", lambda a: show_prefs(entry,root,"checklist"))
        canvas.pack(expand=YES,fill=BOTH)
        root.mainloop()

def main(self,color="#1d1f22"):
    root = tkinter.Tk()
    root.wm_title("SquareNotes")
    entry = tkinter.Text(root, width=16, height=8, font=("Helvetica",20,"normal", "roman"),fg="white",bg=color, highlightthickness=0,insertbackground="white",wrap="word",padx=20,pady=20)
    entry.tag_configure("center", justify="center")
    entry.insert("1.0","\n\n\n")
    entry.tag_add("center","0.0","end")
    root.bind("<Command n>", main)
    root.bind("<Command w>", root.destroy)
    root.bind("<Command c>", lambda a: [entry.configure(bg=change_bg_color())])
    root.bind("<Command C>", lambda a: change_color(entry))
    root.bind("<Command p>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])+1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command o>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1])-1, entry.cget("font").split()[2], entry.cget("font").split()[3])))
    root.bind("<Command b>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), toggle_bold(str(entry.cget("font").split()[2])),entry.cget("font").split()[3])))
    root.bind("<Command i>", lambda a: entry.configure(font=(entry.cget("font").split()[0],int(entry.cget("font").split()[1]), entry.cget("font").split()[2],toggle_italic(entry.cget("font").split()[3]))))
    root.bind("<Command f>", lambda a: entry.configure(font=(show_fonts(),int(entry.cget("font").split()[1]), entry.cget("font").split()[2],entry.cget("font").split()[3])))
    root.bind("<space>", lambda a: [entry.tag_delete(check_for_aster(entry.get("2.0","2.0+3char"))),entry.delete("0.0",delete_aster(entry.get("0.0","end"),entry)),entry.replace("0.0","0.0+1char",bulletoraster)])
    root.bind("<Return>", lambda a: add_bullet(entry))
    root.bind("<Command l>", lambda a: entry.config(state=toggle_lock(str(entry.cget("state")))))
    root.bind("<Command ,>", lambda a: show_prefs(entry,root,"normal"))
    entry.pack(expand=YES,fill=BOTH)
    entry.focus_set()
    root.mainloop()

main(None)
