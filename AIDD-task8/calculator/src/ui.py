import tkinter as tk

class CalculatorUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 16), borderwidth=5, relief=tk.RIDGE)
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            tk.Button(master, text=button_text, width=5, height=2, command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        tk.Button(master, text="=", width=23, height=2, command=self.calculate).grid(row=5, column=0, columnspan=4, pady=2)

    def on_button_click(self, text):
        if text == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()
