import tkinter as tk
from tkinter import filedialog
import time
import threading
from algoritma import PapanQueens 

class AplikasiQueens:
    def __init__(self, master):
        self.master = master
        self.master.title("Penyelesaian Permainan Queens Linkedin")
        self.master.geometry("700x900")
        
        self.data_papan = []
        self.n = 0
        self.solusi_akhir = []
        self.kotak_gui = []
        self.lagi_jalan = False
        self.waktu_mulai = 0
        self.warna_list = ["#FF595E", "#FFCA3A", "#8AC926", "#1982C4", "#6A4C93",
                           "#FF924C", "#25A18E", "#FF6392", "#562C2C", "#D8E2DC"]
        self.buat_ui()

    def buat_ui(self):
        tk.Label(self.master, text="QUEENS", font=("Helvetica", 22, "bold"), pady=20).pack()

        frame_ctrl = tk.Frame(self.master)
        frame_ctrl.pack(pady=10)
        
        self.btn_pilih = tk.Button(frame_ctrl, text="LOAD FILE", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=15, command=self.pilih_file)
        self.btn_pilih.pack(side=tk.LEFT, padx=10)
        
        self.btn_run = tk.Button(frame_ctrl, text="SOLVE", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=15, state="disabled", command=self.mulai_cari)
        self.btn_run.pack(side=tk.LEFT, padx=10)
        
        self.txt_status = tk.StringVar(value="Status: Siap")
        tk.Label(self.master, textvariable=self.txt_status, font=("Consolas", 11)).pack()

        self.lbl_waktu = tk.Label(self.master, text="Waktu pencarian: 0 ms", font=("Consolas", 11))
        self.lbl_waktu.pack()
        self.lbl_iterasi = tk.Label(self.master, text="Banyak kasus yang ditinjau: 0", font=("Consolas", 11))
        self.lbl_iterasi.pack()

        self.frame_simpan = tk.Frame(self.master)
        self.lbl_tanya = tk.Label(self.frame_simpan, text="Apakah Anda ingin menyimpan solusi? (Ya/Tidak)", 
                                 font=("Consolas", 11, "bold"), pady=5)
        self.lbl_tanya.pack()
        
        f_btn_simpan = tk.Frame(self.frame_simpan)
        f_btn_simpan.pack()
        tk.Button(f_btn_simpan, text="Ya", width=10, command=self.aksi_simpan).pack(side=tk.LEFT, padx=5)
        tk.Button(f_btn_simpan, text="Tidak", width=10, command=self.aksi_batal).pack(side=tk.LEFT, padx=5)

        self.area_papan = tk.Frame(self.master, borderwidth=1, relief="solid")
        self.area_papan.pack(padx=20, pady=20)

    def pilih_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.frame_simpan.pack_forget()
            with open(path, 'r') as f:
                baris_teks = [l.strip() for l in f.readlines() if l.strip()]
            
            self.data_papan = [list(l) for l in baris_teks]
            self.n = len(self.data_papan)
            self.buat_grid_papan()
            self.btn_run.config(state="normal")
            self.txt_status.set(f"Papan {self.n}x{self.n} dimuat.")

    def buat_grid_papan(self):
        for w in self.area_papan.winfo_children(): w.destroy()
        self.kotak_gui = []
        chars = sorted(list(set(c for r in self.data_papan for c in r)))
        cmap = {h: self.warna_list[i % len(self.warna_list)] for i, h in enumerate(chars)}
        
        for r in range(self.n):
            baris_kotak = []
            for c in range(self.n):
                l = tk.Label(self.area_papan, text="", bg=cmap[self.data_papan[r][c]], 
                             width=4, height=2, relief="solid", borderwidth=1, font=("Arial", 14, "bold"))
                l.grid(row=r, column=c)
                baris_kotak.append(l)
            self.kotak_gui.append(baris_kotak)

    def refresh_papan(self, solusi):
        for r in range(self.n):
            for c in range(self.n):
                self.kotak_gui[r][c].config(text="Q" if solusi[r] == c else "")
        self.master.update_idletasks()

    def timer_loop(self):
        if self.lagi_jalan:
            skrg = (time.time() - self.waktu_mulai) * 1000
            self.lbl_waktu.config(text=f"Waktu pencarian: {skrg:.2f} ms")
            self.master.after(50, self.timer_loop)

    def mulai_cari(self):
        self.frame_simpan.pack_forget()
        self.btn_run.config(state="disabled")
        self.lagi_jalan = True
        self.waktu_mulai = time.time()
        self.timer_loop()
        threading.Thread(target=self.proses_hitung, daemon=True).start()

    def proses_hitung(self):
        solver = PapanQueens(self.data_papan)
        self.solusi_akhir = [0] * self.n
        ketemu = solver.cari_exhaustive(0, self.solusi_akhir, self.refresh_papan)
        durasi = (time.time() - self.waktu_mulai) * 1000
        self.lagi_jalan = False
        
        self.master.after(0, lambda: self.lbl_waktu.config(text=f"Waktu pencarian: {durasi:.2f} ms"))
        self.master.after(0, lambda: self.lbl_iterasi.config(text=f"Banyak kasus yang ditinjau: {solver.total_iterasi} kasus"))
        
        if ketemu:
            self.master.after(0, self.sukses_ketemu)
        else:
            self.master.after(0, lambda: self.txt_status.set("Status: Tidak ada solusi!"))
        self.master.after(0, lambda: self.btn_run.config(state="normal"))

    def sukses_ketemu(self):
        self.refresh_papan(self.solusi_akhir)
        self.txt_status.set("Status: Solusi Ditemukan!")
        self.frame_simpan.pack(pady=10)

    def aksi_simpan(self):
        nama_file = "solusi.txt"
        with open(nama_file, 'w') as f:
            for r in range(self.n):
                row = "".join(["#" if self.solusi_akhir[r] == c else self.data_papan[r][c] for c in range(self.n)])
                f.write(row + "\n")
        self.frame_simpan.pack_forget()
        self.txt_status.set(f"Status: Solusi berhasil disimpan di {nama_file}!")

    def aksi_batal(self):
        self.frame_simpan.pack_forget()
        self.txt_status.set("Status: Penyimpanan dibatalkan.")