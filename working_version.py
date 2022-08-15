from tkinter import *


# def to open the main window that
# carries out the main function of the app
def newwindow():
    # command to get rid of the welcome screen
    tk_welcome.destroy()

    # setting parent and dimensions of main window
    root = Tk()
    root.geometry('400x300')

    # defs to change colour of the main screen
    def revert():
        root.configure(background='gray20')

    def blue():
        root.configure(background='cadetblue1')

    def purple():
        root.configure(background='darkorchid2')

    def beige():
        root.configure(background='bisque1')

    def help_user():

        help_me = Toplevel(root)
        help_me.geometry('340x250')
        help_me.title("help")

        edit_label = Label(help_me, text="Edit buttonguide",
                           bg="white", fg="black")
        edit_label.grid(row=0, columnspan=2)

        edit_guide = Label(help_me, text="""To edit, click a task/time in the list,
        type your new entry into one of the entry boxes\n and click submit.""")
        edit_guide.grid(row=1, columnspan=2)

    # creating a window to alter app colour
    def create():
        win = Toplevel(root)

        win.title("settings")
        win.geometry('120x300')
        win.grid_columnconfigure(1, weight=1)
        blank_label = Label(win, text="")
        blank_label.grid(row=1, column=0)

        colour_label = Label(win, text="select your colour:",
                             fg="black", bg="white")
        colour_label.grid(row=0, column=0)

        button_g = Button(win, text="revert colour", command=revert)
        button_g.grid(row=2, column=0)

        button_b = Button(win, text="blue", command=blue)
        button_b.grid(row=3, column=0)

        button_p = Button(win, text="purple", command=purple)
        button_p.grid(row=4, column=0)

        button_be = Button(win, text="beige", command=beige)
        button_be.grid(row=5, column=0)

    # def for window to submit a new daily task
    def submitnew():

        # def to verify that entered text is am/pm or AM/PM
        def verify_am_pm():
            am_or_pm = am_pm_entry.get()
            if am_or_pm == "AM" or am_or_pm == "am":
                return True
            if am_or_pm == "PM" or am_or_pm == "pm":
                return True
            else:
                return False

        # def to verify the minutes entered
        def verify_minutes():
            minutes = minutes_time_entry.get()

            if minutes.isdigit and len(minutes) == 2:
                minutes_int = float(minutes)
                try:
                    if 60 >= minutes_int >= 0:

                        return True
                    else:
                        return False

                except ValueError:
                    return False

            if len(minutes) == 0:
                return False

            else:
                return False

        # def to check if hours entered is valid
        def verify_hours():
            hour = hour_time_entry.get()

            if hour.isdigit and len(hour) == 2 or len(hour) == 1:
                hour_int = float(hour)
                try:
                    if 12 >= hour_int >= 0:

                        return True
                    else:
                        return False

                except ValueError:
                    return False

            if len(hour) == 0:
                return False

            else:
                return False

        # verifying the hours, minutes, and AM/PM entry to
        # put them together or to bring up an error if one is not valid
        def verify_task():
            text_warning = Label(
                task, text="""Please enter valid credentials""", fg="red")
            hours = hour_time_entry.get()
            minutes = minutes_time_entry.get()
            event = event_entry.get()
            time = hours + ":" + minutes + am_pm_entry.get()

            if len(event) != 0 and verify_am_pm() == True and verify_hours() == True and verify_minutes():  # noqa
                task_lb.insert(END, event)
                event_entry.delete(0, "end")

                time_lb.insert(END, time)
                hour_time_entry.delete(0, "end")

                task.destroy()
                edit_button.place(x=15, y=5)
                clear_button.place(x=13, y=40)

            else:

                text_warning.place(x=75, y=205)

        # creating the window to create a new task
        task = Toplevel(root)
        task.title("Task Entry")
        task.geometry('320x300')

        Label(task, bg="white", fg="black",
              text="What task do you have to complete?").place(x=45, y=10)

        Label(task, bg="white", fg="black",
              text="What time? (12h scale)").place(x=10, y=75)

        Label(task, bg="white", fg="black",
              text="AM or PM?").place(x=204, y=75)

        variable_words = StringVar()
        event_entry = Entry(task, textvariable=variable_words, width=25)
        event_entry.place(x=40, y=38)

        variable_words = StringVar()
        am_pm_entry = Entry(task, textvariable=variable_words, width=8)
        am_pm_entry.place(x=198, y=100)

        variable_words = StringVar()
        hour_time_entry = Entry(task, textvariable=variable_words, width=10)
        hour_time_entry.place(x=60, y=100)

        hour_label = Label(task, text="hour:")
        hour_label.place(x=2, y=100)

        variable_words = StringVar()
        minutes_time_entry = Entry(task, textvariable=variable_words, width=10)
        minutes_time_entry.place(x=60, y=130)

        minutes_label = Label(task, text="minutes:")
        minutes_label.place(x=2, y=130)

        task_submit = Button(task, text="submit", fg="green",
                             command=lambda: [verify_am_pm(),
                                              verify_task(), verify_hours()])
        task_submit.place(x=130, y=165)

    message_label = Label(root, text="Warning, please enter task", fg="red")

    # def to edit the time in the listbox for an event
    def edit_current_time():

        # def to verify the new entered minutes
        def verify_edit_minutes():
            new_minutes = edit_time_minutes.get()

            if new_minutes.isdigit and len(new_minutes) == 2:
                minutes_int = float(new_minutes)
                try:
                    if 60 >= minutes_int >= 0:

                        return True
                    else:
                        return False

                except ValueError:
                    return False

            if len(new_minutes) == 0:
                return False

            else:
                return False

        # def to verify the new eneterd hours
        def verify_edit_hour():

            hour = edit_time_hours.get()

            if hour.isdigit and len(hour) != 0:
                hour_int = float(hour)
                try:
                    if 12 >= hour_int >= 0:

                        return True
                    else:
                        return False

                except ValueError:
                    return False

            if len(hour) == 0:
                return False

            else:
                return False

        # def to verify the new entered am/pm or AM/PM
        def verify_am_pm():
            am_or_pm = new_am_pm_entry.get()
            if am_or_pm == "AM" or am_or_pm == "am":
                return True
            if am_or_pm == "PM" or am_or_pm == "pm":
                return True
            else:
                return False

        # entering the new time into the time listbox
        for selected_item in time_lb.curselection():
            edited_hours = edit_time_hours.get()
            edited_minutes = edit_time_minutes.get()
            am_pm = new_am_pm_entry.get()

            new_time = edited_hours + ":" + edited_minutes + am_pm

            if verify_edit_hour() == True and verify_edit_minutes() == True and verify_am_pm() == True:  # noqa
                
                edit_value_warning.place_forget()

                time_lb.delete(selected_item)
                time_lb.insert(END, new_time)

                edit_time_hours.delete(0, "end")
                edit_time_minutes.delete(0, "end")
                new_am_pm_entry.delete(0, "end")

            else:
                edit_value_warning.place(x=265, y=295)

    edit_value_warning = Label(root, text="Invalid time value", fg="red")

    # def to edit an event in the event/task listbox
    def edit_current_event():

        # entering the new task/event into the listbox
        for the_selected_item in task_lb.curselection():
            event = edit_entry.get()

            if event != "":
                task_lb.delete(the_selected_item)
                task_lb.insert(END, event)
                edit_entry.delete(0, "end")
                message_label.place_forget()

            else:
                message_label.place(x=35, y=295)

    # def to empty the entire listbox
    def empty_listboxes():
        task_lb.delete(0, END)
        time_lb.delete(0, END)

    # inserting the editing widgets once the edit button is clicked
    def insert_editing_widgets():
        new_am_pm_entry.place(x=380, y=235)
        new_am_pm_label.place(x=380, y=215)

        time_label.place(x=290, y=197)

        edit_hour_label.place(x=265, y=215)

        edit_minutes_label.place(x=310, y=215)

        edit_time_hours.place(x=250, y=235)

        edit_time_minutes.place(x=310, y=235)

        edit_entry.place(x=43, y=235)
        insert_time_edit.place(x=277, y=263)
        insert_event_edit.place(x=76, y=263)
        entry_label.place(x=66, y=197)

    # title of the app
    root.title('Event Planner')
    root.geometry('440x340')
    root.resizable(False, False)
    root.configure(background='gray20')

    # settings button
    settings_button = Button(root, text="⚙️️", command=create)
    settings_button.place(x=366, y=5)

    # help button
    help_button = Button(root, text="Help", command=help_user)
    help_button.place(x=362, y=35)

    # task listbox
    task_lb = Listbox(root, width=22, height=8)
    task_lb.place(x=90, y=10)

    # time listbox
    time_lb = Listbox(root, width=6, height=8)
    time_lb.place(x=300, y=10)

    # task listbox rendering
    task_list = []

    # time listbox rendering
    time_list = []

    # inserting task border/holder into task listbox
    for item in task_list:
        task_lb.insert(END, item)

    # inserting time border/holder into time listbox
    for item in time_list:
        time_lb.insert(END, item)

    # button that inserts the editing widgets into the screen
    edit_button = Button(root,
                         text="Edit",
                         command=lambda: [insert_editing_widgets()])

    # button to bring up task creating window
    task_button = Button(root, text="Enter a new task",
                         fg="green", command=submitnew, relief='solid')
    task_button.place(x=155, y=170)

    clear_button = Button(root, text="Clear\nlist",
                          fg="red", command=empty_listboxes)

    # label stating to enter new time
    time_label = Label(root, text="Enter new time")

    edit_hour_label = Label(root, text="hour")

    edit_minutes_label = Label(root, text="minutes")

    # entry box to edit the time a task needs to take place
    entry_words = StringVar()
    edit_time_hours = Entry(root, textvariable=entry_words, width=5)

    minute_entry_words = StringVar()
    edit_time_minutes = Entry(root, textvariable=minute_entry_words, width=5)

    entry_words = StringVar()
    new_am_pm_entry = Entry(root, textvariable=entry_words, width=4)

    new_am_pm_label = Label(root, text="AM/PM")

    # button to insert the new time
    insert_time_edit = Button(root, text="Submit",
                              command=edit_current_time, fg="green")

    # entry box to edit the task entered
    words_variable = StringVar()
    edit_entry = Entry(root, textvariable=words_variable, width=15)

    # button to insert the new task
    insert_event_edit = Button(root, text="Submit",
                               command=edit_current_event, fg="green")

    # label telling the user to enter to enter a new word
    entry_label = Label(root, text="Enter new word")

    # running the code
    root.mainloop()


