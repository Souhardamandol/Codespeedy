from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(background="#431461")
root.title('To-Do List')
root.geometry("650x450")

my_font = Font(family="Arial", size=21, weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=9)

my_list = Listbox(my_frame, font=my_font, width=38, height=6, bg="cyan", bd=0, fg="#808000", highlightthickness=0, selectbackground="#ff0000", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Arial", 21), width=27, bg='cyan')
my_entry.pack(pady=22)

button_frame = Frame(root, bg='pink')
button_frame.pack(pady=22)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)



def delete_list():
    my_list.delete(0, END)

delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="yellow", font=("arial", 12, "bold"))
add_button = Button(button_frame, text="Add Item", command=add_item, bg="teal", font=("arial", 12, "bold"))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)


root.mainloop()