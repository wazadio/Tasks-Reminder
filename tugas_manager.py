import tkinter as tk

def Personal():
	root.destroy()
	import tugas_manager_1
	
def General():
	root.destroy()
	import tugas_manager_2
	
root = tk.Tk()
root.geometry('80x100')

tk.Button(root, text='Pribadi', command=Personal).pack(side='left')
tk.Button(root, text='Umum', command=General).pack(side='right')

root.mainloop()

