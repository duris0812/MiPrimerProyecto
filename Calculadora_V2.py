import tkinter as tk
from tkinter import messagebox

def suma():
    calcular(lambda a, b: a + b)

def resta():
    calcular(lambda a, b: a - b)

def multiplicacion():
    calcular(lambda a, b: a * b)

def division():
    calcular(lambda a, b: a / b if b != 0 else "Error: División por cero")

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado.set(operacion(num1, num2))
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

root = tk.Tk()
root.title("Calculadora")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado, font=("Arial", 14))
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

btn_suma = tk.Button(frame, text="+", command=suma, width=5)
btn_suma.grid(row=3, column=0, pady=5)

btn_resta = tk.Button(frame, text="-", command=resta, width=5)
btn_resta.grid(row=3, column=1, pady=5)

btn_multiplicacion = tk.Button(frame, text="*", command=multiplicacion, width=5)
btn_multiplicacion.grid(row=4, column=0, pady=5)

btn_division = tk.Button(frame, text="/", command=division, width=5)
btn_division.grid(row=4, column=1, pady=5)

root.mainloop()