from csv import reader, writer

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

def read_file_element_symbols(element_name):
    atomic_masses = None  
    FILENAME="data/element_symbols.txt"

    with open(FILENAME, "r") as infile:
        csvReader = reader(infile)
        for row in csvReader:
            row = row[0].split(":")  
            if row[0].strip() == element_name:  
                atomic_masses = float(row[1].strip()) 
                break  
    return atomic_masses