import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("文本编辑器")
        self.text = tk.Text(self.root, wrap='word')
        self.text.pack(expand=True, fill='both')
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()