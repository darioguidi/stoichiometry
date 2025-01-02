from csv import reader, DictReader


# Funzione che legge il file e restituisce i Pesi Atomici (Pa)
def read_file_atomic_masses(element_name):
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


def read_file_element_symbols_reversed(symbol):
    name = None  
    FILENAME = "data/element_symbol_reversed.txt"

    try:
        with open(FILENAME, "r") as infile:
            csvReader = reader(infile)
            for row in csvReader:
                row = row[0].split(":")  
                if len(row) == 2 and row[0].strip() == symbol:  
                    name = row[1].strip()
                    break
    except FileNotFoundError:
        print(f"File {FILENAME} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return name


