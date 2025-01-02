from calculation.molecularMass import calculate_molecular_mass
from calculation.molarMass import calculate_molar_mass

def application():
    while True:
        print("\nMenu delle Funzioni:")
        print("1. Calcola massa molecolare")
        print("2. Funzione 2")
        print("3. Funzione 3")
        print("4. Uscita")
        
        # Prendi la scelta dell'utente
        scelta = input("Scegli un'opzione (1-4):\n")

        # Gestisci le scelte dell'utente
        if scelta == "1":
            try:
                inputUtentenumeroCoef = int(input("Quanti coefficienti ha la tua formula molecolare?\n"))
                coef = []
                elements = []
                
                for i in range(inputUtentenumeroCoef):
                    inputUtenteCoef = float(input(f"Inserire coefficiente {i + 1}:\n"))
                    inputUtenteNomeElemento = input(f"Inserire nome elemento {i + 1}:\n")
                    coef.append(inputUtenteCoef)
                    elements.append(inputUtenteNomeElemento)
                
                result = calculate_molecular_mass(coef, elements)

                print(f"La massa molecolare è: {result}")
            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(f"Errore inaspettato: {e}")

        elif scelta == "2":
            try:
                moli=0
                sample_weight = float(input("Inserisci il peso del campione (in grammi):\n"))
                chemical_element = input("Inserisci il nome dell'elemento chimico:\n")

                if len(chemical_element)<2:
                    chemical_element=
                
                # Chiamata alla funzione per calcolare il numero di moli
                moli = calculate_molar_mass(sample_weight, chemical_element)
                
                print(f"Il numero di moli è: {moli} x 10^-2")
            except ValueError:
                print("Errore: inserire un valore numerico valido per il peso del campione!")
            except Exception as e:
                print(f"Errore inaspettato: {e}")

        elif scelta == "3":
            print("Hai scelto la funzione 3!")
        elif scelta == "4":
            print("Uscita dal programma...")
            break  # Esci dal ciclo while e termina il programma
        else:
            print("Opzione non valida, riprova!")
