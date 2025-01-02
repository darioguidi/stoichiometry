from csv import reader, DictReader


# Funzione che legge il file e restituisce i Pesi Atomici (Pa)
def read_file_chemical_element(element_name):
    atomic_masses = None  
    FILENAME = "data/chemical_element.txt"

    try:
        with open(FILENAME, "r") as infile:
            csvReader = reader(infile)
            for row in csvReader:
                row = row[0].split(":")  
                if len(row) == 2 and row[0].strip() == element_name:  
                    atomic_masses = float(row[1].strip()) 
                    break
    except FileNotFoundError:
        print(f"File {FILENAME} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return atomic_masses


# Funzione che legge il file e restituisce il simbolo 
def read_file_element_symbols(element_name):
    symbols = None  
    FILENAME = "data/element_symbols.txt"

    try:
        with open(FILENAME, "r") as infile:
            csvReader = reader(infile)
            for row in csvReader:
                row = row[0].split(":")  
                if len(row) == 2 and row[0].strip() == element_name:  
                    symbols = row[1].strip()
                    break
    except FileNotFoundError:
        print(f"File {FILENAME} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return symbols


def read_file_element_symbols_reversed(chemical_symbol):
    # File containing element data
    FILENAME = "data/element_symbols.txt"
    
    try:
        with open(FILENAME, "r") as infile:
            csvReader = reader(infile)
            for row in csvReader:
                row = row[0].split(":")  # Split by colon
                if len(row) == 2:  # Ensure the row contains the expected format
                    name, symbol = row[0].strip(), row[1].strip()  # Name and symbol are split
                    if symbol == chemical_symbol:  # If the symbol matches, return the name
                        return name
    except FileNotFoundError:
        print(f"File {FILENAME} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # If the symbol is not found, return an appropriate message
    return "Unknown Element"
