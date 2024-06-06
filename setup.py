from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path) ->List[str]:
    
    """
    This function will return the list of requirments
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if HYPEN_E_DOT is requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
setup(
    name = 'mlproject',
    version='0.0.1',
    author='Rayan Joseph',
    author_email= 'rayanjoseph05@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirments.txt')
) 