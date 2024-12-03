import tkinter as tk
from tkinter import messagebox
import random
import time

class TreinadorMatematica:
    def verificar_resposta(self):
        try:
            resposta = float(self.entrada.get())
            if resposta == self.resposta_correta:
                self.acertos += 1
            else:
                messagebox.showerror("Incorreto", f"A resposta correta era {self.resposta_correta:.2f}")
            
            self.total += 1
            self.label_pontuacao.config(text=f"Acertos: {self.acertos} | Total: {self.total}")
            self.gerar_nova_conta()

        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido")
            self.entrada.delete(0, tk.END)

    def esconder_conta(self):
        self.label_conta.config(text="")
        self.timer = None

    def mostrar_conta(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        
        self.label_conta.config(text=self.conta_atual)
        self.timer = self.root.after(5000, self.esconder_conta)

    def gerar_divisao_valida(self):
        while True:
            divisor = random.randint(2, 20)
            resultado_desejado = random.randint(1, 100) / 4
            dividendo = int(resultado_desejado * divisor)
            
            resultado_real = dividendo / divisor
            resultado_str = f"{resultado_real:.2f}"
            if float(resultado_str) == resultado_real:
                return dividendo, divisor, resultado_real

    def gerar_nova_conta(self):
        if not self.tempo_inicio:
            self.tempo_inicio = time.time()

        if self.dificuldade == "fácil":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            operador = random.choice(['+', '-'])
            
            if operador == '+':
                self.resposta_correta = a + b
            else:
                self.resposta_correta = a - b
            
            self.conta_atual = f"{a} {operador} {b} = ?"

        else:  # difícil
            operador = random.choice(['+', '-', 'x', '÷'])
            if operador == '÷':
                a, b, self.resposta_correta = self.gerar_divisao_valida()
            elif operador != 'x':
                a = random.randint(2, 5000)
                b = random.randint(2, 5000)
            else:
                a = random.randint(2, 99)
                b = random.randint(2, 50)
            
            if operador == '+':
                self.resposta_correta = a + b
            elif operador == '-':
                self.resposta_correta = a - b
            elif operador == 'x':
                self.resposta_correta = a * b
            
            self.conta_atual = f"{a} {operador} {b} = ?"

        self.mostrar_conta()
        self.entrada.delete(0, tk.END)
        self.entrada.focus()

    def mudar_dificuldade(self):
        if self.dificuldade == "fácil":
            self.dificuldade = "difícil"
            messagebox.showinfo("Dificuldade", "Modo difícil ativado!\nAgora inclui multiplicação, divisão e números maiores!")
        else:
            self.dificuldade = "fácil"
            messagebox.showinfo("Dificuldade", "Modo fácil ativado!\nApenas soma e subtração com números menores.")
        
        self.gerar_nova_conta()

    def __init__(self, root):
        self.root = root
        self.root.title("Treinador de Cálculo Mental")
        self.root.geometry("400x400")

        # Configurando cores do tema escuro
        self.bg_color = "#1e1e1e"  # Cor de fundo escura
        self.text_color = "#ffffff"  # Texto branco
        self.button_bg = "#333333"  # Fundo do botão escuro
        self.button_fg = "#ffffff"  # Texto do botão branco
        self.entry_bg = "#2d2d2d"  # Fundo da entrada um pouco mais claro
        self.entry_fg = "#ffffff"  # Texto da entrada branco

        # Configurando a cor de fundo da janela principal
        self.root.configure(bg=self.bg_color)

        # Variáveis para controlar o jogo
        self.acertos = 0
        self.total = 0
        self.tempo_inicio = None
        self.timer = None
        self.conta_atual = ""

        # Frame principal
        self.frame = tk.Frame(self.root, padx=20, pady=20, bg=self.bg_color)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Label para mostrar a conta
        self.label_conta = tk.Label(
            self.frame,
            text="",
            font=("Arial", 24),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.label_conta.pack(pady=20)

        # Botão para mostrar a conta novamente
        self.botao_mostrar = tk.Button(
            self.frame,
            text="Mostrar Conta (5s)",
            command=self.mostrar_conta,
            bg=self.button_bg,
            fg=self.button_fg,
            relief="flat",
            padx=10,
            pady=5
        )
        self.botao_mostrar.pack(pady=5)

        # Campo para resposta
        self.entrada = tk.Entry(
            self.frame,
            font=("Arial", 18),
            justify='center',
            bg=self.entry_bg,
            fg=self.entry_fg,
            insertbackground=self.text_color  # Cor do cursor
        )
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', lambda e: self.verificar_resposta())

        # Botão verificar
        self.botao_verificar = tk.Button(
            self.frame,
            text="Verificar (Enter)",
            command=self.verificar_resposta,
            bg=self.button_bg,
            fg=self.button_fg,
            relief="flat",
            padx=10,
            pady=5
        )
        self.botao_verificar.pack(pady=10)

        # Label para pontuação
        self.label_pontuacao = tk.Label(
            self.frame,
            text="Acertos: 0 | Total: 0",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.label_pontuacao.pack(pady=10)

        # Configurações iniciais
        self.dificuldade = "difícil"
        self.resposta_correta = None
        self.gerar_nova_conta()

def main():
    root = tk.Tk()
    app = TreinadorMatematica(root)
    root.mainloop()

if __name__ == "__main__":
    main()