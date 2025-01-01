# Calcolo della massa molecolare dati i pesi atomici e i suoi pedici
def molecular_mass_calculation(stoichiometric_coefficients,atomic_masses):
    """
    I coefficienti stechiometrici e i pesi atomici devono coincidere 
    nelle varie liste come posizione ed ordine quindi
    """
    Pa=0
    Pm=0
    for i in range(len(atomic_masses)):
        Pa=stoichiometric_coefficients[i]*atomic_masses[i]
        Pm+=Pa
    return Pm