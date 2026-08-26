import tkinter as tk

def calc(op):
    try:
        a = float(e1.get())
        b = float(e2.get())
        if op == '+': r = a + b
        elif op == '-': r = a - b
        elif op == '*': r = a * b
        else: r = a / b if b else 'Error'
        l.config(text=str(r))
    except:
        l.config(text='Error')

root = tk.Tk()
root.title('Calc')
root.geometry('300x250')

tk.Label(root, text='Num 1:').pack()
e1 = tk.Entry(root); e1.pack()
tk.Label(root, text='Num 2:').pack()
e2 = tk.Entry(root); e2.pack()

f = tk.Frame(root); f.pack()
tk.Button(f, text='+', command=lambda: calc('+')).pack(side=tk.LEFT, padx=2)
tk.Button(f, text='-', command=lambda: calc('-')).pack(side=tk.LEFT, padx=2)
tk.Button(f, text='*', command=lambda: calc('*')).pack(side=tk.LEFT, padx=2)
tk.Button(f, text='/', command=lambda: calc('/')).pack(side=tk.LEFT, padx=2)

l = tk.Label(root, text='Result', font=('Arial', 14, 'bold'))
l.pack()

root.mainloop()
