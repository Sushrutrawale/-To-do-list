import tkinter as tk               
from tkinter import ttk            
from tkinter import messagebox     
import sqlite3 as sql            



conn = sql.connect("todo_list.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)")


def add_task():
    task = entry.get()
    if task:
       
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
       
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = listbox.get(selected_task)
        
        cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()
        
        listbox.delete(selected_task)


def delete_all_tasks():  
      
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        
        while(len(tasks) != 0):  
            
            tasks.pop()  
        
        cursor.execute('delete from tasks')  
        
        listbox.delete(0, 'end')  
        
def close():
    
    message_box = messagebox.askyesno('exit','Are you sure, you want to exit?') 
    if message_box == True:  
        
        window.destroy() 


window = tk.Tk()
window.title("To-Do List")
window.geometry("500x450+750+250")  
window.resizable(0, 0)  
window.configure(bg = "#008080") 



header_frame = tk.Frame(window, bg = "#008080")  
functions_frame = tk.Frame(window, bg = "#008080")  
listbox_frame = tk.Frame(window, bg = "#008080")  


header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")


listbox = tk.Listbox(  
    listbox_frame,  
    width = 26,  
    height = 14,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)  

listbox.place(x = 30, y = 40)  


cursor.execute("SELECT task FROM tasks")
tasks = cursor.fetchall()
for task in tasks:
    listbox.insert(tk.END, task[0])


header_label = ttk.Label(  
    header_frame,  
    text = "My To-Do List",  
    font = ("Roboto", "30"),  
    background = "#008080",  
    foreground = "#000000"  
)  

header_label.pack(padx = 20, pady = 20)  



task_label = ttk.Label(  
    functions_frame,  
    text = "Enter the Task:",  
    font = ("Consolas", "15", "bold"),  
    background = "#008080",  
    foreground = "#000000"  
)  

task_label.place(x = 30, y = 40)  


entry = ttk.Entry(  
    functions_frame,  
    font = ("Consolas", "12"),  
    width = 16,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
)  
  
entry.place(x = 30, y = 80)  


  

add_btn = ttk.Button(  
    functions_frame,  
    text = "Add Task",  
    width = 24,  
    command = add_task  
)  

remove_btn = ttk.Button(  
    functions_frame,  
    text = "Delete Task",  
    width = 24,  
    command = remove_task  
)  

del_all_btn = ttk.Button(  
    functions_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all_tasks  
) 

exit_btn = ttk.Button(  
    functions_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
) 

  
add_btn.place(x = 30, y = 120)  
remove_btn.place(x = 30, y = 160)
del_all_btn.place(x = 30, y = 200)
exit_btn.place(x = 30, y = 240)  

window.mainloop()


cursor.close()
conn.close()
