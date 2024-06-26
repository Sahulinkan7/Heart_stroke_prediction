import os,sys
from pathlib import Path
project_name="heart_stroke_src"
list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/constants/__init__.py",
    "notebooks/eda.ipynb",
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",    
]

for file in list_of_files:
    filepath=Path(file)
    folder,filename = os.path.split(filepath)
    
    if folder!="":
        os.makedirs(folder,exist_ok=True)
    
    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file:
            pass
    else:
        print("file already exists")