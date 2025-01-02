from snippets.fileManagement import read_file_chemical_element
from utils.generateChemicalFormula import generateFormula

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
    formula = ""  # Fixed typo here

    # Loop to get atomic masses and generate formula
    for i in range(len(chemical_element)):
        atomic_masses.append(read_file_chemical_element(chemical_element[i]))
        formula+=generateFormula(chemical_element[i])+str(int(stoichiometric_coefficients[i]))  # Include stoichiometric coefficients if needed

    # Calculate molecular mass
    for i in range(len(atomic_masses)):
        Pa = stoichiometric_coefficients[i] * atomic_masses[i]
        Pm += Pa

    return f"Massa molecolare: {Pm} e formula molecolare: {formula}"
