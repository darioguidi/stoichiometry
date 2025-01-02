import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Per un layout migliorato con stili

from calculation.molecularMass import calculate_molecular_mass
from calculation.molarMass import calculate_molar_mass
from calculation.moliNumber import calculate_moli_number
from calculation.chemicalComposition import calculate_chemical_composition, calculate_sperimental_chemical_composition
from calculation.percentualComposition import calculate_percentual_composition


def calculate_molecular_mass_gui():
    try:
        num_elements = int(entry_num_elements.get())
        elements = []
        coefficients = []

        for i in range(num_elements):
            elements.append(entries_elements[i].get())
            coefficients.append(float(entries_coefficients[i].get()))

        result = calculate_molecular_mass(coefficients, elements)
        lbl_result["text"] = f"Massa molecolare: {result}"
    except Exception as e:
        messagebox.showerror("Errore", f"Errore inaspettato: {e}")

def calculate_molar_mass_gui():
    try:
        weight = float(entry_weight.get())
        element = entry_element.get()
        result = calculate_molar_mass(weight, element)
        lbl_result["text"] = f"Numero di moli: {result}"
    except Exception as e:
        messagebox.showerror("Errore", f"Errore inaspettato: {e}")

def calculate_percentual_gui():
    try:
        num_elements = int(entry_num_elements_percentual.get())
        elements = []
        pedici = []

        for i in range(num_elements):
            elements.append(entries_elements_percentual[i].get())
            pedici.append(int(entries_pedici_percentual[i].get()))

        result = calculate_percentual_composition(pedici, elements)
        lbl_result["text"] = "\n".join([f"{elements[i]}: {res:.2f}%" for i, res in enumerate(result)])
    except Exception as e:
        messagebox.showerror("Errore", f"Errore inaspettato: {e}")

# Layout principale
root = tk.Tk()
root.title("Calcolatore Chimico")
root.geometry("700x600")
root.resizable(False, False)

# Stile migliorato
style = ttk.Style()
style.configure("TFrame", padding=10)
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10))
style.configure("Header.TLabel", font=("Arial", 18, "bold"), foreground="darkblue")

# Intestazione
header = ttk.Label(root, text="Calcolatore Chimico", style="Header.TLabel")
header.pack(pady=10)

# Area per i risultati
lbl_result = ttk.Label(root, text="", font=("Arial", 12), foreground="blue")
lbl_result.pack(pady=10)

# Notebook per organizzare le opzioni in schede
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Scheda 1: Massa molecolare
frame_molecular_mass = ttk.Frame(notebook)
notebook.add(frame_molecular_mass, text="Massa Molecolare")

ttk.Label(frame_molecular_mass, text="Numero di elementi:").grid(row=0, column=0, sticky="w")
entry_num_elements = ttk.Entry(frame_molecular_mass)
entry_num_elements.grid(row=0, column=1)

entries_elements = []
entries_coefficients = []

def setup_molecular_mass_inputs():
    for widget in frame_molecular_mass.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.destroy()

    ttk.Label(frame_molecular_mass, text="Numero di elementi:").grid(row=0, column=0, sticky="w")
    entry_num_elements.grid(row=0, column=1)
    ttk.Button(frame_molecular_mass, text="Imposta campi", command=setup_molecular_mass_inputs).grid(row=0, column=2)
    ttk.Button(frame_molecular_mass, text="Calcola", command=calculate_molecular_mass_gui).grid(row=0, column=3)

    try:
        num_elements = int(entry_num_elements.get())
        entries_elements.clear()
        entries_coefficients.clear()

        for i in range(num_elements):
            ttk.Label(frame_molecular_mass, text=f"Elemento {i + 1}:").grid(row=1 + i, column=0, sticky="w")
            entry_element = ttk.Entry(frame_molecular_mass)
            entry_element.grid(row=1 + i, column=1)
            entries_elements.append(entry_element)

            ttk.Label(frame_molecular_mass, text=f"Coefficiente {i + 1}:").grid(row=1 + i, column=2, sticky="w")
            entry_coefficient = ttk.Entry(frame_molecular_mass)
            entry_coefficient.grid(row=1 + i, column=3)
            entries_coefficients.append(entry_coefficient)
    except ValueError:
        messagebox.showerror("Errore", "Inserire un numero valido!")

setup_molecular_mass_inputs()

# Scheda 2: Numero di moli
frame_molar_mass = ttk.Frame(notebook)
notebook.add(frame_molar_mass, text="Numero di Moli")

ttk.Label(frame_molar_mass, text="Peso del campione (g):").grid(row=0, column=0, sticky="w")
entry_weight = ttk.Entry(frame_molar_mass)
entry_weight.grid(row=0, column=1)

ttk.Label(frame_molar_mass, text="Elemento:").grid(row=1, column=0, sticky="w")
entry_element = ttk.Entry(frame_molar_mass)
entry_element.grid(row=1, column=1)

ttk.Button(frame_molar_mass, text="Calcola", command=calculate_molar_mass_gui).grid(row=2, columnspan=2)

# Scheda 3: Composizione Percentuale
frame_percentual = ttk.Frame(notebook)
notebook.add(frame_percentual, text="Composizione Percentuale")

ttk.Label(frame_percentual, text="Numero di elementi:").grid(row=0, column=0, sticky="w")
entry_num_elements_percentual = ttk.Entry(frame_percentual)
entry_num_elements_percentual.grid(row=0, column=1)

entries_elements_percentual = []
entries_pedici_percentual = []

def setup_percentual_inputs():
    for widget in frame_percentual.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.destroy()

    ttk.Label(frame_percentual, text="Numero di elementi:").grid(row=0, column=0, sticky="w")
    entry_num_elements_percentual.grid(row=0, column=1)
    ttk.Button(frame_percentual, text="Imposta campi", command=setup_percentual_inputs).grid(row=0, column=2)
    ttk.Button(frame_percentual, text="Calcola", command=calculate_percentual_gui).grid(row=0, column=3)

    try:
        num_elements = int(entry_num_elements_percentual.get())
        entries_elements_percentual.clear()
        entries_pedici_percentual.clear()

        for i in range(num_elements):
            ttk.Label(frame_percentual, text=f"Elemento {i + 1}:").grid(row=1 + i, column=0, sticky="w")
            entry_element = ttk.Entry(frame_percentual)
            entry_element.grid(row=1 + i, column=1)
            entries_elements_percentual.append(entry_element)

            ttk.Label(frame_percentual, text=f"Pedice {i + 1}:").grid(row=1 + i, column=2, sticky="w")
            entry_pedice = ttk.Entry(frame_percentual)
            entry_pedice.grid(row=1 + i, column=3)
            entries_pedici_percentual.append(entry_pedice)
    except ValueError:
        messagebox.showerror("Errore", "Inserire un numero valido!")

setup_percentual_inputs()

# Pulsante di uscita
ttk.Button(root, text="Esci", command=root.quit).pack(pady=10)

# Avvio dell'app
root.mainloop()
