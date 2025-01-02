from snippets.fileManagement import read_file_element_symbols, read_file_element_symbols_reversed


# Restituisce il simbolo di un elemento
def generateSymbol(chemical_element):
    symbols=read_file_element_symbols(chemical_element)
    return symbols 

# Restituisce il nome di un elemento
def generateElementName(chemical_symbol):
    name=read_file_element_symbols_reversed(chemical_symbol)
    return name 
