import tkinter as tk
from tkinter import PhotoImage, messagebox

def button_clicked():
    messagebox.showinfo("Notificación", "El botón fue presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Botón con Imagen en Tkinter")

# Cargar la imagen
button_image = PhotoImage(file="logo.png") # Reemplaza con la ruta de tu imagen

# Crear un botón y usar la imagen como fondo
image_button = tk.Button(root, image=button_image, command=button_clicked, borderwidth=0)
image_button.pack(pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()