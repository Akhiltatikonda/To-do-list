import tkinter as tk

def create_task():
    task=entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0,tk.END)

def update_task():
    selected_task_index=listbox.curselection()[0]
    new_task=entry.get()
    if new_task:
        tasks[selected_task_index]=new_task
        update_listbox()
        entry.delete(0,tk.END)

def delete_task():
    try:
        selected_task_index=listbox.curselection()[0]
        del tasks[selected_task_index]
        update_listbox()
        entry.delete(0,tk.END)
    except IndexError:
        pass

def update_listbox():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)

window = tk.Tk()
window.title("TO-DO-LIST App")
tasks=[   ]
listbox=tk.Listbox(window,width=50,height=30)
entry=tk.Entry(window,width=50)
create_button=tk.Button(window, text="Add Your Task",command=create_task)
update_button=tk.Button(window,text="UPDATE TASK",command=update_task)
delete_button=tk.Button(window,text="Delete Task",command=delete_task)

listbox.pack(pady=10)
entry.pack()
create_button.pack()
update_button.pack()
delete_button.pack()


window.mainloop()

