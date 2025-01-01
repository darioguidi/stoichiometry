from src.molecularMass import calculate_molecular_mass
from src.molarMass import calculate_molar_mass

def main():
    coef=[2,1,4]
    pa=[23,32,16]
    print(calculate_molecular_mass(coef,pa))

    element_name="Rame"
    peso=1 #g
    print(calculate_molar_mass(peso,element_name))
    


if __name__=="__main__":
    main()