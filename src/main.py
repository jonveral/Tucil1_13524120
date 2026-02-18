import tkinter as tk
from tampilan import AplikasiQueens

def main():
    root = tk.Tk()
    app = AplikasiQueens(root)
    root.mainloop()

if __name__ == "__main__":
    main()