import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os


filenameT="new.c"
class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("IDE faucc")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        
        self.text_area2 = tk.Text(self.root, height=10, width=50)
        self.text_area2.pack(pady=10)

        # Botões
        self.open_button = tk.Button(self.root, text="open", command=self.opens)
        self.open_button.pack(pady=5)
        
        self.save_button = tk.Button(self.root, text="save", command=self.saves)
        self.save_button.pack(pady=5)
        
        self.ssource_button = tk.Button(self.root, text="save source", command=self.savessources)
        self.ssource_button.pack(pady=5)
        
        self.compile_button = tk.Button(self.root, text="compile", command=self.compiles)
        self.compile_button.pack(pady=5)
        
        self.source_button = tk.Button(self.root, text="source", command=self.sources)
        self.source_button.pack(pady=5)
        
        self.run_button = tk.Button(self.root, text="Run", command=self.Runs)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="new file", command=self.copy_file)
        self.copy_button.pack(pady=5)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            if show:
                self.text_area2.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area2.insert(tk.END,f"Error executing command:\n{e.output}")

    def saves(self):
        global filenameT
        ss=self.text_area.get("1.0","end-1c")
        filename = tk.asksaveasfilename(title="Select file")
        t=filename.split(".")
        filenameT=t[0]
        f1=open(filename,"w")
        f1.write(ss)
        f1.close()
    def savessources(self):
        global filenameT
        ss=self.text_area.get("1.0","end-1c")
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        t=filename.split(".")
        
        f1=open(filename,"w")
        f1.write(ss)
        f1.close()
 
    def opens(self):
        global filenameT
        self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.askopenfilename(title="Select file")
        t=filename.split(".")
        filenameT=t[0]
        f1=open(filename,"r")
        ss=f1.read()
        f1.close()
        self.text_area.insert(tk.END,ss)
        
    def compiles(self):
        global filenameT
        self.text_area2.delete(1.0, tk.END)
        
        self.execute_command("faucc -o $filenames $filenames.c".replace("$filenames",filenameT),True)

    def sources(self):
        global filenameT
        self.text_area2.delete(1.0, tk.END)
        self.execute_command("faucc -o $filenames.s $filenames.c -S -masm=intel ".replace("$filenames",filenameT),False)
        filename =filenameT+".s"
        f1=open(filename,"r")
        ss=f1.read()
        f1.close()
        self.text_area2.insert(tk.END,ss)
        
    def Runs(self):
        global filenameT
        self.text_area2.delete(1.0, tk.END)
        self.execute_command('xterm "$filenames"'.replace("$filenames",filenameT) ,True)        
        
        
    def copy_file(self):
        self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        if filename:
            shutil.copy( f"./file/new",filename+".c")
            self.text_area.insert(tk.END, f"File {filename} copied \n",True)


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
