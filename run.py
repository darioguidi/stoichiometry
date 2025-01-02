"""import sys
import os

project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

from snippets.application import application

def main():
    application()
    
if __name__=="__main__":
    main() """

import sys
import os

# Aggiungi il percorso al modulo principale
project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

# Importa il modulo per l'interfaccia grafica
from src import tkinter as gui_main

def main():
    # Avvia l'interfaccia grafica
    gui_main()

if __name__ == "__main__":
    main()
