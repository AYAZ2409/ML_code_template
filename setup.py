# Write code scripts for setting up a python package

from setuptools import setup, find_packages
from typing import List

project_name = "ML production template"
version = "0.0.1"
description = "This a template built for modular coding in ML projects"
author_name = "AYAZ2409"
author_email = "ayazlakhani24@gmail.com"
requirements = "requirements.txt"
hyphen_e_dot = "-e ."
#open rquirements.txt
def get_requirements()->List[str]:
    with open(requirements) as file:
        requirements_lst = file.readlines()
        requirements_lst = [requirement.replace("\n", "") for requirement in requirements_lst if requirement.strip() and not requirement.startswith("#")]

        if hyphen_e_dot in requirements_lst:
            requirements_lst.remove(hyphen_e_dot)
        return requirements_lst
setup(name= project_name,
      version=version,
      description=description,
      author=author_name,
      author_email=author_email,
      packages=find_packages(),
      install_requires= get_requirements(),
      python_requires='>=3.12'
)