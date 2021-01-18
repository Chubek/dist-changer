import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from replace_distribution import iter




class GUI:

    def __init__(self, window):
        self.window = window

        self.title = "Answer Changer GUI"

        window.title(self.title)
      
        window.rowconfigure(0, minsize=800, weight=1)
        window.columnconfigure(1, minsize=200, weight=1)
        
        self.frm_stuff = tk.Frame(window)
        
        self.txt_edit = tk.Text(window)
        self.ent_pcnt = tk.Entry(self.frm_stuff)
        self.ent_iter = tk.Entry(self.frm_stuff)
        self.lbl_pcnt = tk.Label(self.frm_stuff, text="Percent")
        self.lbl_iter = tk.Label(self.frm_stuff, text="Num Iter")
        self.is_lower = tk.BooleanVar()
        self.cbox_islower = tk.Checkbutton(self.frm_stuff, text='Lowercase?', variable=self.is_lower, onvalue=True, offvalue=False)
        self.btn_open = tk.Button(self.frm_stuff, text="Open", command=self.__open_file)
        self.btn_save = tk.Button(self.frm_stuff, text="Save As...", command=self.__save_file)
        self.btn_op = tk.Button(self.frm_stuff, text="Operate", command=self.__operate)
        self.btn_clear = tk.Button(self.frm_stuff, text="Clear", command=lambda: self.txt_edit.delete("1.0", tk.END))

        self.txt_edit.grid(row=0, column=0, sticky="nsew")
        self.frm_stuff.grid(row=0, column=1, sticky="nsew", padx=26)

        self.lbl_iter.grid(row=0, column=0, sticky="nsew")
        self.lbl_pcnt.grid(row=2, column=0, sticky="nsew")
        self.btn_open.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=6, column=0, sticky="ew", padx=5)
        self.ent_pcnt.grid(row=3, column=0, sticky="nsew")
        self.ent_iter.grid(row=1, column=0, sticky="nsew")
        self.cbox_islower.grid(row=4, column=0, sticky="nsew")
        self.btn_op.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
        self.btn_clear.grid(row=8, column=0, sticky="ew", padx=5, pady=5)

    
    def __open_file(self):
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if not filepath:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        self.title = f"Answer Changer GUI - {filepath}"


    def __save_file(self):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.txt_edit.get(1.0, tk.END)
            output_file.write(text)
        self.title = f"Answer Changer GUI - {filepath}"

    def __operate(self):
        txt = self.txt_edit.get(1.0, tk.END)

        try:
            txt_split = txt.split(",")
        except:
            messagebox.showerror("Entry Error!", "Text Doesn't Contain Any Commas")
            return

        if len(txt) <= 1:
            messagebox.showerror("Entry Error!", "Text Not Entered")
            return

        try:
            pcnt = float(self.ent_pcnt.get())
        except:
            messagebox.showerror("Entry Error!", "Percent Not Entered")
            return
        try:    
            num_iter = int(self.ent_iter.get())
        except:
            messagebox.showerror("Entry Error!", "Iter Number Not Entered")
            return

        is_lower = self.is_lower.get()

        print(is_lower, "is_lower")

        outputs = "\n".join(iter(num_iter, pcnt, txt, is_lower))

        self.txt_edit.delete("1.0", tk.END)
        self.txt_edit.insert(tk.END, outputs)





        