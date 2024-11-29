import tkinter as tk
import datetime

# Função para verificar o período (dia ou noite)
def verificar_periodo():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual < 18:
        return "dia", "#D3D3D3"  # Dia, luz apagada
    else:
        return "noite", "#FFD700"  # Noite, luz acesa

# Função para alternar as luzes
def alternar_luzes():
    global luzes_acesas
    luzes_acesas = not luzes_acesas  # Alterna o estado das luzes

    if luzes_acesas:
        botao_luzes.config(text="Apagar Luzes")  # Se as luzes estão acesas, o botão vai "Apagar Luzes"
    else:
        botao_luzes.config(text="Acender Luzes")  # Se as luzes estão apagadas, o botão vai "Acender Luzes"
    
    atualizar_interface()

# Função para atualizar a interface com base no estado das luzes
def atualizar_interface():
    if luzes_acesas:
        cor_luz = "#FFD700"  # Luz acesa (cor amarela)
    else:
        cor_luz = "#D3D3D3"  # Luz apagada (cor cinza)
    
    periodo, _ = verificar_periodo()
    horario_atual = datetime.datetime.now().strftime("%H:%M:%S")  # Formato HH:MM:SS
    mensagem.config(text=f"Pelo visto está de {periodo}.\nHorário atual: {horario_atual}")

    # Alterando as cores das janelas do prédio
    for janela in janelas:
        canvas.itemconfig(janela, fill=cor_luz)

    # Reagendar a atualização para o próximo segundo
    root.after(1000, atualizar_interface)

# Criando a janela principal
root = tk.Tk()
root.title("Simulação de Luzes do Prédio")
root.geometry("300x450")  # Aumentei a altura para caber o botão no topo

# Criando um canvas para desenhar o prédio
canvas = tk.Canvas(root, width=300, height=350, bg="skyblue")
canvas.pack()

# Desenhando o prédio (representação das janelas)
janelas = []
for i in range(3):  # 3 andares
    for j in range(2):  # 2 janelas por andar
        janela = canvas.create_rectangle(50 + j * 100, 50 + i * 100, 150 + j * 100, 150 + i * 100, fill="#D3D3D3")
        janelas.append(janela)

# Adicionando uma label para mostrar a mensagem interativa
mensagem = tk.Label(root, text="", font=("Arial", 14), bg="skyblue")
mensagem.place(x=150, y=430, anchor="center")  # Centralizado horizontalmente e abaixo do canvas

# Variável de controle para o estado das luzes (começa com as luzes apagadas)
luzes_acesas = False

# Adicionando o botão para acender e apagar as luzes
botao_luzes = tk.Button(root, text="Acender Luzes", font=("Arial", 12), command=alternar_luzes)
botao_luzes.pack(pady=10)  # O botão fica no topo com algum espaço abaixo dele

# Atualizando a interface para refletir o estado atual
atualizar_interface()

# Iniciando o loop principal da interface
root.mainloop()
