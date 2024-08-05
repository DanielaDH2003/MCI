import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os

def calcular_bmi():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if altura > 3:
            altura /= 100
        
        bmi = peso / (altura ** 2)
        
        label_resultado.config(text=f"BMI: {bmi:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def guardar_datos():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if altura > 3:
            altura /= 100
        
        bmi = peso / (altura ** 2)
        
        nombre_archivo = f"{nombre}.csv"
        
        archivo_nuevo = not os.path.isfile(nombre_archivo)
        
        with open(nombre_archivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if archivo_nuevo:
                writer.writerow(["Nombre", "Edad", "Sexo", "Peso", "Altura", "BMI"])
            
            writer.writerow([nombre, edad, sexo, peso, altura, bmi])
        
        messagebox.showinfo("Guardado", f"Datos guardados en {nombre_archivo}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

root = tk.Tk()
root.title("Calculadora de BMI")

image = Image.open("fondo.png")
fondo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=fondo.width(), height=fondo.height())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

canvas_width = fondo.width()
canvas_height = fondo.height()

x_center = canvas_width // 2
y_start = 50
y_step = 60

font_style = ("Helvetica", 16, "bold italic")
title_font_style = ("Helvetica", 24, "bold")

def create_labeled_entry(canvas, label_text, font, y_pos, entry_width=25):
    frame = tk.Frame(root, bg="white")
    label = tk.Label(frame, text=label_text, font=font, fg="#000000", bg="white")
    entry = tk.Entry(frame, width=entry_width)
    label.pack(side="left", padx=5)
    entry.pack(side="left", padx=5)
    canvas.create_window(x_center, y_pos, anchor="n", window=frame)
    return entry

# Título de la aplicación
label_title = tk.Label(root, text="Calculo de BMI", font=title_font_style, fg="#000000", bg="white")
canvas.create_window(x_center, y_start, anchor="n", window=label_title)

entry_nombre = create_labeled_entry(canvas, "Nombre:", font_style, y_start + y_step)
entry_edad = create_labeled_entry(canvas, "Edad:", font_style, y_start + 2 * y_step, entry_width=10)
entry_sexo = create_labeled_entry(canvas, "Sexo:", font_style, y_start + 3 * y_step)
entry_peso = create_labeled_entry(canvas, "Peso (kg):", font_style, y_start + 4 * y_step, entry_width=10)
entry_altura = create_labeled_entry(canvas, "Altura (m):", font_style, y_start + 5 * y_step, entry_width=10)

img_calcular = Image.open("Calcular.png").resize((120, 80), Image.LANCZOS)
img_guardar = Image.open("guardar1.png").resize((120, 80), Image.LANCZOS)

photo_calcular = ImageTk.PhotoImage(img_calcular)
photo_guardar = ImageTk.PhotoImage(img_guardar)

button_calcular = tk.Button(root, image=photo_calcular, command=calcular_bmi, cursor="hand2", borderwidth=0)
canvas.create_window(x_center - 80, y_start + 7 * y_step, anchor="e", window=button_calcular)

button_guardar = tk.Button(root, image=photo_guardar, command=guardar_datos, cursor="hand2", borderwidth=0)
canvas.create_window(x_center + 80, y_start + 7 * y_step, anchor="w", window=button_guardar)

label_resultado = tk.Label(root, text="BMI:", font=font_style, fg="#000000", bg="white")
canvas.create_window(x_center, y_start + 8 * y_step, anchor="center", window=label_resultado)

root.mainloop()
