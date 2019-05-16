import Tkinter
import ast
import os

# creating root window
root = Tkinter.Tk()


# Configuring root window
root.configure(bg="white")
root.title("To-Do App")
root.geometry("730x632")


tasks = []
done_tasks = []
del_all_flag = 0
del_tasks = []
logged_in_user = ''


# Functions for commands
def update_task():
	list_task.delete(0,"end")
	for task in tasks:
		list_task.insert("end", task)
	if logged_in_user != '':
		path_user = 'users/'+logged_in_user+'/'+logged_in_user+'unfinished.txt'
		with open(path_user, 'w') as f:
			print>>f, tasks

def update_done_task():
	list_done_task.delete(0,"end")
	for task in done_tasks:
		list_done_task.insert("end", task)
	if logged_in_user != '':
		path_user = 'users/'+logged_in_user+'/'+logged_in_user+'finished.txt'
		with open(path_user, 'w') as f:
			print>>f, done_tasks


def add_task():
	global del_all_flag
	global del_tasks
	task = txt_input.get()
	task=task.strip()
	if task != "":
		if task in tasks:
			error_space['text'] = "Existing Task."
		else:
			tasks.append(task)
			update_task()
			error_space["text"] = ""
			del_all_flag=0
			del_tasks = []
	else:
		error_space["text"] = "Insert a valid task."
	txt_input.delete(0,"end")



def del_one_task():
	global del_tasks
	task = list_task.get("active")
	if task in tasks:
		tasks.remove(task)
		del_tasks.append(task)
		update_task()


def del_all_task():
	global tasks
	global del_all_flag
	global del_tasks
	del_tasks = tasks
	tasks = []
	del_all_flag=1
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
	done_tasks = []
	update_done_task()

def undo_task():
	task = list_done_task.get("active")
	if task in done_tasks:
		done_tasks.remove(task)
		tasks.append(task)
	update_done_task()
	update_task()

def del_undo_task():
	global tasks
	global del_tasks
	global del_all_flag
	if(del_all_flag == 0):
		del_tasks.reverse()
		if(len(del_tasks)!=0):
			var = del_tasks[0]
			if var in del_tasks:
				del_tasks.remove(var)
			tasks.append(var)
	else:
		if(len(del_tasks)!=0):
			tasks = del_tasks
			del_tasks =[]
			del_all_flag=0

	del_tasks.reverse()
	update_task()


def exist_login():
	users = []
	global logged_in_user
	global tasks
	global done_tasks
	global del_tasks
	global del_all_flag
	u_id = exist_id.get()
	u_pass = exist_pass.get()
	u_id = u_id.strip()
	u_pass =u_pass.strip()
	if(u_pass!='' and u_id!=''):
		with open('auth/auth.txt', 'r') as f:
			users = ast.literal_eval(f.read())
		f.close()
		is_existing = [user for user in users if user[0]==u_id and user[1]==u_pass]
		if(is_existing!=[]):
			logged_in_user = u_id
			login_status["text"]="Login Successful."
			lbl_warning["text"] = "Logged In"
			del_all_flag=0
			del_tasks=[]
			path_user_unfinished = 'users/'+u_id+'/'+u_id+'unfinished.txt'
			path_user_finished = 'users/'+u_id+'/'+u_id+'finished.txt'
			with open(path_user_unfinished,'r') as f:
				tasks = ast.literal_eval(f.read())
			f.close()
			with open(path_user_finished,'r') as f:
				done_tasks = ast.literal_eval(f.read())
			f.close()
			update_task()
			update_done_task()
		else:
			login_status["text"]="Invalid Credentials."
	else:
		login_status["text"] = "Invalid entry."
	exist_id.delete(0,"end")
	exist_pass.delete(0,"end")

def signup():
	user_tuple = (new_id.get(), new_pass.get())
	users=[]
	u_id = new_id.get()
	u_id = u_id.strip()
	u_pass = new_pass.get()
	u_pass=u_pass.strip()
	task_initialiser = []
	if(u_pass!='' and u_id!=''):
		with open('auth/auth.txt', 'r') as f:
			users = ast.literal_eval(f.read())
		f.close()
		is_existing = [user for user in users if user[0]==new_id.get()]
		if(is_existing!=[]):
			signup_status["text"] = "User exists."
		else:
			users.append(user_tuple)
			with open('auth/auth.txt', 'w') as f:
				print>>f, users
			f.close()
			path_dir = 'users/'+u_id
			if not os.path.exists(path_dir):
				os.makedirs(path_dir)
			path_user_finished = 'users/'+u_id+'/'+u_id+'finished.txt'
			path_user_unfinished = 'users/'+u_id+'/'+u_id+'unfinished.txt'
			if not os.path.exists(path_user_unfinished):
				open(path_user_unfinished, 'w').close()
				open(path_user_finished, 'w').close()
				with open(path_user_unfinished, 'w') as f:
					print>>f, task_initialiser
				f.close()
				with open(path_user_finished, 'w') as f:
					print>>f, task_initialiser
				f.close()
			signup_status["text"] = "Login now."
	else:
		signup_status["text"] = "Invalid entry."
	new_id.delete(0,"end")
	new_pass.delete(0,"end")






lbl_Existing = Tkinter.Label(root, text="Existing User:", bg="white")
lbl_Existing.grid(row=0 , column=0)

login_status = Tkinter.Label(root, text="", bg="white", fg="blue")
login_status.grid(row=0 , column=1)

