import tkinter as tk
from tkinter import ttk
import time

f = open('umum.txt', 'a')
f.close()


def bagi_data():

	f = open('umum.txt')
	hitung = 0
	data2 = []
	lewat = []
	hampir = []
	indeks_lewat = []
	indeks_hampir = []

	while True:
		data = f.readline()
		if data == '':
			break
		else:
			hitung += 1
			data2.append(data)
			if hitung % 6 == 0:
				#_ = list(data2[3])
				hari = ''
				bulan = ''
				tahun = ''
				batas = []
				indeks = 0
				for i in data2[3]:
					if i == '-':

						batas.append(indeks)
					indeks += 1

				

				hari = data2[3][: batas[0]]
				
				hari = int(hari)
				bulan = data2[3][(batas[0]+1): batas[1]]
				
				bulan = int(bulan)
				tahun = data2[3][(batas[1]+1): ]
				
				tahun = int(tahun)
				
				if tahun == int(time.strftime('%y\n')):
					
					if bulan == int(time.strftime('%m\n')):
						
						if (hari - int(time.strftime('%d\n'))) < 0:
							
							lewat.append(data2)
							indeks_lewat.append(hitung-5)
						elif (hari - int(time.strftime('%d\n'))) < 3:
							
							hampir.append(data2)
							indeks_hampir.append(hitung-5)
					elif bulan < int(time.strftime('%m\n')):
						lewat.append(data2)
						indeks_lewat.append(hitung-5)
				elif tahun < int(time.strftime('%y\n')):
					lewat.append(data2)
					indeks_lewat.append()

				data2 = []
			

	f.close()
	list_hampir = dict(zip(indeks_hampir, hampir))
	list_lewat = dict(zip(indeks_lewat, lewat))
	return {'hampir':list_hampir, 'lewat':list_lewat}

def hapus_lewat():
	baris = 1
	indeks = []
	for i in list(bagi_data()['lewat'].keys()):
		for j in range(6):
			indeks.append(i+j)

	with open("umum.txt", "r") as f:
		lines = f.readlines()
	with open("umum.txt", "w") as f:
		for line in lines:
			if baris not in indeks:
				f.write(line)

			baris += 1


def tampil_data():
	list_tugas.delete(*list_tugas.get_children())
	f = open('umum.txt')
	hitung = 0
	data2 = []

	while True:
		data = f.readline()
		if data == '':
			break
		else:
			hitung += 1
			data2.append(data)
			if hitung == 6:
				list_tugas.insert('', 'end', values=data2)
				data2 = []
				hitung = 0



	f.close()



def tambah_data():

	a = entri_nama_tugas.get()
	if a == '':
		a = 'Tanpa Nama'

	a1 = entri_jenis_tugas.get()
	a2 = entri_awal.get()
	if a2 == '':
		a2 = time.strftime('%d-%m-%y')

	a3 = entri_deadline.get()
	if a3 == '':
		a3 = str(int(time.strftime('%d') + 7))

	a4 = entri_bentuk_tugas.get()
	a5 = entri_deskripsi_tugas.get('1.0', 'end')
	if a5 == '\n':
		a5 = '--\n'

	f = open('umum.txt', 'a')
	f.write(a+'\n'+
		a1+'\n'+
		a2+'\n'+
		a3+'\n'+
		a4+'\n'+
		a5)
	f.close()
	apdet()


def notif():
	baris = 1
	indeks = []
	_ = []
	_1 = []
	for i in list(bagi_data()['hampir'].keys()):
		indeks.append(i)

	with open("umum.txt", "r") as f:
		lines = f.readlines()
	for line in lines:
		#print(type(line), line)
		if baris in indeks:
			_.append(line)

		baris += 1

	label_notifikasi.delete(0,len(_))
	for i in _:
		label_notifikasi.insert('end', i+' akan berakhir dalam 3 hari atau kurang')



def tanggaldanwaktu():
	tanggal = time.strftime('%d-%m-%y')
	waktu = time.strftime('%H:%M')
	tanggal_waktu.config(text=tanggal+'\n\n'+waktu)
	tanggal_waktu.after(5000, tanggaldanwaktu)



root = tk.Tk()
root['bg'] = '#15beed'
root.title('Manajemen Tugas')
root.geometry('1200x600')
root.resizable(False, False)

tk.Label(root, bg='#15beed', text='LIST KEGIATAN', font=('bold', 24)).place(x=725, y=10)
frame_deskripsi = tk.Frame(root, bg='white', relief='groove', bd=5)
frame_deskripsi.place(x=430, y=50, width=770, height=450)

tk.Label(root, bg='#15beed', text='MASUKKAN DATA', font=('bold', 24)).place(x=60, y=10)
frame_aksi = tk.Frame(root, bg='white', bd=2)
frame_aksi.place(x=20, y=50, width=350, height=320)

