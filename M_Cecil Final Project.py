import tkinter
from tkinter import ttk
from tkinter import messagebox

def show_message():
    if button_dnf:
        messagebox.showinfo("DNF","Don't Stop, Put it down and come back to it!")
# define button
def show_message_tbr():
    if button_tbr:
        messagebox.showinfo("TBR", "Check out your local library or bookstore and get to reading.")
# define table entries
def enter_data():
    book_title = book_title_entry.get()
    auth_first = auth_first_name_entry.get()
    auth_last = auth_last_name_entry.get()
    media_form = media_format_combobox.get()
    date_completed = date_completed_entry.get()
    book_status = button_tbr or button_submit or button_dnf

# set validation requirements
    if book_title and auth_first and auth_last and media_form and date_completed:
        print("Book Title: ", book_title, "Author First Name: ",auth_first,
        "Author Last Name: ", auth_last, "Format: ", media_form, "Date Finished: ", date_completed,)
    else:  messagebox.showwarning("Warning", "Please Complete All Fields")
window = tkinter.Tk()
window.title("Book Tracker")
frame = tkinter.Frame(window)
frame.pack()
# Saving Book Title
tbr_frame = tkinter.LabelFrame(frame, text=" Book Tracker")
tbr_frame.grid(row=0, column=0)
book_title_label = tkinter.Label(tbr_frame, text="Book Title")
book_title_label.grid(row=2, column=1)
book_title_entry = tkinter.Entry(tbr_frame)
book_title_entry.grid(row=3, column=1)
# Saving Author Information
auth_first_name_label = tkinter.Label(tbr_frame, text="Authors First Name")
auth_first_name_label.grid(row=2, column=2)
auth_last_name_label = tkinter.Label(tbr_frame, text="Author Last Name")
auth_last_name_label.grid(row=2, column=3)
auth_first_name_entry = tkinter.Entry(tbr_frame)
auth_first_name_entry.grid(row=3,column=2)
auth_last_name_entry = tkinter.Entry(tbr_frame)
auth_last_name_entry.grid(row=3, column=3)
# saving format
media_format_label = tkinter.Label(tbr_frame, text="Format")
media_format_combobox = ttk.Combobox(tbr_frame, values=["Print","Kindle","Audiobook"])
media_format_label.grid(row=2, column=4)
media_format_combobox.grid(row=3, column=4)
# getting date completed
date_completed_label = tkinter.Label(tbr_frame, text="Date Completed: MM/DD/YY ")
date_completed_label.grid(row=2, column=5)
date_completed_entry = tkinter.Entry(tbr_frame)
date_completed_entry.grid(row=3,column=5)
# padding
for widget in tbr_frame.winfo_children():
    widget.grid_configure(padx=20, pady=10)

# submit
button_submit = tkinter.Button(frame, text="Finished", command=enter_data)
button_submit.grid(row=4, column=2, padx=10, pady=10)
button_dnf = tkinter.Button(frame, text="Did Not Finish", command=show_message)
button_dnf.grid(row=4, column=1,padx=10, pady=10)
button_tbr = tkinter.Button(frame, text= "To Be Read", command=show_message_tbr)
button_tbr.grid(row=4, column=3, padx=10, pady=10)
button_exit = tkinter.Button(frame, text = "Cancel", command = exit)
button_exit.grid(row=1, column=1, padx=10,pady=10)

def exit():
    window.destroy()

window.mainloop()


