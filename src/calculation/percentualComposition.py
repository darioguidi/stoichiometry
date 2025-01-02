from calculation.molecularMass import calculate_molecular_mass

def calculate_percentual_composition(pedici, elements):
    Pa = []
    percentual = []
    Pm = 0  # Inizializzazione della massa molecolare totale

    # Calcolo della massa atomica per ogni elemento
    for i in range(len(elements)):
        massa = calculate_molecular_mass(pedici[i], elements[i])
        Pa.append(massa)
        Pm += massa  # Somma alla massa totale

    # Calcolo della percentuale per ogni elemento
    for value in Pa:
        percentual.append(float((value * 100) / Pm))
    return percentual