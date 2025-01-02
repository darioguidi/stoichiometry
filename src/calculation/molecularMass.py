from snippets.fileManagement import read_file_atomic_masses
from utils.generateChemicalFormula import generateSymbol

# Calcolo della massa molecolare dati i pesi atomici e i suoi pedici
def calculate_molecular_mass(stoichiometric_coefficients, chemical_element):
    """
    I coefficienti stechiometrici e i pesi atomici devono coincidere 
    nelle varie liste come posizione ed ordine quindi
    """

    Pa = 0
    Pm = 0
    FILENAME = "data/chemical_element.txt"

    atomic_masses = []
    formula = ""  

    # Loop to get atomic masses and generate formula
    for i in range(len(chemical_element)):
        atomic_masses.append(read_file_atomic_masses(chemical_element[i]))
        formula+=generateSymbol(chemical_element[i])+str(int(stoichiometric_coefficients[i]))

    # Calculate molecular mass
    for i in range(len(atomic_masses)):
        Pa = stoichiometric_coefficients[i] * atomic_masses[i]
        Pm += Pa

    return Pm
