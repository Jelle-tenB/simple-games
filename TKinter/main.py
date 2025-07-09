import tkinter as tk

window = tk.Tk()
window.title("Convert Mile to Kilometer")
window.config(padx=20, pady=20)


def convert():
    miles = float(entry.get())
    km = miles * 1.6
    kilometers.config(text=f'{km}')


entry = tk.Entry(width=7)
entry.insert(tk.END, string='0')
entry.grid(column=1, row=0)

# Label
my_label = tk.Label(text="Miles")
my_label.grid(column=2, row=0)

equal = tk.Label(text='is equal to')
equal.grid(column=0, row=1)

kilometers = tk.Label(text='0')
kilometers.grid(column=1, row=1)

km_label = tk.Label(text='Km')
km_label.grid(column=2, row=1)

button = tk.Button(text='Calculate', command=convert)
button.grid(column=1, row=2)

window.mainloop()
