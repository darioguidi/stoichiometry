from snippets.fileManagement import read_file_element_symbols, read_file_element_symbols_reversed, read_file_atomic_masses

# Restituisce il simbolo di un elemento
def generateSymbol(chemical_element):
    try:
        symbol = read_file_element_symbols(chemical_element)
        if symbol is None:
            raise ValueError(f"Symbol for element '{chemical_element}' not found.")
        return symbol
    except Exception as e:
        raise ValueError(f"Error generating symbol for element '{chemical_element}': {str(e)}")

# Restituisce il nome di un elemento
def generateElementName(chemical_symbol):
    try:
        name = read_file_element_symbols_reversed(chemical_symbol)
        if name is None:
            raise ValueError(f"Name for symbol '{chemical_symbol}' not found.")
        return name
    except Exception as e:
        raise ValueError(f"Error generating name for symbol '{chemical_symbol}': {str(e)}")

def calculate_molecular_mass_formula(stoichiometric_coefficients, chemical_element):
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

    return f"Massa molecolare: {Pm} e formula molecolare: {formula}"