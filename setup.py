#creating machine learning application as an package 

from setup.tools import find_packages,setup # it is used to find all packages n libraries listed in modules
from typing import List

HYPEN_E_DOT='-e .' #this will automatically trigger setup.py from requirements.txt (-e.) everytime so to remove this we use if loop inside get_requirements

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of libraries in the requirements.txt file

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements: # to remove -e. in the requirements.txt file , this will enable to install all locally created python module/package libraries (triggering setup.py)
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

#metadata for the ml application 
setup(
name='students_performance',
version='0.0.1',
author='Karthik',
author_email='karthiksurya611@gmail.com',
packages=find_packages(), #whereeven __init__.py is there it will go to that folder and find all libraries
install_requires=get_requirements('requirements.txt')

)



"""
use pip install -r requirements.txt
and in folder structure seperate package will be created
"""