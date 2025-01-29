import requests
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox

# receber informacoes do clima
def clima(cidade):
    api_key = "4c60d81d6fed58d57ba080a02e83681f"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        c = temp - 273
        c = int(c)
        return c, desc
    else: 
        return "Erro"

# funcao na qual mostra as informacoes na label "sexo"
def mostrar():
    cidade = entrada.get()
    temp_desc = clima(cidade)

    if temp_desc == "Erro":
        messagebox.showerror("Erro", "Local não encontrado")
    else:
        sexo.config(text=f"Temperatura: {temp_desc[0]}°C \nDescrição: {temp_desc[1]}", font=("Arial", 15))


# Configurações da janela
root = tk.Tk()
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(400,400)
root.title("Clima")
root.configure(background='light blue')

# titulo do bagulho e frases
fodase = Label(root, text="Verificador de Clima", font=("Comic Sans MS", 20), bg="Light Blue")
fodase.pack(pady=10)
b = Label(root, text="Qual Local?", font=("Arial", 10),bg="Light Blue")
b.pack(pady=10)

# input
entrada = tk.Entry(root)
entrada.pack()

# botao
botao = tk.Button(root, text="ver clima", command=mostrar, bg="dark red", fg="white")
botao.pack(pady=10)

# onde vai aparecer as informaçoes
sexo = Label(root, text="",justify=tk.LEFT,bg="Light Blue")
sexo.pack()


# creditos
footer_label = tk.Label(root, text="feito por preyzin", font=("Comic Sans MS", 8), bg='Light Blue', fg="purple")
footer_label.pack(side="bottom", pady=10)


# chama a janela
root.mainloop()     