from curses.ascii import isalpha
from doctest import TestResults
from ssl import Options
from tkinter import *
from functools import partial
from tkinter import messagebox



def newwindow():

    tk_welcome.destroy()


    from tkinter import messagebox
    import time
  

    root = Tk()
    root.geometry('400x300')
    

    def revert():
        root.configure(background='gray20')
        

    def blue():
        root.configure(background='cadetblue1')
        

    def purple():
        root.configure(background='darkorchid2')
       


    def beige():
        root.configure(background='bisque1')
     


    def help_user():

            help = Toplevel(root)
            help.geometry('230x250')
            help.title("help")

            edit_label = Label(help, text="Edit button guide", bg="white", fg="black")
            edit_label.grid(row=0, column=1)

            edit_guide = Label(help, text="To edit, click a task in the list,\n type your new entry in the entry box\n and click edit")
            edit_guide.grid(row=1, column=1)


    def create():
        win = Toplevel(root)

        


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


    def submitnew():

        def verify_am_pm():
            am_or_pm = am_pm_entry.get()
            if am_or_pm == "AM":
                return True
            if am_or_pm == "PM":
                return True
            else:
                return False


   
        def verify_time():
            
            time = time_entry.get()

            if time != "":
                try:
                    if  float(time) < 12 and float(time) > 0:
                        return True
                    else: 
                        return False

                except: 
                    ValueError
                    return False

            if len(time) == 0:
                
                return False

            if not time.isalpha:
                return False

        
                
            else:
                return False

        def verify_task():
            time_value_warning = Label(task, text="Please enter a value in between 0 and 12", fg="red")
            am_pm_warning = Label(task, text="please enter AM or PM", fg="red")
            entry_syntax_warning = Label(task, text="Please enter text", fg="red")
            event = event_entry.get()
            time = time_entry.get() + am_pm_entry.get()
            


            if event != "" and verify_time() == True and verify_am_pm() == True:
                task_lb.insert(END, event)
                event_entry.delete(0, "end")

                time_lb.insert(END, time)
                time_entry.delete(0, "end")

                
                task.destroy()
                edit_button.place(x=15, y=5)


            elif event != "" and verify_time() == False and verify_am_pm() == True:
                print("1111")

                entry_syntax_warning.grid_forget()
                time_value_warning.grid(row=6, columnspan=2)
            
                
                

            elif event != "" and verify_time() == True and verify_am_pm() == False:
                am_pm_warning.grid(row=8, columnspan=2)
                entry_syntax_warning.grid_forget()
                time_value_warning.grid_forget()


            
                

            elif len(event)==0:
                
                entry_syntax_warning.grid(row=6, columnspan=2)
                
                

        task = Toplevel(root)
        task.title("task entry")
        task.geometry('250x300')

        blank_label = Label(task, text="")
        blank_label.grid(row=3, column=0)

        Label(task, text="").grid(row=2, column=0)

        Label(task, bg="white", fg="black", text="What task do you have to complete").grid(row=0, column=0, columnspan=2)

        Label(task, bg="white", fg="black", text="What time (12h scale)").grid(row=3, column=0, sticky="w")

        Label(task, bg="white", fg="black", text="AM or PM?").grid(row=3, column=1)#, sticky="e")

       

        words = StringVar()
        event_entry = Entry(task, textvariable=words)
        event_entry.grid(row=1, column=0, columnspan=2)

        words = StringVar()
        am_pm_entry = Entry(task, textvariable=words, width=10)
        am_pm_entry.grid(row=4, column=1)

        words = StringVar()
        time_entry = Entry(task, textvariable=words, width=13)
        time_entry.grid(row=4, column=0)

        task_submit = Button(task, text="submit", fg="green", command=lambda:[verify_am_pm(), verify_task(), verify_time()])
        task_submit.grid(row=5, columnspan=2)



    message_label = Label(root, text="Warning, please enter task", fg="red")
    message_label.place(x=139, y=150)

    message_label_blocker = Label(root, text="", width=25)
    message_label_blocker.place(x=110, y=150)

    def edit_current_time():

        def verify_edit_time():
            if float(time) < 24 and float(time) > 0:
                return True

            else:
                return False
        
        def verify_am_pm():
            am_or_pm = edit_time.get()
            if am_or_pm == "AM":
                return True
            if am_or_pm == "PM":
                return True
            else:
                return False


        
        for item in time_lb.curselection():
            time = edit_time.get()

            if verify_edit_time == True and verify_am_pm == True:
                
                time_lb.delete(item)
                time_lb.insert(END, time)
                edit_time.delete(0, "end")
            
            else:
                

                edit_value_warning = Label(root, text="Invalid time value", fg="red")
                edit_value_warning.place(x=265, y=295)



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

    def insert_editing_widgets():
        am_pm.place(x=350,y=235)
        am_pm_label.place(x=350,y=213)

        edit_time.place(x=243, y=235)
        time_label.place(x=245, y=213)

        edit_entry.place(x=43, y=235)
        insert_time_edit.place(x=277, y=263)
        insert_event_edit.place(x=76, y=263)
        entry_label.place(x=66, y=213)
       

# title of the app
    root.title('Event Planner')
    root.geometry('440x340')
    root.resizable(False, False)
    root.configure(background='gray20')

#settings button
    settings_button = Button(root, text="⚙️️", command=create)
    settings_button.place(x=366, y=5)

#help button
    help_button = Button(root, text="Help", command=help_user)
    help_button.place(x=362, y=35)

#task listbox
    task_lb = Listbox(root, width=22, height=8)
    task_lb.place(x=90, y=10)
   
#time listbox
    time_lb = Listbox(root, width=5, height=8)
    time_lb.place(x=300, y=10)
    
#task listbox rendering
    task_list = []

#time listbox rendering
    time_list = []

#inserting task border/holder into task listbox
    for item in task_list:
        task_lb.insert(END, item)

#inserting time border/holder into time listbox
    for item in time_list:
        time_lb.insert(END, item)


#button that inserts the editing widgets into the screen
    edit_button = Button(root, text="Edit", command=lambda: [insert_editing_widgets()])
    



    
#button to bring up task creating window
    task_button = Button(root, text="Enter a new task", fg="green", command=submitnew, relief='solid')
    task_button.place(x=155, y=170)


#label stating to enter new time
    time_label = Label(root, text="Enter new time")
    

#entry box to edit the time a task needs to take place
    words = StringVar()
    edit_time = Entry(root, textvariable=words, width=10)


    words = StringVar()
    am_pm = Entry(root, textvariable=words, width=4)

    am_pm_label = Label(root, text="AM/PM")

    #options = [
    #    "AM",
    #    "PM"
    #]

    #variable = StringVar()
    #variable.set("AM")
    #am_pm = OptionMenu(root, variable, *options)
    
    

#button to insert the new time
    insert_time_edit = Button(root, text="Submit", command=edit_current_time, fg="green")
    

#entry box to edit the task entered
    words = StringVar()
    edit_entry = Entry(root, textvariable=words, width=15)
    

#button to insert the new task
    insert_event_edit = Button(root, text="Submit", command=edit_current_event, fg="green")
    

#label telling the user to enter to enter a new word
    entry_label = Label(root, text="Enter new word")
    
#running the code
    root.mainloop()


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
        placeholder_label.grid_forget()
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
