import os,sys
from pathlib import Path
import logging


while True:
    project_name = input("Enter your proect name")
    if project_name != "":
        break

#src/__init__.py
#src/components/__init__.py
lst_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/config.yaml",
    f"{project_name}/exception/config.json",
    f"{project_name}/logger/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "requirements.txt",
    "setup.py",
    "exceptions.py",
    "README.md",
]

for file in lst_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"{filepath} already exists and is not empty. Skipping creation.")
    logging.info(f"Created file: {filepath}")