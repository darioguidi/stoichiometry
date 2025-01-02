from snippets.fileManagement import read_file_atomic_masses
from utils.generateChemicalFormula import generateElementName

# Calcola il numero di moli dato peso e nome simbolico dell'elemento
def calculate_molar_mass(sample_weight, chemical_element):
    if len(chemical_element) < 3:  # Se è un simbolo (e.g., "Cu")
        chemical_element = generateElementName(chemical_element)  # Converte simbolo in nome (e.g., "Cu" -> "Copper")
    
    # A questo punto chemical_element è sicuramente il nome (e.g., "Copper")
    molarMass = read_file_atomic_masses(chemical_element)

    if molarMass is None:
        raise ValueError(f"Molar mass for element '{chemical_element}' not found.")

    # Calcola il numero di moli
    nmoli = sample_weight / float(molarMass)  # Moli = peso / massa molare
    return nmoli

