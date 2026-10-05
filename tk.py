import tkinter as tk
from tkinter import ttk

# --- Configuração Principal da Janela ---
root = tk.Tk()
root.title("TASKMANAGER")
root.geometry("900x600")
root.configure(bg="#F4F5F7")

# --- CORES E ESTILOS ---
COLOR_BG = "#F4F5F7"
COLOR_SIDEBAR = "#FFFFFF"
COLOR_CARD = "#FFFFFF"
COLOR_TEXT = "#333333"
COLOR_PRIMARY = "#6C5CE7"

style = ttk.Style()
style.theme_use("clam")

# --- 1. HEADER SUPERIOR ---
header = tk.Frame(root, bg=COLOR_SIDEBAR, height=50, highlightbackground="#E0E0E0", highlightthickness=1)
header.pack(fill="x", side="top")

lbl_title = tk.Label(header, text="TASKMANAGER", font=("Helvetica", 12, "bold"), bg=COLOR_SIDEBAR, fg=COLOR_TEXT)
lbl_title.pack(side="left", padx=20, pady=10)

lbl_user = tk.Label(header, text="👤 Usuário", font=("Helvetica", 10), bg=COLOR_SIDEBAR, fg=COLOR_TEXT)
lbl_user.pack(side="right", padx=20, pady=10)

# --- CORPO DA APLICAÇÃO (Sidebar + Main) ---
body = tk.Frame(root, bg=COLOR_BG)
body.pack(fill="both", expand=True)

# --- 2. MENU LATERAL (SIDEBAR) ---
sidebar = tk.Frame(body, bg=COLOR_SIDEBAR, width=180, highlightbackground="#E0E0E0", highlightthickness=1)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

btn_inicio = tk.Button(sidebar, text="🏠 Início", anchor="w", relief="flat", bg=COLOR_SIDEBAR, font=("Helvetica", 10, "bold"), fg=COLOR_PRIMARY)
btn_inicio.pack(fill="x", padx=15, pady=(20, 5))

btn_tarefas = tk.Button(sidebar, text="📋 Tarefas", anchor="w", relief="flat", bg=COLOR_SIDEBAR, font=("Helvetica", 10), fg=COLOR_TEXT)
btn_tarefas.pack(fill="x", padx=15, pady=5)

btn_agenda = tk.Button(sidebar, text="📅 Agenda", anchor="w", relief="flat", bg=COLOR_SIDEBAR, font=("Helvetica", 10), fg=COLOR_TEXT)
btn_agenda.pack(fill="x", padx=15, pady=5)

btn_config = tk.Button(sidebar, text="⚙ Config.", anchor="w", relief="flat", bg=COLOR_SIDEBAR, font=("Helvetica", 10), fg=COLOR_TEXT)
btn_config.pack(fill="x", padx=15, pady=5)

# --- 3. ÁREA PRINCIPAL DE CONTEÚDO ---
main_content = tk.Frame(body, bg=COLOR_BG, padx=20, pady=20)
main_content.pack(side="right", fill="both", expand=True)

lbl_dashboard = tk.Label(main_content, text="DASHBOARD", font=("Helvetica", 14, "bold"), bg=COLOR_BG, fg=COLOR_TEXT)
lbl_dashboard.pack(anchor="w", pady=(0, 15))

# --- 4. CARDS / INDICADORES ---
cards_frame = tk.Frame(main_content, bg=COLOR_BG)
cards_frame.pack(fill="x", pady=(0, 20))

def create_card(parent, title, value):
    card = tk.Frame(parent, bg=COLOR_CARD, padx=15, pady=15, highlightbackground="#E0E0E0", highlightthickness=1)
    lbl_val = tk.Label(card, text=value, font=("Helvetica", 18, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT)
    lbl_val.pack(anchor="center")
    lbl_txt = tk.Label(card, text=title, font=("Helvetica", 9), bg=COLOR_CARD, fg="#666666")
    lbl_txt.pack(anchor="center")
    return card

card1 = create_card(cards_frame, "Tarefas", "12")
card1.pack(side="left", fill="x", expand=True, padx=(0, 10))

card2 = create_card(cards_frame, "Pendentes", "05")
card2.pack(side="left", fill="x", expand=True, padx=5)

card3 = create_card(cards_frame, "Concluídas", "07")
card3.pack(side="left", fill="x", expand=True, padx=(10, 0))

# --- 5. SECÇÃO "PRÓXIMAS TAREFAS" ---
lbl_proximas = tk.Label(main_content, text="Próximas tarefas", font=("Helvetica", 11, "bold"), bg=COLOR_BG, fg=COLOR_TEXT)
lbl_proximas.pack(anchor="w", pady=(0, 10))

list_frame = tk.Frame(main_content, bg=COLOR_CARD, highlightbackground="#E0E0E0", highlightthickness=1)
list_frame.pack(fill="both", expand=True)

# Item 1
item1 = tk.Frame(list_frame, bg=COLOR_CARD, pady=8, padx=10)
item1.pack(fill="x")
chk1 = tk.Checkbutton(item1, text="Criar documentação", bg=COLOR_CARD, font=("Helvetica", 10), anchor="w")
chk1.pack(side="left")
prio1 = tk.Label(item1, text="Alta", fg="#D63031", bg=COLOR_CARD, font=("Helvetica", 9, "bold"))
prio1.pack(side="right", padx=10)

# Item 2
item2 = tk.Frame(list_frame, bg=COLOR_CARD, pady=8, padx=10)
item2.pack(fill="x")
chk2 = tk.Checkbutton(item2, text="Reunião com equipe", bg=COLOR_CARD, font=("Helvetica", 10), anchor="w")
chk2.pack(side="left")
prio2 = tk.Label(item2, text="Média", fg="#E17055", bg=COLOR_CARD, font=("Helvetica", 9, "bold"))
prio2.pack(side="right", padx=10)

# Item 3
item3 = tk.Frame(list_frame, bg=COLOR_CARD, pady=8, padx=10)
item3.pack(fill="x")
chk3 = tk.Checkbutton(item3, text="Enviar relatório", bg=COLOR_CARD, font=("Helvetica", 10), anchor="w")
chk3.pack(side="left")
prio3 = tk.Label(item3, text="Baixa", fg="#00B894", bg=COLOR_CARD, font=("Helvetica", 9, "bold"))
prio3.pack(side="right", padx=10)

root.mainloop()