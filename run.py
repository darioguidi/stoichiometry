import sys
import os

project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

from snippets.application import application

def main():
    application()
    
if __name__=="__main__":
    main()