lbl_username = Tkinter.Label(root, text="Email id :", bg="white", fg="blue")
lbl_username.grid(row=1 , column=0)

exist_id = Tkinter.Entry(root, width=13)
exist_id.grid(row=1, column=1)

lbl_pass = Tkinter.Label(root, text="Password :", bg="white", fg="blue")
lbl_pass.grid(row=2, column=0)

exist_pass = Tkinter.Entry(root, width=13)
exist_pass.grid(row=2, column=1)

btn_exist_login = Tkinter.Button(root, text="Login", fg="blue", height=1, width=11, command=exist_login)
btn_exist_login.grid(row=3, column=1)

lbl_gap_exst_new = Tkinter.Label(root, text="", bg="white")
lbl_gap_exst_new.grid(row=4 , column=0)



lbl_new = Tkinter.Label(root, text="New User:", bg="white")
lbl_new.grid(row=5 , column=0)

signup_status = Tkinter.Label(root, text="", bg="white", fg="blue")
signup_status.grid(row=5 , column=1)

lbl_new_username = Tkinter.Label(root, text="Email id :", bg="white", fg="blue")
lbl_new_username.grid(row=6 , column=0)

new_id = Tkinter.Entry(root, width=13)
new_id.grid(row=6, column=1)

lbl_new_pass = Tkinter.Label(root, text="Password :", bg="white", fg="blue")
lbl_new_pass.grid(row=7 , column=0)

new_pass = Tkinter.Entry(root, width=13)
new_pass.grid(row=7, column=1)

btn_new_login = Tkinter.Button(root, text="Login", fg="blue", height=1, width=11, command=signup)
btn_new_login.grid(row=8, column=1)

lbl_gap_new_body = Tkinter.Label(root, text="", bg="white")
lbl_gap_new_body.grid(row=9 , column=0)


gap_auth_app = Tkinter.Label(root, text="", bg="white", width=3)
gap_auth_app.grid(row=0 , column=3)




lbl_title = Tkinter.Label(root, text="To-Do:", bg="white")
lbl_title.grid(row=0 , column=4)

lbl_warning = Tkinter.Label(root, text="Login to save data.", bg="white")
lbl_warning.grid(row=1 , column=4)

error_space = Tkinter.Label(root, text="", bg="white", fg="red")
error_space.grid(row=1 , column=5)

lbl_todo = Tkinter.Label(root, text="Enter Task :", bg="white", fg="blue")
lbl_todo.grid(row=2 , column=4)

txt_input = Tkinter.Entry(root, width=35)
txt_input.grid(row=2 , column=5)

btn_add_task = Tkinter.Button(root, text="Add", bg="white", fg="green", command=add_task, height=1, width=15)
btn_add_task.grid(row=3 , column=4)

btn_del_one_task = Tkinter.Button(root, text="Delete Selected Task", bg="white", fg="red", command=del_one_task,height=1, width=15)
btn_del_one_task.grid(row=4 , column=4)

btn_del_all_task = Tkinter.Button(root, text="Delete All", bg="white", fg="red", command=del_all_task,height=1,  width=15)
btn_del_all_task.grid(row=5 , column=4)

btn_del_undo_task = Tkinter.Button(root, text="Undo", bg="white", fg="blue", command=del_undo_task,height=1,  width=15)
btn_del_undo_task.grid(row=6 , column=4)

btn_sort_asc_task = Tkinter.Button(root, text="Sort (Asc.)", bg="white", fg="blue", command=sort_asc_task, height=1,  width=15)
btn_sort_asc_task.grid(row=7 , column=4)

btn_sort_desc_task = Tkinter.Button(root, text="Sort (Desc.)", bg="white", fg="blue", command=sort_desc_task, height=1,  width=15)
btn_sort_desc_task.grid(row=8 , column=4)

btn_done_one_task = Tkinter.Button(root, text="Done Selected Task", bg="white", fg="green", command=done_one_task, height=1,  width=15)
btn_done_one_task.grid(row=9 , column=4)

btn_done_all_task = Tkinter.Button(root, text="Done All", bg="white", fg="green", command=done_all_task, height=1,  width=15)
btn_done_all_task.grid(row=10 , column=4)

list_task = Tkinter.Listbox(root, height=37, width=35)
list_task.grid(row=3 , column=5,  rowspan=50)





gap = Tkinter.Label(root, text="", bg="white", fg="red")
gap.grid(row=11 , column=4)

lbl_done = Tkinter.Label(root, text="Done:", bg="white")
lbl_done.grid(row=12 , column=4)

btn_clear_task = Tkinter.Button(root, text="Clear All", bg="white", fg="blue", command=clear_task, height=1,  width=15)
btn_clear_task.grid(row=13 , column=4)

btn_undo_task = Tkinter.Button(root, text="Undo Selected Task", bg="white", fg="blue", command=undo_task, height=1,  width=15)
btn_undo_task.grid(row=14 , column=4)


list_done_task = Tkinter.Listbox(root, height=15)
list_done_task.grid(row=15 , column=4,  rowspan=55)

lbl_credit = Tkinter.Label(root, text="Developed by Surya", fg="grey")
lbl_credit.grid(row=202, column=0)
lbl_credit = Tkinter.Label(root, text="Copyright@2018", fg="grey")
lbl_credit.grid(row=202, column=1)













#start main event loop
root.mainloop()