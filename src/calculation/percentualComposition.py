from calculation.molecularMass import calculate_molecular_mass
from snippets.fileManagement import read_file_atomic_masses

def calculate_percentual_composition(pedici, elements):
    Pa = []
    percentual = []
    Pm = calculate_molecular_mass(pedici,elements)

    for i in range(len(elements)):
        Pa.append(float(read_file_atomic_masses(elements[i])))

    # Calcolo della percentuale per ogni elemento
    for value in Pa:
        percentual.append(float((value * 100) / Pm))
    return percentual