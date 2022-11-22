import tkinter
from tkinter import ttk

def seleccionar():
    monitor.config(text="{}".format(selected.get()))

def reinicio():
    selected.set(None)
    monitor.config(text="")

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=6)

selected = tkinter.StringVar()
selected.set(None)
r1 = ttk.Radiobutton(window, text='Si', value='Si', variable=selected, command=seleccionar)
r2 = ttk.Radiobutton(window, text='No', value='No', variable=selected, command=seleccionar)
r3 = ttk.Radiobutton(window, text='Quizás', value='Quizás', variable=selected, command=seleccionar)
boton_reinicio = ttk.Button(window, text='Reiniciar valores', command=reinicio)
monitor = ttk.Label(window)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
monitor.grid(column=0, row=4, padx=5, pady=5)
boton_reinicio.grid(column=0, row=5, padx=5, pady=5)



window.mainloop()