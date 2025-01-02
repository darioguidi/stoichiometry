from csv import reader, writer

def read_file_chemical_element(filename, element_name):
    atomic_masses = None  

    with open(filename, "r") as infile:
        csvReader = reader(infile)
        for row in csvReader:
            row = row[0].split(":")  
            if row[0].strip() == element_name:  
                atomic_masses = float(row[1].strip()) 
                break  
    return atomic_masses