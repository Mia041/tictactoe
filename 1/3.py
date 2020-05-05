import tkinter as tk

def show_entry_fields():
    master = tk.Tk()

    w= tk.Canvas (master, width=600, height =600)
    w.pack()

    w.create_rectangle(0,0,600,200,fill="blue")
    w.create_rectangle(0,200,600,400,fill="yellow")
    w.create_rectangle(0,400,600,600,fill="red")
    w.grid(row=0, column=1)
    w.grid(row=1, column=1)
    w.create_text(300,300,text=e1.get())


    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()
