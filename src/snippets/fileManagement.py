from csv import reader, writer


# Funzione che legge il file e restituisce i Pesi Atomici (Pa)
def read_file_chemical_element(element_name):
    atomic_masses = None  
    FILENAME="data/chemical_element.txt"

    with open(FILENAME, "r") as infile:
        csvReader = reader(infile)
        for row in csvReader:
            row = row[0].split(":")  
            if row[0].strip() == element_name:  
                atomic_masses = float(row[1].strip()) 
                break  
    return atomic_masses

# Funzione che legge il file e restituisce il simbolo 
def read_file_element_symbols(element_name):
    symbols = None  
    FILENAME="data/element_symbols.txt"

    with open(FILENAME, "r") as infile:
        csvReader = reader(infile)
        for row in csvReader:
            row = row[0].split(":")  
            if row[0].strip() == element_name:  
                symbols = row[1].strip()
                break  
    return symbols

# Funzione che legge il file e restituisce il nome
def read_file_element_symbols_reversed(chemical_symbol):
    atomic_masses = None  
    FILENAME="data/element_symbols.txt"

    with open(FILENAME, "r") as infile:
        csvReader = reader(infile)
        for row in csvReader:
            row = row[0].split(":")  
            if row[1].strip() == chemical_symbol:  
                name = float(row[0].strip()) 
                break  
    return name