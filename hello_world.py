import tkinter as tk

#create a window / initialize
root = tk.Tk()
root.title("Hello World")
root.iconbitmap('Tick_Mark.ico')
width , height = 400, 400
root.resizable(False,False)
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}')
#run the window
root.mainloop()