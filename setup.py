'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """
    requirements_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            ##read line from the files
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirements=line.strip()
                ##ignoring empty lines and -e .
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

setup(
    name='NetworkSecurity',
    version='0.0.0.1',
    author='Ahad Khan',
    author_email='ahadkhan.ai306@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)


