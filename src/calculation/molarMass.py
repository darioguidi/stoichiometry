from src.snippets.fileManagement import read_file_chemical_element


# Calcolo della massa molare dato peso e nome del elemento, infine calcolo numero di moli
def calculate_molar_mass(sample_weight, chemical_element):
    molarMass=read_file_chemical_element(chemical_element)

    nmoli=sample_weight/molarMass*100

    return nmoli