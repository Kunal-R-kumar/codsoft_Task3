from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from random import randint,choice
import os
root=Tk()
root.title("Password Generator")
sw,sh=root.winfo_screenwidth(),root.winfo_screenheight()
root.attributes("-fullscreen",True)
bg=ImageTk.PhotoImage(Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\pswd.png").resize((sw,sh)))
bgl=Label(image=bg)
bgl.pack()
fntsize=min(sw//30,sh//30)
def only_number(ip):
    if (ip.isdigit()and int(ip)<21) or ip=="":return True 
    else:return False
onc = root.register(only_number)
Label(text="Password Generator",font=("Times",fntsize,"italic"),fg="#00ff8c",bg="black").place(relx=0.22,rely=0.126)
Label(text="Required Length:",font=("Times",fntsize,),fg="#00ff8c",bg="black").place(relx=0.1,rely=0.35)
Label(text="Strength:",font=("Times",fntsize,),fg="#00ff8c",bg="black").place(relx=0.1,rely=0.43)
Label(text="Type:",font=("Times",fntsize,),fg="#00ff8c",bg="black").place(relx=0.1,rely=0.51)
Label(text="Generated Password:",font=("Times",fntsize,),fg="#00ff8c",bg="black").place(relx=0.1,rely=0.59)
e1=Entry(fg="white",bg="#152449",highlightthickness=1,highlightbackground="#00ff8c",highlightcolor="#00ff8c",font=("Times",fntsize-8),insertbackground="white",validate="key", validatecommand=(onc,'%P'))
e1.place(relx=0.35,rely=0.355)
s,t,c=IntVar(value=5),IntVar(value=1),IntVar(value=3)
def types():
    for i in [r1,r2,r3,r4]:
        try:i.place_forget()
        except:continue
    if s.get()!=7:
        r1.place(relx=0.3,rely=0.525)
        r2.place(relx=0.44,rely=0.525)
    else:
        r4.place(relx=0.3,rely=0.525)
        r3.place(relx=0.44,rely=0.525) 
style=ttk.Style()
style.configure("TRadiobutton",foreground="#00ff8c",background="black",font=("Times",fntsize-8))
style.configure("TCheckbutton",foreground="#00ff8c",background="black",font=("Times",fntsize-8))
ttk.Radiobutton(text="Low",style="TRadiobutton",value=3,command=types,variable=s).place(relx=0.3,rely=0.44)
ttk.Radiobutton(text="Medium",style="TRadiobutton",value=5,command=types,variable=s).place(relx=0.4,rely=0.44)
ttk.Radiobutton(text="High",style="TRadiobutton",value=7,command=types,variable=s).place(relx=0.5,rely=0.44)
r1=ttk.Radiobutton(text="Alphabetical",style="TRadiobutton",value=1,variable=t)
r2=ttk.Radiobutton(text="Alphanumerical",style="TRadiobutton",value=2,variable=t)
r3=ttk.Checkbutton(text="include Special Char",onvalue=3,offvalue=2,variable=c,style="TCheckbutton")
r4=Label(text="Alphanumerical",fg="#00ff8c",bg="black",font=("Times",fntsize-8))
types()
def high(l):
    global ps;ps,up,lo,sp,num="",0,0,0,0
    for i in range(l) :
        b=randint(0,c.get())
        if b==0:ps+=chr(randint(65,90))
        elif b==1:ps+=chr(randint(97,122 ))
        elif b==2:ps+=str(choice("0123456789"))
        elif b==3:ps+=str(choice('~`!@#$%^&*()-+={[}]|\:;<>.?/'))
    for i in ps:
        if i.isupper():up+=1
        elif i.islower():lo+=1
        elif i.isdigit():num+=1
        else:sp+=1
    if up==0 or lo==0 or num==0 or (sp==0 and c.get()==3):
        high(l)
    pslbl.configure(text=f"{ps}")
def nrml(st,l,n,s1):
    global ps;ps=f"{chr(st)}"
    if s1==5:ps=ps.upper()
    al=l//n
    while len(ps)!=al:
        if ord(ps[-1])<122-s1 & ord(ps[-1])>97:ps+=chr(ord(ps[-1])+randint(0,s1))
        else:ps+=chr(randint(97,122-s1))
    while len(ps)!=l:
        if ord(ps[-1])<57-s1:ps+=str(int(ps[-1])+randint(0,s1))
        else:ps+=chr(randint(48,57-s1))   
    pslbl.configure(text=f"{ps}")
st,ps=0,""
def psgn():
    global st;st+=1
    if s.get()==7:high(int(e1.get()))                 
    else:nrml(randint(97,122),int(e1.get()),t.get(),s.get())   
    if st<8:root.after(60,psgn)
    else:st=0;b1.config(state=NORMAL);b2.config(state=NORMAL);p1.configure(text="Generated");p1.after(700,lambda:p1.configure(text=""))
def press():
    b2.config(state=DISABLED)
    if e1.get()!="" and (int(e1.get()))>3:b1.config(state=DISABLED);psgn()
    else:p1.configure(text="Lesser length than 4");p1.after(700,lambda:p1.configure(text=""))
def clip():
        root.clipboard_clear()
        root.clipboard_append(ps)
        root.update() 
        p1.configure(text="Text copied");p1.after(700,lambda:p1.configure(text=""))
pslbl=Label(font=("Times",fntsize-8,UNDERLINE),bg="black",fg="#00ff8c",highlightbackground="#00ff8c",bd=1,relief=SOLID)
pslbl.place(relx=0.35,rely=0.595)
b1=Button(text="Generate",fg="#00ff8c",bg="#152449",font=(f"Times {fntsize-8} underline"),command=press,highlightbackground="#00ff8c",bd=1,relief=SOLID,cursor="hand2")
b1.place(relx=0.55,rely=0.67)
b2=Button(text="Copy",fg="#00ff8c",bg="#152449",font=(f"Times {fntsize-8} underline"),command=clip,highlightbackground="#00ff8c",bd=1,relief=SOLID,cursor="hand2",state=DISABLED)
b2.place(relx=0.45,rely=0.67)
p1=Label(text="*Length can range from 4 to 20  ",font=("Times",fntsize-7,),fg="#fff",bg="black")
p1.place(relx=0.1,rely=0.66);
root.mainloop()