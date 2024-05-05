import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="black")

        self.entry = tk.Entry(root, width=20, font=("Helvetica", 20), bd=5, justify="right", bg="black", fg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=("Helvetica", 20),
                                command=lambda t=text: self.on_button_click(t), bg="black", fg="orange")
            button.grid(row=row, column=col, padx=5, pady=5)
            button.config(borderwidth=0, highlightthickness=0)
            button.config(activebackground="orange", activeforeground="black")
            button.config(relief=tk.RAISED)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    calculator = Calculator(root)
    root.mainloop()
