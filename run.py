import sys
import os

# Percorso assoluto della directory "src"
project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

from calculation.molecularMass import calculate_molecular_mass
from calculation.molarMass import calculate_molar_mass
from snippets.application import application

def main():
    coef=[2,1,4]
    pa=["Sodio", "Zolfo", "Ossigeno"]
    print(calculate_molecular_mass(coef,pa))

    element_name="Rame"
    peso=1 #g
    print(calculate_molar_mass(peso,element_name))

    application()
    

if __name__=="__main__":
    main()