import tkinter as tk
root=tk.Tk()
root.geometry("720x720")

frame=tk.Frame(root,bg='lightblue')
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

def page1():
    label=tk.Label(frame,text='this is the page1')
    label.place(relx=0.3,rely=0.4)

def page2():
    label=tk.Label(frame,text='this is the page2')
    label.place(relx=0.3,rely=0.4)

def page3():
    label=tk.Label(frame,text='this is the page3')
    label.place(relx=0.3,rely=0.4)

bt=tk.Button(root,text='page1',command=page1)
bt.grid(column=0,row=0)

bt1=tk.Button(root,text='page2',command=page2)
bt1.grid(row=0,column=1)

bt2=tk.Button(root,text='page3',command=page3)
bt2.grid(row=0,column=2)

root.mainloop()