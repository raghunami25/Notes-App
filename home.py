import Tkinter

#creating root window
root = Tkinter.Tk()


#Configuring root window
root.configure(bg="white")
root.title("To-Do App")
root.geometry("455x550")


#Functions for commands

tasks = []
done_tasks = []

def update_task():
	list_task.delete(0,"end")
	for task in tasks:
		list_task.insert("end", task)

def update_done_task():
	list_done_task.delete(0,"end")
	for task in done_tasks:
		list_done_task.insert("end", task)

def add_task():
	task = txt_input.get()
	task=task.strip()
	if task != "":
		if task in tasks:
			error_space['text'] = "Existing Task."
		else:
			tasks.append(task)
			update_task()
			error_space["text"] = ""
	else:
		error_space["text"] = "Insert a valid task."
	txt_input.delete(0,"end")


def del_one_task():
	task = list_task.get("active")
	if task in tasks:
		tasks.remove(task)
		update_task()


def del_all_task():
	global tasks
	tasks = []
	update_task()

def sort_asc_task():
	tasks.sort()
	update_task()


def sort_desc_task():
	tasks.sort()
	tasks.reverse()
	update_task()

def done_one_task():
	task = list_task.get("active")
	if task in tasks:
		tasks.remove(task)
		done_tasks.append(task)
	update_task()
	update_done_task()

def done_all_task():
	for task in tasks:
		done_tasks.append(task)
	update_task()
	del_all_task()
	update_done_task()

def clear_task():
	global done_tasks
	done_tasks =[]
	update_done_task()

def undo_task():
	task = list_done_task.get("active")
	if task in done_tasks:
		done_tasks.remove(task)
		tasks.append(task)
	update_done_task()
	update_task()









lbl_title = Tkinter.Label(root, text="To-Do:", bg="white")
lbl_title.grid(row=0 , column=0)

txt_input = Tkinter.Entry(root, width=35)
txt_input.grid(row=1 , column=1)

error_space = Tkinter.Label(root, text="", bg="white", fg="red")
error_space.grid(row=0 , column=1)

btn_add_task = Tkinter.Button(root, text="Add", bg="white", fg="green", command=add_task, height=1, width=15)
btn_add_task.grid(row=1 , column=0)

btn_del_one_task = Tkinter.Button(root, text="Delete Selected Task", bg="white", fg="red", command=del_one_task,height=1, width=15)
btn_del_one_task.grid(row=2 , column=0)

btn_del_all_task = Tkinter.Button(root, text="Delete All", bg="white", fg="red", command=del_all_task,height=1,  width=15)
btn_del_all_task.grid(row=3 , column=0)

btn_sort_asc_task = Tkinter.Button(root, text="Sort (Asc.)", bg="white", fg="blue", command=sort_asc_task, height=1,  width=15)
btn_sort_asc_task.grid(row=4 , column=0)

btn_sort_desc_task = Tkinter.Button(root, text="Sort (Desc.)", bg="white", fg="blue", command=sort_desc_task, height=1,  width=15)
btn_sort_desc_task.grid(row=5 , column=0)

btn_done_one_task = Tkinter.Button(root, text="Done Selected Task", bg="white", fg="green", command=done_one_task, height=1,  width=15)
btn_done_one_task.grid(row=6 , column=0)

btn_done_all_task = Tkinter.Button(root, text="Done All", bg="white", fg="green", command=done_all_task, height=1,  width=15)
btn_done_all_task.grid(row=7 , column=0)

list_task = Tkinter.Listbox(root, height=32, width=35)
list_task.grid(row=2 , column=1,  rowspan=100)





gap = Tkinter.Label(root, text="", bg="white", fg="red")
gap.grid(row=16 , column=0)

lbl_done = Tkinter.Label(root, text="Done:", bg="white")
lbl_done.grid(row=17 , column=0)

btn_clear_task = Tkinter.Button(root, text="Clear All", bg="white", fg="blue", command=clear_task, height=1,  width=15)
btn_clear_task.grid(row=18 , column=0)

btn_undo_task = Tkinter.Button(root, text="Undo Selected Task", bg="white", fg="blue", command=undo_task, height=1,  width=15)
btn_undo_task.grid(row=19 , column=0)


list_done_task = Tkinter.Listbox(root, height=15)
list_done_task.grid(row=20 , column=0,  rowspan=55)

lbl_credit = Tkinter.Label(root, text="Developed by Surya", fg="grey")
lbl_credit.grid(row=202, column=0)
lbl_credit = Tkinter.Label(root, text="Copyright@2018", fg="grey")
lbl_credit.grid(row=202, column=1)













#start main event loop
root.mainloop()