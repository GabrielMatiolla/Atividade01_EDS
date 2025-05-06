import tkinter as tk
from tkinter import messagebox, ttk
from categoria import Categoria
from desktop import Desktop
from notebook import Notebook

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        
        self.categorias = [
            Categoria(1, "Econômico"),
            Categoria(2, "Intermediário"),
            Categoria(3, "Premium")
        ]
        
        self.criar_interface()
    
    def criar_interface(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.tipo_produto = tk.StringVar(value="Desktop")
        self.modelo = tk.StringVar()
        self.cor = tk.StringVar()
        self.preco = tk.DoubleVar()
        self.categoria = tk.StringVar()
        self.extra = tk.StringVar()
        
        ttk.Label(frame, text="Tipo de Produto:").grid(column=0, row=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Desktop", variable=self.tipo_produto, value="Desktop").grid(column=1, row=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Notebook", variable=self.tipo_produto, value="Notebook").grid(column=2, row=0, sticky=tk.W)
        
        ttk.Label(frame, text="Modelo:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.modelo).grid(column=1, row=1, columnspan=2, sticky=tk.EW, pady=5)
        
        ttk.Label(frame, text="Cor:").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.cor).grid(column=1, row=2, columnspan=2, sticky=tk.EW, pady=5)
        
        ttk.Label(frame, text="Preço:").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.preco).grid(column=1, row=3, columnspan=2, sticky=tk.EW, pady=5)
        
        ttk.Label(frame, text="Categoria:").grid(column=0, row=4, sticky=tk.W)
        categorias_nomes = [c.nome for c in self.categorias]
        ttk.Combobox(frame, textvariable=self.categoria, values=categorias_nomes).grid(column=1, row=4, columnspan=2, sticky=tk.EW, pady=5)
        
        self.extra_frame = ttk.Frame(frame)
        self.extra_frame.grid(column=0, row=5, columnspan=3, sticky=tk.EW)
        
        self.extra_label = ttk.Label(self.extra_frame, text="Potência da Fonte (Desktop):")
        self.extra_label.grid(column=0, row=0, sticky=tk.W)
        
        self.extra_entry = ttk.Entry(self.extra_frame, textvariable=self.extra)
        self.extra_entry.grid(column=1, row=0, sticky=tk.EW, pady=5)
        
        ttk.Button(frame, text="Cadastrar", command=self.cadastrar_produto).grid(column=0, row=6, columnspan=3, pady=10)
        
        frame.columnconfigure(1, weight=1)
        self.extra_frame.columnconfigure(1, weight=1)
        
        self.tipo_produto.trace_add("write", self.atualizar_extra_field)
    
    def atualizar_extra_field(self, *args):
        tipo = self.tipo_produto.get()
        
        if tipo == "Desktop":
            self.extra_label.config(text="Potência da Fonte (Desktop):")
        else:
            self.extra_label.config(text="Tempo de Bateria (Notebook):")
    
    def cadastrar_produto(self):
        try:
            categoria_nome = self.categoria.get()
            categoria = next((c for c in self.categorias if c.nome == categoria_nome), None)
            
            if not categoria:
                raise ValueError("Selecione uma categoria válida")
            
            if self.tipo_produto.get() == "Desktop":
                produto = Desktop(
                    modelo=self.modelo.get(),
                    cor=self.cor.get(),
                    preco=self.preco.get(),
                    categoria=categoria,
                    potenciaDaFonte=int(self.extra.get())
                )
            else:
                produto = Notebook(
                    modelo=self.modelo.get(),
                    cor=self.cor.get(),
                    preco=self.preco.get(),
                    categoria=categoria,
                    tempoDeBateria=int(self.extra.get())
                )
            
            produto.cadastrar()
            
            info = produto.getInformacoes()
            messagebox.showinfo("Sucesso", f"Produto cadastrado com sucesso!\n\n{info}")
            
            self.modelo.set("")
            self.cor.set("")
            self.preco.set(0.0)
            self.categoria.set("")
            self.extra.set("")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o produto:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()