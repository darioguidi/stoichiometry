import tkinter as tk
from tkinter import messagebox

# Funzioni di callback per ogni opzione
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
root.geometry("600x400")

# Area per i risultati
lbl_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
lbl_result.pack(pady=10)

# Opzione 1: Massa molecolare
frame_molecular_mass = tk.Frame(root)
frame_molecular_mass.pack(pady=10)

tk.Label(frame_molecular_mass, text="Opzione 1: Massa molecolare").grid(row=0, column=0, columnspan=2)
tk.Label(frame_molecular_mass, text="Numero di elementi:").grid(row=1, column=0)
entry_num_elements = tk.Entry(frame_molecular_mass)
entry_num_elements.grid(row=1, column=1)

entries_elements = []
entries_coefficients = []

def setup_molecular_mass_inputs():
    for widget in frame_molecular_mass.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.destroy()

    try:
        num_elements = int(entry_num_elements.get())
        entries_elements.clear()
        entries_coefficients.clear()

        for i in range(num_elements):
            tk.Label(frame_molecular_mass, text=f"Elemento {i+1}:").grid(row=2+i, column=0)
            entry_element = tk.Entry(frame_molecular_mass)
            entry_element.grid(row=2+i, column=1)
            entries_elements.append(entry_element)

            tk.Label(frame_molecular_mass, text=f"Coefficiente {i+1}:").grid(row=2+i, column=2)
            entry_coefficient = tk.Entry(frame_molecular_mass)
            entry_coefficient.grid(row=2+i, column=3)
            entries_coefficients.append(entry_coefficient)
    except ValueError:
        messagebox.showerror("Errore", "Inserire un numero valido!")

tk.Button(frame_molecular_mass, text="Imposta campi", command=setup_molecular_mass_inputs).grid(row=1, column=2)
tk.Button(frame_molecular_mass, text="Calcola", command=calculate_molecular_mass_gui).grid(row=1, column=3)

# Opzione 2: Numero di moli
frame_molar_mass = tk.Frame(root)
frame_molar_mass.pack(pady=10)

tk.Label(frame_molar_mass, text="Opzione 2: Numero di moli").grid(row=0, column=0, columnspan=2)
tk.Label(frame_molar_mass, text="Peso del campione (g):").grid(row=1, column=0)
entry_weight = tk.Entry(frame_molar_mass)
entry_weight.grid(row=1, column=1)

tk.Label(frame_molar_mass, text="Elemento:").grid(row=2, column=0)
entry_element = tk.Entry(frame_molar_mass)
entry_element.grid(row=2, column=1)

tk.Button(frame_molar_mass, text="Calcola", command=calculate_molar_mass_gui).grid(row=3, columnspan=2)

# Opzione 6: Composizione percentuale
frame_percentual = tk.Frame(root)
frame_percentual.pack(pady=10)

tk.Label(frame_percentual, text="Opzione 6: Composizione percentuale").grid(row=0, column=0, columnspan=2)
tk.Label(frame_percentual, text="Numero di elementi:").grid(row=1, column=0)
entry_num_elements_percentual = tk.Entry(frame_percentual)
entry_num_elements_percentual.grid(row=1, column=1)

entries_elements_percentual = []
entries_pedici_percentual = []

def setup_percentual_inputs():
    for widget in frame_percentual.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.destroy()

    try:
        num_elements = int(entry_num_elements_percentual.get())
        entries_elements_percentual.clear()
        entries_pedici_percentual.clear()

        for i in range(num_elements):
            tk.Label(frame_percentual, text=f"Elemento {i+1}:").grid(row=2+i, column=0)
            entry_element = tk.Entry(frame_percentual)
            entry_element.grid(row=2+i, column=1)
            entries_elements_percentual.append(entry_element)

            tk.Label(frame_percentual, text=f"Pedice {i+1}:").grid(row=2+i, column=2)
            entry_pedice = tk.Entry(frame_percentual)
            entry_pedice.grid(row=2+i, column=3)
            entries_pedici_percentual.append(entry_pedice)
    except ValueError:
        messagebox.showerror("Errore", "Inserire un numero valido!")

tk.Button(frame_percentual, text="Imposta campi", command=setup_percentual_inputs).grid(row=1, column=2)
tk.Button(frame_percentual, text="Calcola", command=calculate_percentual_gui).grid(row=1, column=3)

# Pulsante di uscita
tk.Button(root, text="Esci", command=root.quit, fg="red").pack(pady=10)

# Avvio dell'app
root.mainloop()
