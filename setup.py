'''
    setup.py file 

'''

from setuptools import find_packages,setup
from typing import List
from typing import Generator

# def get_requirements()-> List[str]:
#     '''
#     This function will return the list of requirements
#     '''
#     requirements:List[str] = []
#     try: 
#         with open('requirements.txt', 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 requirement = line.strip()
#                 if requirement and not requirement.startswith('#') and not requirement.startswith('-e .'):
#                     requirements.append(requirement)       
#     except FileNotFoundError:
#         return requirements



def get_requirements() -> Generator[str, None, None]:
    """
    This function will yield the requirements line by line.
    """
    try: 
        with open('requirements.txt', 'r') as file:
            # OPTIMIZATION: Loop directly over 'file' instead of file.readlines()
            for line in file:
                requirement = line.strip()
                if requirement and not requirement.startswith('#') and not requirement.startswith('-e .'):
                    yield requirement        
    except FileNotFoundError:
        print("⚠️ Warning: requirements.txt not found.")
        # A generator function uses a bare 'return' to stop yielding values safely
        return 


requirements = list(get_requirements())
#print(f"✅ Requirements loaded: {requirements}")

setup(
        name="Network_security_MLOps",
        version="0.0.1",
        author="Rishav Kumar",
        author_email="rishav.sukarna@gmail.com",
        packages=find_packages(),
        install_requires=requirements
    )