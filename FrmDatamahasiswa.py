import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox, ttk, END
from tkcalendar import DateEntry
from Datamahasiswa import Datamahasiswa

class FormDatamahasiswa:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("470x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onkeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        #atur latar belakang 
        background_label = Label(mainFrame, bg="Gold")
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        Label(mainFrame, text='NIM:', bg="Gold").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>", self.onCari) 
        
        Label(mainFrame, text='NAMA:', bg="Gold").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='KELAS:', bg="Gold").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKELAS = Entry(mainFrame) 
        self.txtKELAS.grid(row=2, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='MATKUL:', bg="Gold").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtMATKUL = Entry(mainFrame) 
        self.txtMATKUL.grid(row=3, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='TANGGAL LAHIR:', bg="Gold").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtTANGGALLAHIR = DateEntry(mainFrame, width=16, background="magenta3", foreground="white", bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGALLAHIR.grid(row=4, column=1, padx=5, pady=5)
                    
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        columns = ('id', 'nim', 'nama', 'kelas', 'matkul', 'tanggal lahir')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        self.tree.heading('id', text='ID')
        self.tree.column('id', width=30)
        self.tree.heading('nim', text='NIM')
        self.tree.column('nim', width=65)
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width=80)
        self.tree.heading('kelas', text='Kelas')
        self.tree.column('kelas', width=65)
        self.tree.heading('matkul', text='Matkul')
        self.tree.column('matkul', width=110)
        self.tree.heading('tanggal lahir', text='Tanggal Lahir')
        self.tree.column('tanggal lahir', width=100)
        self.tree.place(x=0, y=250)
        self.onReload()

    
    def onClear(self, event=None):
        self.txtNIM.delete(0, END)
        self.txtNAMA.delete(0, END)
        self.txtKELAS.delete(0, END)
        self.txtMATKUL.delete(0, END)
        self.txtTANGGALLAHIR.delete(0, END)
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

        
    def onReload(self, event=None):
        obj = Datamahasiswa()
        result = obj.getAllData()
        self.tree.delete(*self.tree.get_children())
        for row in result:
            self.tree.insert('', END, values=row)
            
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        obj = Datamahasiswa()
        res = obj.getByNIM(nim)
        rec = obj.affected
        if rec > 0:
            messagebox.showinfo("Info", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Peringatan", "Data Tidak Ditemukan") 
            self.ditemukan = False
        return res
            
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        obj = Datamahasiswa()
        res = obj.getByNIM(nim)
        self.txtNAMA.delete(0, END)
        self.txtKELAS.delete(0, END)
        self.txtMATKUL.delete(0, END)
        self.txtTANGGALLAHIR.delete(0, END)
        self.txtNAMA.insert(END, obj.nama)
        self.txtKELAS.insert(END, obj.kelas)
        self.txtMATKUL.insert(END, obj.matkul)
        self.txtTANGGALLAHIR.insert(END, obj.tanggal_lahir)
        self.btnSimpan.config(text="Update")
    
    def onSimpan(self, event=None):
        nim = self.txtNIM.get()
        nama = self.txtNAMA.get()
        kelas = self.txtKELAS.get()
        matkul = self.txtMATKUL.get()
        tanggal_lahir = self.txtTANGGALLAHIR.get()
        obj = Datamahasiswa()
        obj.nim = nim
        obj.nama = nama
        obj.kelas = kelas
        obj.matkul = matkul
        obj.tanggal_lahir = tanggal_lahir
        if self.ditemukan:
            res = obj.updateByNIM(nim)
            ket = 'Diperbarui'
        else:
            res = obj.simpan()
            ket = 'Disimpan'
        rec = obj.affected
        if rec > 0:
            messagebox.showinfo("Info", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("Peringatan", f"Data Gagal {ket}")
        self.onClear()
        return rec
    
    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        obj = Datamahasiswa()
        obj.nim = nim
        if(self.ditemukan==True):
            res = obj.deleteByNIM(nim)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        self.onClear
    def onkeluar(self,event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__=='__main__':
    root = tk.Tk()
    aplikasi = FormDatamahasiswa(root,"Aplikasi Data Datamahasiswa")
    root.mainloop()
    
    

