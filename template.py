import os
from pathlib import Path
import logging

# List of file names along with the directory mentioned

list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/model_api.py",
    "QAWithPDF/embedding.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

# Iterate over each string path
for filepath in list_of_files:
    # Convert the string to actual path
    filepath = Path(filepath)

    #split the file directory and file name from the path
    filedir, filename = os.path.split(filepath)

    #if file directory exists, create one
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    #if filename doesnt exists or filename exists but filesize is 0, create empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists.")

