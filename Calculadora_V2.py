#Calculadora_V2
import tkinter as tk
from tkinter import messagebox

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = operacion(num1, num2)
        resultado_var.set(resultado)
        historial.insert(tk.END, f"{num1} {operacion.__name__} {num2} = {resultado}\n")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números validos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por 0")

def limpiar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado_var.set("")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Calculadora V2")
root.geometry("300x400")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

resultado_var = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado_var, font=("Arial", 14))
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

botones = [
    ("+", lambda a, b: a + b, 3, 0),
    ("-", lambda a, b: a - b, 3, 1),
    ("*", lambda a, b: a * b, 4, 0),
    ("/", lambda a, b: a / b if b != 0 else float('inf'), 4, 1)
]

for simbolo, operacion, fila, columna in botones:
    tk.Button(frame, text=simbolo, command=lambda op=operacion: calcular(op), width=5).grid(row=fila, column=columna, pady=5)

tk.Button(frame, text="Limpiar", command=limpiar, width=10).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Salir", command=salir, width=10).grid(row=6, column=0, columnspan=2, pady=5)

historial = tk.Text(root, height=6, width=35)
historial.pack(pady=10)

root.mainloop()
