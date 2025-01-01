import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from snippets.fileManagement import read_file_chemical_element_

print(read_file_chemical_element("data/chemical_element.txt","Calcio"))