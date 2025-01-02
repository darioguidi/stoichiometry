from snippets.fileManagement import read_file_chemical_element
from snippets.fileManagement import read_file_element_symbols
from utils.generateChemicalFormula import generateSymbol


# Calcolo della massa molare dato peso e nome del elemento, infine calcolo numero di moli
def calculate_molar_mass(sample_weight, chemical_element):
    if len(chemical_element)<2:
        chemical_element=generateSymbol(chemical_element)
        
    molarMass=read_file_chemical_element(chemical_element)
    nmoli=sample_weight/molarMass*100
    return nmoli