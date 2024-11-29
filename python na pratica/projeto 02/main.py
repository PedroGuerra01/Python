import tkinter as tk
import datetime

# Função para verificar o período (dia ou noite)
def verificar_periodo():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual < 18:
        return "dia", "#D3D3D3"  # Dia, luz apagada
    else:
        return "noite", "#FFD700"  # Noite, luz acesa

# Função para atualizar a interface com base no período
def atualizar_interface():
    periodo, cor_luz = verificar_periodo()
    mensagem.config(text=f"Pelo visto está de {periodo}.")
    
    # Alterando as cores das janelas do prédio
    for janela in janelas:
        canvas.itemconfig(janela, fill=cor_luz)

# Criando a janela principal
root = tk.Tk()
root.title("Simulação de Luzes do Prédio")
root.geometry("300x400")

# Criando um canvas para desenhar o prédio
canvas = tk.Canvas(root, width=300, height=350, bg="skyblue")
canvas.pack()

# Desenhando o prédio (representação das janelas)
janelas = []
for i in range(3):  # 3 andares
    for j in range(2):  # 2 janelas por andar
        janela = canvas.create_rectangle(50 + j * 100, 50 + i * 100, 150 + j * 100, 150 + i * 100, fill="#D3D3D3")
        janelas.append(janela)  # Guardamos os IDs dos retângulos, não o itemconfig

# Adicionando uma label para mostrar a mensagem interativa
mensagem = tk.Label(root, text="Pelo visto está de dia.", font=("Arial", 14))
mensagem.place(x=125, y=350)  # Colocando o texto inicialmente fora da tela (embaixo)

# Atualizando a interface para refletir o estado atual
atualizar_interface()

# Atualizando a interface a cada 60 segundos
root.after(60000, atualizar_interface)

# Iniciando o loop principal da interface
root.mainloop()
