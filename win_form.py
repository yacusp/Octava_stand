from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

window = Tk()
window.title("Стенд испытания шасси")
#window.geometry('310x300')
lbl_1 = Label(window, text="Порт", width=15, height=1)
lbl_1.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)
lbl_2 = Label(window, text="Скорость", width=15, height=1)
lbl_2.grid(row=0, column=1, padx=5, pady=5, sticky=W+E)

combo_1 = Combobox(window, width=15, height=1)
combo_1['values'] = (1, 2, 3, 4, 5, "Текст")
combo_1.current(1)  # установите вариант по умолчанию
combo_1.grid(row=1, column=0)
combo_2 = Combobox(window, width=15, height=1)
combo_2['values'] = (1, 2, 3, 4, 5, "Текст")
combo_2.current(1)  # установите вариант по умолчанию
combo_2.grid(row=1, column=1)

txt = Entry(window, width=10)
txt.grid(row=2, columnspan=2, padx=5, pady=5, sticky=W+E)
btn = Button(window, text="Клик!", width=30, height=1, command=clicked)
btn.grid(row=3, columnspan=2, padx=5, pady=5)
window.mainloop()