scroll_y = tk.Scrollbar(frame_deskripsi, orient='vertical')
scroll_x = tk.Scrollbar(frame_deskripsi, orient='horizontal')
list_tugas = ttk.Treeview(frame_deskripsi, columns=('nama_tugas', 'jenis_tugas', 'tanggal_masuk', 'deadline', 'bentuk_tugas', 'deskripsi'),
							yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_y.config(command=list_tugas.yview)
scroll_x.config(command=list_tugas.xview)
list_tugas.heading('nama_tugas', text='Nama Tugas', anchor='w')
list_tugas.heading('jenis_tugas', text='Jenis Tugas', anchor='w')
list_tugas.heading('tanggal_masuk', text='Tanggal Masuk', anchor='w')
list_tugas.heading('deadline', text='Deadline', anchor='w')
list_tugas.heading('bentuk_tugas', text='Bentuk Tugas', anchor='w')
list_tugas.heading('deskripsi', text='Deskripsi', anchor='w') 
list_tugas.column('nama_tugas', width=100)
list_tugas.column('jenis_tugas', width=100)
list_tugas.column('tanggal_masuk', width=100)
list_tugas.column('deadline', width=100)
list_tugas.column('bentuk_tugas', width=100)
list_tugas.column('deskripsi', width=500)
list_tugas['show'] = 'headings'
scroll_y.pack(side='right', fill='y') 
scroll_x.pack(side='bottom', fill='x')
list_tugas.pack(fill='both', expand=1)

tombol_tambah = tk.Button(root, text='Tambah', font=('bold'), width=7, bd=5, command=tambah_data)
tombol_tambah.place(x=290, y=370)



nama_tugas = tk.Label(frame_aksi, bg='white', text='Nama Tugas\t:', font=('bold'))
nama_tugas.grid(row=0, column=0)

var_nama_tugas = tk.StringVar()
entri_nama_tugas = tk.Entry(frame_aksi, textvariable=var_nama_tugas, font=(14), bd=4)
entri_nama_tugas.grid(row=0, column=1, pady=5)

jenis_tugas = tk.Label(frame_aksi, text='Jenis Tugas \t: ', bg='white', font=('bold'))
jenis_tugas.grid(row=1, column=0, pady=5)

entri_jenis_tugas = ttk.Combobox(frame_aksi, values=('Tugas Kuliah', 'Acara', 'Kegiatan Lainnya'), font=(14), width=18, state='readonly')
entri_jenis_tugas.current(0)
entri_jenis_tugas.grid(row=1, column=1, pady=5)

awal = tk.Label(frame_aksi, text='Tanggal Masuk\t:', bg='white', font=('bold'), bd=4)
awal.grid(row=2, column=0, pady=5)

var_awal = tk.StringVar()
entri_awal = tk.Entry(frame_aksi, textvariable=var_awal, font=(14), bd=4)
entri_awal.insert(0, time.strftime('%d-%m-%y'))
entri_awal.grid(row=2, column=1, pady=5)

label_deadline = tk.Label(frame_aksi, text='Deadline\t\t:', bg='white', font=('bold'))
label_deadline.grid(row=3, column=0, pady=5)

var_deadline = tk.StringVar()
entri_deadline = tk.Entry(frame_aksi, textvariable=var_deadline, font=(14), bd=4)
entri_deadline.insert(0, str(int(time.strftime('%d'))+7)+time.strftime('-%m-%y'))
entri_deadline.grid(row=3, column=1, pady=5)

bentuk_tugas = tk.Label(frame_aksi, text='Bentuk Tugas\t:', bg='white', font=('bold'))
bentuk_tugas.grid(row=4, column=0, pady=5)

entri_bentuk_tugas = ttk.Combobox(frame_aksi, values=('Mandiri', 'Kelompok'), font=(14), width=18, state='readonly')
entri_bentuk_tugas.current(0)
entri_bentuk_tugas.grid(row=4, column=1, pady=5)

deskripsi_tugas = tk.Label(frame_aksi, text='Deskripsi Tugas\t:', bg='white', font=('bold'))
deskripsi_tugas.grid(row=5, column=0, pady=5)

entri_deskripsi_tugas = tk.Text(frame_aksi, width=21, height=7, relief='groove', bd=5, font=('Times New Roman', 11))
entri_deskripsi_tugas.grid(row=5, column=1, pady=5)

tanggal_waktu = tk.Label(root, bg='#b3ffff', fg='#2a8000', height=4, width=10, font=('Times New Roman',12, 'bold'))
tanggal_waktu.place(x=0, y=517)


frame_notifikasi = tk.Frame(root, bg='gray', bd=4)
frame_notifikasi.place(width=770, height=90, x=430, y=500)

y_scroll = tk.Scrollbar(frame_notifikasi, orient='vertical')
label_notifikasi = tk.Listbox(frame_notifikasi, fg='#e60000', font=('bold'), yscrollcommand=y_scroll.set)
y_scroll.config(command=label_notifikasi.yview)
y_scroll.pack(side='right', fill='y')
label_notifikasi.pack(fill='both', expand=1)


tk.Label(root, bg='#15beed', fg='#3333ff', font=('Times New Roman', 16, 'bold'),
 		 text='Copyright wazadio@2020\nWhatsApp : 081261853337').place(x=100, y=530)
tk.Label(root, bg='white', width=45, text='ISILAH SESUAI DENGAN FORMAT UNTUK MENGHINDARI BUG', font=('calibri', 8)).place(x=12, y=371)

def apdet():
	bagi_data()
	hapus_lewat()
	tampil_data()
	notif()

apdet()
tanggaldanwaktu()
root.mainloop()


