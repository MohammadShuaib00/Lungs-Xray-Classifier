import zipfile
import os
import sys
from xray.logger.logging import logging
from xray.exception.exception import XrayException

def unzip_data(zip_file_path, destination_dir):
    """
    Extracts the contents of a zip file while maintaining the folder structure.
    """
    try:
        logging.info(f"Unzipping data from {zip_file_path} to {destination_dir}")
        
        # Extract the zip file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(destination_dir)
        
        logging.info(f"Data unzipped successfully to {destination_dir}")
    except Exception as e:
        raise XrayException(e, sys)
