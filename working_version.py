from doctest import TestResults
from tkinter import *
from functools import partial
from tkinter import messagebox



# tkWindow = Tk()
# tkWindow.geometry('350x130')
# tkWindow.title('main login page')

# def validateLogin(username, password):
#    print("username entered :", username.get())
#    print("password entered :", password.get())
#    return

# def validatepassword():
#    passwoord = password_Entry.get()
#    usernaame = username_Entry.get()
#    if (passwoord == "") and (usernaame == ""):
#        newwindow()
#    else:
#        messagebox.showwarning("warning", "please enter the correct login details")

def newwindow():

    tk_welcome.destroy()

    # from tkinter import *
    from tkinter import messagebox
    import time
    #    tkWindow.destroy()

    root = Tk()
    root.geometry('400x300')

    def revert():
        root.configure(background='gray20')
        blocker_label.config(background='gray20')

    def blue():
        root.configure(background='cadetblue1')
        blocker_label.config(background='cadetblue1')

    def purple():
        root.configure(background='darkorchid2')
        blocker_label.config(background='darkorchid2')

    def beige():
        root.configure(background='bisque1')
        blocker_label.config(background='bisque1')

    def create():
        win = Toplevel(root)
        def helpuser():

            help = Toplevel(win)
            help.title("help")
            help.geometry('300x300')
            edit_label = Label(help, text="Edit button guide", bg="white", fg="black")
            edit_label.grid(row=0, column=1)
            edit_guide = Label(help, text="To edit, click a task in the list,\n type your new entry in the entry box\n and click edit")
            edit_guide.grid(row=1, column=1)


        win.title("settings")
        win.geometry('300x300')
        win.grid_columnconfigure(1, weight=1)
        blank_label = Label(win, text="")
        blank_label.grid(row=1, column=0)
        colour_label = Label(win, text="select your colour:", fg="black", bg="white")
        colour_label.grid(row=0, column=0)
        button_g = Button(win, text="revert colour", command=revert)
        button_g.grid(row=2, column=0)
        button_b = Button(win, text="blue", command=blue)
        button_b.grid(row=3, column=0)
        button_p = Button(win, text="purple", command=purple)
        button_p.grid(row=4, column=0)
        button_be = Button(win, text="beige", command=beige)
        button_be.grid(row=5, column=0)

        help_button = Button(win, text="Help", command=helpuser)
        help_button.grid(row=0, column=1)

    # root = Tk()

    def submitnew():
        
        

        
        
        def verify_task():
            entry_syntax_warning = Label(task, text="Please enter text", fg="red")
            event = event_entry.get()


            if event != "" and verify_time() ==True:
                task_lb.insert(END, event)
                event_entry.delete(0, "end")


            else:
                
                entry_syntax_warning.grid(row=5, column=2)

                
                
 

        def verify_time():
            time_value_warning = Label(task, text="Please enter a value", fg="red")
            time = time_entry.get()
            try:
                int(time)
                time_lb.insert(END, time)
                time_entry.delete(0, "end")
                time_value_warning.grid_forget()
                #close_task_window()
                return True
                
                


            except ValueError:
                
                time_value_warning.grid(row=6, column=2)
                return False
                


        task = Toplevel(root)
        task.title("task entry")
        task.geometry('275x300')

        blank_label = Label(task, text="")
        blank_label.grid(row=0, column=0)

        Label(task, text="").grid(row=2, column=0)

        Button(task, bg="white", fg="black", text="What task do you have to complete").grid(row=0, column=2)

        Button(task, bg="white", fg="black", text="What time do you have to do this task").grid(row=2, column=2)

        task_submit = Button(task, text="submit", fg="green", command=lambda:[verify_task(), verify_time()])
        task_submit.grid(row=4, column=2)

        words = StringVar()
        event_entry = Entry(task, textvariable=words)
        event_entry.grid(row=1, column=2)

        words = StringVar()
        time_entry = Entry(task, textvariable=words)
        time_entry.grid(row=3, column=2)



    # def clearentry():
    #    event = event_entry.get()
    #    if event != "":
    #        lb.delete(ANCHOR)
    #    else:
    #        messagebox.showwarning("warning", "please enter text")

    message_label = Label(root, text="Warning, please enter task", fg="red")
    message_label.place(x=119, y=150)

    message_label_blocker = Label(root, text="", width=25)
    message_label_blocker.place(x=110, y=150)

    def edit_current_time():
        for item in time_lb.curselection():
            time = edit_time.get()

            if time != "":
                time_lb.delete(item)
                time_lb.insert(END, time)
                edit_time.delete(0, "end")

    def edit_current_event():

        for item in task_lb.curselection():
            event = edit_entry.get()

            if event != "":
                task_lb.delete(item)
                task_lb.insert(END, event)
                edit_entry.delete(0, "end")

                message_label_blocker.place(x=110, y=150)

            else:
                message_label_blocker.place_forget()




    def empty_lb():
        task_lb.delete(0, END)

    def delete_blocker():
        blocker_label.after(0, blocker_label.destroy())

    # title of the app
    root.title('Event Planner')
    root.geometry('400x300')
    root.resizable(False, False)
    root.configure(background='gray20')

    # frame = Frame(root)
    # frame.pack(pady=10)

    # placing entry widget and choosing what can be entered
    # words = StringVar()
    # event_entry = Entry(root, textvariable=words)
    # event_entry.place(x=105, y=150)

    # strminutes = IntVar()
    # timed_reminder = Entry(root)
    # timed_reminder.place(x=105, y=180)

    settings_button = Button(root, text="⚙️️", command=create)
    settings_button.place(x=337, y=5)

    task_lb = Listbox(root, width=22, height=8)
    task_lb.place(x=70, y=10)
    # task_lb.insert(1, 'task name')

    time_lb = Listbox(root, width=5, height=8)
    time_lb.place(x=280, y=10)
    # time_lb.insert(1, 'time',)

    task_list = []

    time_list = []

    for item in time_list:
        time_lb.insert(END, item)

    for item in task_list:
        task_lb.insert(END, item)

    # task_lb.after(3000, empty_lb)

    submit_button = Button(root, text="Enter a new task", fg="green", command=submitnew, relief='solid')
    submit_button.place(x=129, y=170)

    # clear_button = Button(root, text="clear", fg="red", command=clearentry)
    # clear_button.place(x=167, y=240)



    time_label = Label(root, text="Enter new time")
    time_label.place(x=230, y=213)

    words = StringVar()
    edit_time = Entry(root, textvariable=words, width=15)
    edit_time.place(x=203, y=235)

    insert_time_edit = Button(root, text="Submit", command=edit_current_time, fg="green")
    insert_time_edit.place(x=237, y=263)

    words = StringVar()
    edit_entry = Entry(root, textvariable=words, width=15)
    edit_entry.place(x=43, y=235)



    insert_event_edit = Button(root, text="Submit", command=edit_current_event, fg="green")
    insert_event_edit.place(x=76, y=263)

    edit_label = Label(root, text="Enter new word")
    edit_label.place(x=66, y=213)


    edit_button = Button(root, text="Edit", command=lambda: [delete_blocker()])
    edit_button.place(x=4, y=5)

    blocker_label = Label(root, bg="gray20", width=50, height=5, text="")
    blocker_label.place(x=40, y=210)

    root.mainloop()

