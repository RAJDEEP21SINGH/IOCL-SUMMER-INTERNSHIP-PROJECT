from tkinter import ttk
from customtkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database
#Functions
def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records')
    if result:
        database.deleteall_records()
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted')
def showall():
    treeview_data()
    search_Entry.delete(0,END)
    searchbox.set("Seach By")
def search_employee():
    if search_Entry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchbox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    
    else:
        search_data= database.search(searchbox.get(),search_Entry.get())
        tree.delete(*tree.get_children())
#deletes the record first and then adds the updated list all at ones 
        for employee in search_data:
         tree.insert("",END,values=employee)
       
def delete_employee():
    selected_item=tree.selection()
    result=messagebox.askyesno('Confirm','Do you really want to delete this record')
    if result:
       if not selected_item:
        messagebox.showerror("Error",'Select data to delete')
       else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted')

def update_employee():
    selected_items=tree.selection()
    result=messagebox.askyesno('Confirm','Do you really want to update the existing employee')
    if result:
        if not selected_items:
         messagebox.showerror('Error','Select Data To Update')
    
        else:
         database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salary_Entry.get())
         treeview_data()
         clear()
         messagebox.showinfo('Success','Data is updated')

def selection(event):#will add all details in the fields if selected
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salary_Entry.insert(0,row[5])
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    rolebox.set('web Developer')
    genderbox.set('Male')
    salary_Entry.delete(0,END)
def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
#deletes the record first and then adds the updated list all at ones 
    for employee in employees:
        tree.insert("",END,values=employee)

def add_employee():
    phone_text = phoneEntry.get()  # Get the text from the entry widget
    phone_length = len(phone_text)
    
    salary_text = salary_Entry.get()  
    salary_length = len(salary_text)

    result=messagebox.askyesno('Confirm','Do you really want to add the employee')
    if result:
        if idEntry.get()=="" or phoneEntry.get()=='' or nameEntry.get()=='' or salary_Entry.get()=='':
         messagebox.showerror('Error','All fields are required')
        elif phone_length<10 or phone_length>10  or salary_length>8:
         messagebox.showerror('Error','Invalid Entry')
        elif database.id_exists(idEntry.get()):
         messagebox.showerror('Error','Id already exists')
        elif not idEntry.get().startswith('EMP'):
         messagebox.showerror('Error',"Invalid ID format. Use 'EMP' followed by a number (e.g., 'EMP1').")
        else:
         database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salary_Entry.get()) 
         treeview_data()
         clear()
         messagebox.showinfo("Success","Data is added") 

#GUI Part

window=CTk()
window.geometry('1100x700+200+80')
window.resizable(0,0)#or can use (false,false)
window.title("Employee Management System")
window.configure(fg_color='#161C30')
image=Image.open(r"D:\1689563693471.jpeg")
resized_image = image.resize((1375,280))
photo=ImageTk.PhotoImage(resized_image)

logo_label=CTkLabel(window,image=photo,text='')
logo_label.grid(row=0,column=0,columnspan=2)

leftframe=CTkFrame(window,fg_color='#161C30',border_width=2,border_color='white')
leftframe.grid(row=1,column=0,pady=20,padx=2)

idlabel=CTkLabel(leftframe,text="ID",font=('arial',18,'bold'),text_color='white')
idlabel.grid(row=0,column=0,padx=20,pady=20,sticky="w")

idEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1,padx=20)

namelabel=CTkLabel(leftframe,text="Name",font=('arial',18,'bold'),text_color='white')
namelabel.grid(row=1,column=0,padx=20,pady=15,sticky="w")

nameEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phonelabel=CTkLabel(leftframe,text="Phone",font=('arial',18,'bold'),text_color='white')
phonelabel.grid(row=2,column=0,padx=20,pady=15,sticky="w")

phoneEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

rolelabel=CTkLabel(leftframe,text="Role",font=('arial',18,'bold'),text_color='white')
rolelabel.grid(row=3,column=0,padx=20,pady=15,sticky="w")

role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','Data Analyst','Data Scientist','Business Analyst','IT Consultant','UX/UI Designer']
rolebox=CTkComboBox(leftframe,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)
rolebox.set(role_options[0])

genderlabel=CTkLabel(leftframe,text="Gender",font=('arial',18,'bold'),text_color='white')
genderlabel.grid(row=4,column=0,padx=20,pady=15,sticky="w")

gender_options=["Male","Female"]
genderbox=CTkComboBox(leftframe,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)
genderbox.set('Male')

salary_label=CTkLabel(leftframe,text="Salary",font=('arial',18,'bold'),text_color='white')
salary_label.grid(row=5,column=0,padx=20,pady=15,sticky="w")

salary_Entry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
salary_Entry.grid(row=5,column=1)

rightframe=CTkFrame(window)
rightframe.grid(row=1,column=1,padx=1,pady=15)


search_options=["ID","Name","Phone","Role","Gender","Salary"]

searchbox=CTkComboBox(rightframe,values=search_options,width=180,font=('arial',15,'bold'),state='readonly')
searchbox.grid(row=0,column=0,)
searchbox.set('Search By')

search_Entry=CTkEntry(rightframe,font=('arial',15,'bold'),width=180)
search_Entry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text="Search",width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightframe,text="Show All",width=100,command=showall)
showallButton.grid(row=0,column=3,pady=8)

tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=['ID','Name','Phone','Role','Gender','Salary']
#creates columns without the title
tree.heading('ID',text=' ID ')
tree.heading('Name',text=' Name ')
tree.heading('Phone',text=' Phone ')
tree.heading('Role',text=' Role ')
tree.heading('Gender',text=' Gender ')
tree.heading('Salary',text=' Salary ')
tree.config(show='headings')#removes default column
tree.column('ID',width=100)
tree.column('Name',width=180)
tree.column('Phone',width=160)
tree.column('Role',width=180)
tree.column('Gender',width=110)
tree.column('Salary',width=140)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'),pady=10)
style.configure('Treeview',font=('arial',15,'bold'),rowheight=30,background='#161C30',foreground='white',pady=10)
scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)
buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=5)


newButton=CTkButton(buttonFrame,text="New Employee",font=('arial',15,'bold'),width=160,corner_radius=15,border_spacing=10,command=lambda: clear(True),border_width=2,border_color='white')
newButton.grid(row=0,column=0,pady=5,padx=20)

addButton=CTkButton(buttonFrame,text="Add Employee",font=('arial',15,'bold'),width=160,corner_radius=15,border_spacing=10,command=add_employee,border_width=2,border_color='white')
addButton.grid(row=0,column=1,padx=20,pady=5)

updateButton=CTkButton(buttonFrame,text="Update Employee",font=('arial',15,'bold'),width=160,corner_radius=15,border_spacing=10,command=update_employee,border_width=2,border_color='white')
updateButton.grid(row=0,column=2,padx=20,pady=5,)

deleteButton=CTkButton(buttonFrame,text="Delete Employee",font=('arial',15,'bold'),width=160,corner_radius=15,border_spacing=10,command=delete_employee,border_width=2,border_color='white')
deleteButton.grid(row=0,column=3,padx=20,pady=5,)

deleteallButton=CTkButton(buttonFrame,text="Delete All",font=('arial',15,'bold'),width=160,corner_radius=15,border_spacing=10,command=delete_all,border_width=2,border_color='white')
deleteallButton.grid(row=0,column=4,padx=20,pady=5,)

treeview_data()
window.bind('<ButtonRelease>',selection)
#whenever the button will be released selection button will be called 
window.mainloop()
