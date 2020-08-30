import tkinter as tk


def pag_one(window):
  label = tk.Label(window, text = 'HOLA MUNDO', fg = 'blue').grid(row = 0, column = 0, columnspan = 2, sticky = 'n', pady = 50)

  button_next = tk.Button(window, text = 'next', command = pag_two).grid(row = 1, columnspan = 2, pady = 15)


def pag_two(window):
  label = tk.Label(window, text = 'MARICO EL QUE LO LEA JSJS', fg = 'red').grid(row = 0, column = 0, columnspan = 2, sticky = 'n', pady = 50)

  button_back = tk.Button(window, text = 'black', command = pag_one).grid(row = 1,columnspan = 2, pady = 15)


def pag_view(window):
  pag_one()


if __name__ == "__main__":
  window = tk.Tk()
  pag_view(window)
  window.mainloop()