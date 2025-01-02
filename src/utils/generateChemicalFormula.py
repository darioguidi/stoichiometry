from snippets.fileManagement import read_file_element_symbols, read_file_element_symbols_reversed

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
