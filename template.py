import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s]')

package_name = "heart"

list_of_files=[
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/config_entity.py",
    f"src/{package_name}/entity/artifact_entity.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_validation.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/components/model_evaluation.py",
    f"src/{package_name}/components/model_pusher.py",
    f"src/{package_name}/configuration/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/logger/__init__.py",
    f"src/{package_name}/exception/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/tain_pipeline.py",
    f"src/{package_name}/pipeline/prediction_pipeline.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/commonutils.py",
    f"config/config.yaml",
    f"params.yaml",
    f"notebooks/experiments.ipynb",
    "app.py",
    "train.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py"
    ]   

for file_path in list_of_files:

    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating file directory {filedir} for file {filename}")

    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file:
            pass
            logging.info(f"Empty file {filepath} created successfully !")
    else:
        logging.info(f"file {filepath} already exist.")