from tkinter import *
import backend


def view_command():
    list1.delete(0,END) # Deleting everything from start to end.
    for count, row in enumerate(backend.view_all()):
        list1.insert(END,(count+1,row)) # The first argument sets the position where its going to get settled the incoming string inside the view box, e.g. 0,1,2... END.
        # print(count+1)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text_input.get(),author_text_input.get(),year_text_input.get(),isbn_text_input.get()): # Below, the arguments used in entries are defined as string objects using the method StringVar() and not as simple strings. So to get a simple string and use it in the backend.search() function as needed, there must be appended in the arguments the get() method which produces a simple string.
        list1.insert(END,row)

def add_command():
    backend.insert(title_text_input.get(),author_text_input.get(),year_text_input.get(),isbn_text_input.get()) # This inserts the inputed arguments inside the database table
    list1.delete(0,END)
    list1.insert(END,(title_text_input.get(),author_text_input.get(),year_text_input.get(),isbn_text_input.get())) # while this inserts them in to the view box of the app. # Also note that the arguments are inputed inside brackets as a single value, as a result in the output list we take one line of string and not many as the number of the imported arguments.

def delete_command():
    index_of_listbox=list1.curselection()[0] # Using this to get the number of the selected line of the listbox.
    index_of_database=list1.get(index_of_listbox)[1][0] # Using this to get the the number of line which is registered in the database. (content enumeration: database table different from listbox)
    backend.delete(index_of_database)
    list1.delete(0,END)
    for count, row in enumerate(backend.view_all()): # Updating the listbox after deleting
        list1.insert(END,(count+1,row))
    # print(index_of_database)

def update_command():
    # list1.delete(0,END)
    index_of_listbox=list1.curselection()[0] # Using this to get the number of the selected line of the listbox.
    index_of_database=list1.get(index_of_listbox)[1][0] # Using this to get the the number of line which is registered in the database. (for content enumeration: database table different from listbox)
    backend.update(index_of_database,title_text_input.get(),author_text_input.get(),year_text_input.get(),isbn_text_input.get())
    list1.delete(0,END)
    for count, row in enumerate(backend.view_all()): # Updating the listbox after updating the database.
        list1.insert(END,(count+1,row))
    # print(index_of_database)


def fill_entries(evt): # Fill entries with info form the selected row. Connected with list1.bind() method in Listbox sector below.
# Note here that Tkinter passes an event object to fill_entries(). In this exapmle the event is the selection of a row in the listbox.
    try:
        index_of_listbox=list1.curselection()[0]
        index_of_database=list1.get(index_of_listbox)
        e1.delete(0,END)
        e1.insert(END, index_of_database[1][1])         # Here the use of try and except block, excepts the error produced when clicking inside an empty listbox.
        e2.delete(0,END)                                # The <<index_of_listbox=list1.curselection()[0]>> gives a list from which we took the first object. So when the listbox is empty we will take an empty list with no objects which produces an error.
        e2.insert(END, index_of_database[1][2])
        e3.delete(0,END)
        e3.insert(END, index_of_database[1][3])
        e4.delete(0,END)
        e4.insert(END, index_of_database[1][4])
        # print(index_of_database[1][2])
    except IndexError:
        pass

def clean_entries_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)



###########################################
# Creation of GUI and its elements elements
###########################################

# All the element alligning happens inside a grid. 
# Each element declares its own position inside the grid.

# Creating a window object
window=Tk()

# window.create_window(height=100, width=100)

# Window title
window.wm_title('Book Library')

# Labels
l1=Label(window,text="Title")
l1.grid(row=1,column=0)

l2=Label(window,text="Author")
l2.grid(row=2,column=0)

l3=Label(window,text="Year")
l3.grid(row=3,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=4,column=0)

#Entries
title_text_input=StringVar()
e1=Entry(window,textvariable=title_text_input)
e1.grid(row=1,column=1)

author_text_input=StringVar()
e2=Entry(window,textvariable=author_text_input)
e2.grid(row=2,column=1)

year_text_input=StringVar()
e3=Entry(window,textvariable=year_text_input)
e3.grid(row=3,column=1)

isbn_text_input=StringVar()
e4=Entry(window,textvariable=isbn_text_input)
e4.grid(row=4,column=1)

#ListBox
list1=Listbox(window,height=10,width=90,highlightcolor='green',selectbackground='green')
list1.grid(row=1,column=2,rowspan=4,columnspan=6)
list1.bind('<<ListboxSelect>>', fill_entries) # The fill_entries function is going to be executed when a row of the listbox is selected. Check for more http://www.tcl.tk/man/tcl8.5/TkCmd/event.htm#M41]

#Scrollbars
# sb1=Scrollbar(window)
# sb1.grid(row=2,column=2,rowspan=6)
#
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

#Buttons
b1=Button(window,text="View All", width=14, command=view_command) # Using the function without brackets to execute it when the button is pushed without waiting this line of the script gets read.
b1.grid(row=0,column=2)
b2=Button(window,text="Search Entry", width=14, command=search_command)
b2.grid(row=0,column=3)
b3=Button(window,text="Add Entry", width=14, command=add_command)
b3.grid(row=0,column=4)
b4=Button(window,text="Update", width=14, command=update_command)
b4.grid(row=0,column=5)
b5=Button(window,text="Delete", width=14, command=delete_command)
b5.grid(row=0,column=6)
b6=Button(window,text="Close", width=4, command=window.destroy)
b6.grid(row=0,column=0)
b7=Button(window,text="Clean", width=15, command=clean_entries_command)
b7.grid(row=0,column=1)


# Show created window with its contained elements
window.mainloop()