# window

# username label and text entry box
# username_Label = Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = StringVar()
# username_Entry = Entry(tkWindow, textvariable=username)
# username_Entry.grid(row=0, column=1)
# password label and password entry box
# password_Label = Label(tkWindow, text="Password").grid(row=1, column=0)
# password = StringVar()
# password_Entry = Entry(tkWindow, textvariable=password, show="*")
# password_Entry.grid(row=1, column=1)

# validateLogin = partial(validateLogin, username, password)

# login button
# login_Button = Button(tkWindow, text="Login", command=validatepassword)
# login_Button.grid(row=4, column=1)



tk_welcome = Tk()
tk_welcome.geometry('385x350')
tk_welcome.title('Welcome')

welcome_label = Label(tk_welcome, text="Welcome!", font=("Ariel", 30))
welcome_label.grid(row=0, column=1)


desc_label = Label(tk_welcome, text="Hi there user, this is my daily use to do list application. If\nyou get stuck at any point, please "
                                       "press the help button on the\nmain page :)", font=("Ariel"))
desc_label.grid(row=2, column=1)

Label(tk_welcome, text="").grid(row=3, column=1)

name_ask_label = Label(tk_welcome, text="What should I call you?")
name_ask_label.grid(row=4, column=1)


words = StringVar()
name_entry = Entry(tk_welcome, textvariable=words)
name_entry.grid(row=5, column=1)



def place_name():
    name = name_entry.get()


    if len(name) == 0:
        placeholder_label.grid_forget()
        placeholder_label.grid_forget()


        warning_label.grid(row=7, column=1)

    elif not name.isalpha():
        warning_text_label.grid(row=7, column=1)
        warning_label.grid_forget()


    else:
        warning_label.grid_forget()
        name_entry.grid_forget()
        name_ask_label.grid_forget()
        enter_button.grid_forget()
        warning_text_label.grid_forget()
        skip_button.grid_forget()

        continue_button.grid(row=8, column=1)

        Label(tk_welcome, text="").grid(row=4, column=1)

        name_label.config(text=f"Hello there, {name}. Press continue when ready.")
        name_label.grid(row=5, column=1)





warning_label = Label(tk_welcome, text="Warning, please enter name.", fg="red")

warning_text_label = Label(tk_welcome, text="Please enter letters only", fg="red")

enter_button = Button(tk_welcome, text="Enter", fg="green", command=place_name)
enter_button.grid(row=6, column=1)

name_label = Label(tk_welcome, text="")


placeholder_label = Label(tk_welcome)
placeholder_label.grid(row=7, column=1)

skip_button = Button(tk_welcome, text="skip", command=newwindow)
skip_button.grid(row=8, column=1)


continue_button = Button(tk_welcome, text="Continue", command=newwindow)


tk_welcome.mainloop()
