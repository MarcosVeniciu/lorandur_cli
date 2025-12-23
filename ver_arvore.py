import os
from pathlib import Path

def print_tree(directory, prefix=""):
    """
    Imprime a árvore de diretórios de forma recursiva e visual.
    """
    path_obj = Path(directory)
    
    # Lista o conteúdo e ordena (pastas e arquivos misturados)
    try:
        contents = list(path_obj.iterdir())
    except PermissionError:
        print(f"{prefix}[Acesso Negado]")
        return

    # Filtra pastas que não queremos ver (poluição visual)
    ignore_list = ['.git', '__pycache__', '.vscode', '.idea', 'venv', 'env']
    contents = [c for c in contents if c.name not in ignore_list]
    
    # Ordena: Pastas primeiro, depois arquivos, ambos alfabeticamente
    contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

    # Contadores para desenhar as linhas corretamente
    count = len(contents)
    
    for index, item in enumerate(contents):
        is_last = (index == count - 1)
        
        # Escolhe o conector gráfico
        connector = "└── " if is_last else "├── "
        
        # Imprime o item atual
        print(f"{prefix}{connector}{item.name}")
        
        # Se for diretório, entra nele (Recursão)
        if item.is_dir():
            # Define o prefixo para os filhos (se este item é o último, o prefixo é vazio, senão é uma barra)
            extension = "    " if is_last else "│   "
            print_tree(item, prefix + extension)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"\n📂 Raiz do Projeto: {current_dir}\n")
    print(".")
    print_tree(current_dir)
    print("\n")