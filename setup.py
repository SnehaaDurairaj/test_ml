from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path) ->List[str]:
    
    """
    This function will return the list of requirments
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
setup(
    name = 'mlproject',
    version='0.0.1',
    author='Rayan Joseph',
    author_email= 'rayanjoseph05@gmail.com',
    packages=find_packages(),
    requires=['pandas', 'numpy', 'seaborn']
)