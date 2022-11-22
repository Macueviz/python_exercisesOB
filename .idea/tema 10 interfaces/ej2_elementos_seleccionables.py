import tkinter

window = tkinter.Tk()

#selected = tkinter.StringVar()
lista = ['Coche', 'Motocicleta', 'Andando', 'Transporte público']
lista_items = tkinter.StringVar(value=lista)

label = tkinter.Label(window, text='¿Cómo prefieres ir al trabajo?')
listbox = tkinter.Listbox(window, height=100, listvariable= lista_items)

label.pack(ipadx=25, ipady=25, fill='x')
listbox.pack(ipadx=45, ipady=45)
window.mainloop()