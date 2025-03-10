import tkinter as tk


class Window:
    def __init__(self, master):
        label_frame = tk.LabelFrame(master, text="LABELFRAME WIDGET")
        label_frame.pack(padx=5, pady=5)

        var = tk.IntVar()

        radio1 = tk.Radiobutton(label_frame, text="Option1", variable=var, value=1)
        radio2 = tk.Radiobutton(label_frame, text="Option2", variable=var, value=2)
        radio3 = tk.Radiobutton(label_frame, text="Option3", variable=var, value=3)

        radio1.pack(padx=5, pady=5)
        radio2.pack(padx=5, pady=5)
        radio3.pack(padx=5, pady=5)


root = tk.Tk()
root.geometry("300x200")
window = Window(root)
root.mainloop()
