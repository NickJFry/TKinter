import tkinter as tk


def delete_entry():
    wish.delete(0, tk.END)


def get_entry():
    value = wish.get()
    len_value = len(value)
    if len_value < 2:
        delete_entry()
        return label_2.pack()
    else:
        label_2.destroy()
        return label_3.pack()


win = tk.Tk()
win.title('Сюда пиши желание')
photo = tk.PhotoImage(file='make_wish.png')
win.iconphoto(False, photo)
win.config(bg='#F0FFF0')
win.geometry('500x200+400+100')
win.minsize(300, 100)
win.maxsize()
win.resizable(True, True)

label_1 = tk.Label(win, text='Желай пиши',
                   bg='#F0FFF0',
                   font=('Roboto,', 20),
                   # padx=15,
                   # pady=20,
                   )
label_1.pack()
label_2 = tk.Label(win, text='Мало символов')
label_3 = tk.Label(win, text='Записано')


wish = tk.Entry(win)
wish.pack()

button_1 = tk.Button(win, text='Хочу!',
                     command=get_entry,
                     bg='#F0FFF0',
                     activebackground='green',)
button_1.pack()
win.mainloop()