# title of the welcoming window
tk_welcome = Tk()
tk_welcome.geometry('365x350')
tk_welcome.title('Welcome')

# laying out various labels to welcome the user
welcome_label = Label(tk_welcome, text="Welcome!", font=("Ariel", 30))
welcome_label.grid(row=0, columnspan=3)

desc_label = Label(tk_welcome,
                   text="""Hi there user, this is my daily use to dolist application. If\nyou 
get stuck at anypoint, please press the help button on the\nmain page :)""", font="Ariel")  # noqa
desc_label.grid(row=2, columnspan=3)

Label(tk_welcome, text="").grid(row=3, columnspan=3)

name_ask_label = Label(tk_welcome, text="What should I call you?")
name_ask_label.grid(row=4, columnspan=3)

# entry to enter name
words = StringVar()
name_entry = Entry(tk_welcome, textvariable=words)
name_entry.grid(row=5, column=1)


# def to verify the name and insert it into a welcome message
def place_name():
    name = name_entry.get()

    if len(name) == 0:
        placeholder_label.grid_forget()
        placeholder_label.grid_forget()

        warning_label.grid(row=7, column=1)
        warning_text_label.grid_forget()

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

        name_label.config(
            text=f"Hello there, {name}. Press continue when ready.")
        name_label.grid(row=5, column=1)


# various labels and buttons laying out the welcome screen
warning_label = Label(tk_welcome, text="Warning, please enter name.", fg="red")

warning_text_label = Label(tk_welcome,
                           text="Please enter letters only", fg="red")

enter_button = Button(tk_welcome, text="Enter", fg="green", command=place_name)
enter_button.grid(row=6, column=1)

name_label = Label(tk_welcome, text="")

placeholder_label = Label(tk_welcome)
placeholder_label.grid(row=7, column=1)

skip_button = Button(tk_welcome, text="skip", command=newwindow)
skip_button.grid(row=8, column=1)

continue_button = Button(tk_welcome, text="Continue", command=newwindow)

# looping the entire program
tk_welcome.mainloop()
