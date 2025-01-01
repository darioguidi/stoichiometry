from src.molecularMass import molecular_mass_calculation
from src.molarMass import molar_mass_calculation

def main():
    coef=[2,1,4]
    pa=[23,32,16]
    print(molecular_mass_calculation(coef,pa))

if __name__=="__main__":
    main()