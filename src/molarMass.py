import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from snippets.fileManagement import read_file_chemical_element


# Calcolo della massa molare dato peso e nome del elemento, infine calcolo numero di moli
def calculate_molar_mass(sample_weight, chemical_element):
    FILENAME="data/chemical_element.txt"
    molarMass=read_file_chemical_element(FILENAME,chemical_element)

    nmoli=sample_weight/molarMass*100

    return nmoli