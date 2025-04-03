import tkinter as tk
from tkinter import ttk, messagebox

def calcular(operacion):
    """ Realiza la operación matemática y maneja errores """
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operacion == "/" and num2 == 0:
            raise ZeroDivisionError
        resultado = operacion(num1, num2)
        resultado_var.set(round(resultado, 4))
        historial.insert(tk.END, f"{num1} {operacion.__name__} {num2} = {resultado}\n")
        historial.see(tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por 0")

def limpiar():
    """ Limpia las entradas y el resultado """
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado_var.set("")

def limpiar_historial():
    """ Limpia el historial de operaciones """
    historial.delete("1.0", tk.END)

def salir():
    """ Cierra la aplicación """
    root.quit()

def tecla_enter(event):
    """ Ejecuta la última operación cuando se presiona Enter """
    if ultima_operacion.get():
        calcular(ultima_operacion.get())

root = tk.Tk()
root.title("Calculadora V2.1 Mejorada")
root.geometry("400x500")
root.resizable(False, False)

# Marco principal
frame = ttk.Frame(root, padding=10)
frame.pack()

# Entradas
entry1 = ttk.Entry(frame, font=("Arial", 14))
entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
entry2 = ttk.Entry(frame, font=("Arial", 14))
entry2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Resultado
resultado_var = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado_var, font=("Arial", 16), foreground="blue")
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

# Botones de operación
ultima_operacion = tk.StringVar()

botones = [
    ("+", lambda a, b: a + b, 3, 0),
    ("-", lambda a, b: a - b, 3, 1),
    ("*", lambda a, b: a * b, 4, 0),
    ("/", lambda a, b: a / b, 4, 1),
    ("%", lambda a, b: a % b, 5, 0)
]

for simbolo, operacion, fila, columna in botones:
    def click(op=operacion):
        ultima_operacion.set(op)
        calcular(op)
    
    ttk.Button(frame, text=simbolo, command=click, width=6).grid(row=fila, column=columna, pady=5)

# Botones adicionales
ttk.Button(frame, text="Limpiar", command=limpiar, width=13).grid(row=6, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Limpiar Historial", command=limpiar_historial, width=13).grid(row=7, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Salir", command=salir, width=13).grid(row=8, column=0, columnspan=2, pady=5)

# Historial con scrollbar
hist_frame = ttk.Frame(root)
hist_frame.pack(pady=10)

scrollbar = ttk.Scrollbar(hist_frame)
historial = tk.Text(hist_frame, height=6, width=40, font=("Arial", 10), yscrollcommand=scrollbar.set)
scrollbar.config(command=historial.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
historial.pack(side=tk.LEFT)

# Vincular Enter con la última operación seleccionada
root.bind("<Return>", tecla_enter)

root.mainloop()
