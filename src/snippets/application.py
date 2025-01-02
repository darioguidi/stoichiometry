from calculation.molecularMass import calculate_molecular_mass
from calculation.molarMass import calculate_molar_mass
from calculation.moliNumber import calculate_moli_number
from calculation.chemicalComposition import calculate_chemical_composition, calculate_sperimental_chemical_composition
from calculation.percentualComposition import calculate_percentual_composition

def application():
    while True:
        print("\nMenu delle Funzioni:")
        print("1. Calcola massa molecolare")
        print("2. Calcola numero di moli")
        print("3. Calcolo numero di moli di un elemento, dato il peso in g, e la massa molare del composto")
        print("4. Data la composizione in percentuale di un composto, determinare la formula minima")
        print("5. Data la composizione in percentuale di un composto, determinare la formula minima, riferendoci ad un precedente calcolo sperimentale")
        print("6. Calcolo composizione percentuale data formula minima")
        print("7. Uscita")
        
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

                if result is not None:
                    print(f"La massa molecolare è: {result}")
                else:
                    print("Errore: la massa molecolare non è stata calcolata correttamente.")
            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(f"Errore inaspettato: {e}")

        elif scelta == "2":
            try:
                moli = 0
                sample_weight = input("Inserisci il peso del campione (in grammi):\n")

                # Gestisci il separatore decimale in caso di virgola
                sample_weight = sample_weight.replace(",", ".")
                
                # Prova a convertire il valore in float
                sample_weight = float(sample_weight)
                
                chemical_element = input("Inserisci il nome dell'elemento chimico:\n")

                # Chiamata alla funzione per calcolare il numero di moli
                moli = calculate_molar_mass(sample_weight, chemical_element)
                
                if moli is not None:
                    print(f"Il numero di moli è: {moli} x 10^-2")
                else:
                    print("Errore: non è stato possibile calcolare il numero di moli.")
            except ValueError:
                print("Errore: inserire un valore numerico valido per il peso del campione!")
            except Exception as e:
                print(f"Errore inaspettato: {e}")

        elif scelta == "3":
            try:
                element=input("Di che elemento si tratta?\n")
                weight=float(input("Quanto è la sua quantità in g?\n"))
                compost=input("Di che composto fa parte?\n")
                molar_mass=float(input("Ultima domanda, a quanto corissponde la massa molare in g/mol?\n"))

                nmoli=calculate_moli_number(element, weight, compost, molar_mass)
                print(nmoli)
            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(f"Errore inaspettato: {e}")

        elif scelta=="4":
            try:
                elements=[]
                compositions=[]
                inputUtente=int(input("Da quanti elementi è composto il tuo composto?\n"))
                for i in range(inputUtente):
                    inputElement=input("Inserisci elemento\n")
                    elements.append(inputElement)
                    inputComposition=float(input("Inserisci composizione in percentuale del elemento\n"))
                    compositions.append(inputComposition)
                formula=calculate_chemical_composition(elements, compositions)
                print(formula)
            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(e)
        elif scelta=="5":
            try:
                elements=[]
                compositions=[]
                inputUtente=int(input("Da quanti elementi è composto il tuo composto?\n"))
                for i in range(inputUtente):
                    inputElement=input("Inserisci elemento\n")
                    elements.append(inputElement)
                    inputComposition=float(input("Inserisci composizione in percentuale del elemento\n"))
                    compositions.append(inputComposition)
                sperimentale=float(input("A quanto corrisponde il calcolo sperimentale del Pm?\n"))
                formula=calculate_sperimental_chemical_composition(elements, compositions, sperimentale)
                print(formula)
            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(e)

        elif scelta=="6":
            try:
                elements = []
                pedici = []
                inputUtente = int(input("Da quanti elementi è composto il tuo composto?\n"))

                for i in range(inputUtente):
                    inputElement = input("Inserisci elemento\n")
                    elements.append(inputElement)
                    inputPedice = int(input("Inserisci pedice\n"))  # Deve essere un intero
                    pedici.append(inputPedice)

                perc = calculate_percentual_composition(pedici, elements)

                for i, value in enumerate(perc):
                    print(f"L'elemento {elements[i]} ha una composizione percentuale di {value:.2f}%")

            except ValueError:
                print("Errore: inserire un valore numerico valido!")
            except Exception as e:
                print(f"Errore inatteso: {e}")

        elif scelta == "7":
            confirm_exit = input("Sei sicuro di voler uscire? (S/N): ").strip().upper()
            if confirm_exit == "S":
                print("Uscita dal programma...")
                break 
            else:
                print("Ritorno al menu principale...")

        else:
            print("Opzione non valida, riprova!")

