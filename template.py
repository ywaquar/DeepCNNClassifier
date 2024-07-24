import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

pacakge_name = 'deepClassifier'

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{pacakge_name}/__init__.py",
    f"src/{pacakge_name}/components/__init__.py",
    f"src/{pacakge_name}/utils/__init__.py",
    f"src/{pacakge_name}/config/__init__.py",
    f"src/{pacakge_name}/pipeline/__init__.py",
    f"src/{pacakge_name}/entity/__init__.py",
    f"src/{pacakge_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "project.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass #create an empty file
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} already exist")

            
