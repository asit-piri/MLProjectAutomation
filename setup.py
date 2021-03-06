from pkg_resources import Requirement
from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass

# Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Asit Piri"
DESCRIPTION="This is a Machine Learning Project."
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    
    Description: This function is going to return list of requirement
    mentioned in the requirements.txt file.

    Return this function is going to return a list which contains name
    of libraries mentioned in the requirements.txt file

    """

    with open (REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)