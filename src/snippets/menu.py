def menu():
    while True:
        # Mostra il menu
        print("\nMenu delle Funzioni:")
        print("1. Funzione 1")
        print("2. Funzione 2")
        print("3. Funzione 3")
        print("4. Uscita")
        
        # Prendi la scelta dell'utente
        scelta = input("Scegli un'opzione (1-4): ")

        # Gestisci le scelte dell'utente
        if scelta == "1":
            print("Hai scelto la funzione 1!")
        elif scelta == "2":
            print("Hai scelto la funzione 2!")
        elif scelta == "3":
            print("Hai scelto la funzione 3!")
        elif scelta == "4":
            print("Uscita dal programma...")
            break  # Esci dal ciclo while e termina il programma
        else:
            print("Opzione non valida, riprova!")