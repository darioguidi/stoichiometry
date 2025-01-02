from snippets.fileManagement import read_file_atomic_masses, read_file_element_symbols
from calculation.molecularMass import calculate_molecular_mass


def calculate_chemical_composition(elements, compositions):
    moli = []
    molar_mass = []
    pedici = []

    # Check if the lengths of elements and compositions match
    if len(elements) == len(compositions):
        for i in range(len(elements)):
            mass = read_file_atomic_masses(elements[i])
            if mass is None:
                return f"Error: Atomic mass for element {elements[i]} not found."
            molar_mass.append(mass)
            moli.append(compositions[i] / mass)

        # Find the minimum amount of moles
        min_moli = min(moli)

        # Calculate the ratio for each element and append it to pedici
        for mole in moli:
            pedici.append(mole / min_moli)

        # Check if any pedici contain decimals that need adjustment
        # Find the maximum decimal part
        decimals = [p - int(p) for p in pedici]
        max_decimal = max(decimals)

        # If any decimal part is non-zero, multiply the pedici to round them
        if max_decimal > 0:
            # Find the smallest multiplier to make all values integers
            multiplier = 1
            if max_decimal >= 0.9:
                multiplier = 10  # Multiply by 10 if decimals are too large
            elif max_decimal >= 0.5:
                multiplier = 2  # Multiply by 2 for decimals like 0.5, 0.6, etc.
            elif max_decimal >= 0.33:
                multiplier = 3  # Multiply by 3 for decimals like 0.3333
            
            # Multiply all pedici by the multiplier
            pedici = [round(p * multiplier) for p in pedici]

        # Generate the empirical formula
        formula = ""
        for i in range(len(elements)):
            formula += f"{read_file_element_symbols(elements[i])}{pedici[i]}"

        return f"La formula minima è {formula}"
    else:
        return "Errore: il numero di elementi deve corrispondere al numero di composizioni"

def calculate_sperimental_chemical_composition(elements, compositions, sperimental):
    moli = []
    molar_mass = []
    pedici = []

    # Check if the lengths of elements and compositions match
    if len(elements) == len(compositions):
        for i in range(len(elements)):
            mass = read_file_atomic_masses(elements[i])
            if mass is None:
                return f"Error: Atomic mass for element {elements[i]} not found."
            molar_mass.append(mass)
            moli.append(compositions[i] / mass)

        # Find the minimum amount of moles
        min_moli = min(moli)

        # Calculate the ratio for each element and append it to pedici
        for mole in moli:
            pedici.append(mole / min_moli)

        # Check if any pedici contain decimals that need adjustment
        # Find the maximum decimal part
        decimals = [p - int(p) for p in pedici]
        max_decimal = max(decimals)

        # If any decimal part is non-zero, multiply the pedici to round them
        if max_decimal > 0:
            # Find the smallest multiplier to make all values integers
            multiplier = 1
            if max_decimal >= 0.9:
                multiplier = 10  # Multiply by 10 if decimals are too large
            elif max_decimal >= 0.5:
                multiplier = 2  # Multiply by 2 for decimals like 0.5, 0.6, etc.
            elif max_decimal >= 0.33:
                multiplier = 3  # Multiply by 3 for decimals like 0.3333
            
            # Multiply all pedici by the multiplier
            pedici = [round(p * multiplier) for p in pedici]

        pm=calculate_molecular_mass(pedici, elements)

        moltiplicatore=sperimental/pm

        # Generate the molecular formula by rounding the final pedici
        formula = ""
        for i in range(len(elements)):
            final_pedice = round(pedici[i] * moltiplicatore)  # Round the final subscripts
            formula += f"{read_file_element_symbols(elements[i])}{final_pedice}"
            
        return f"La formula minima è {formula}"
    else:
        return "Errore: il numero di elementi deve corrispondere al numero di composizioni"
