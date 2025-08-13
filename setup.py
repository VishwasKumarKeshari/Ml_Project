from setuptools import setup, find_packages
from typing import List
hyphen_e_dot = "-e ."
def get_requirements(file_path: str) -> List:
    """
    Reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements        
setup(
    name="ML_Project",
    version="0.1.0",
    description="A machine learning project",
    author="Vishwas Keshari",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
   
)