import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml :Path)->ConfigBox:
    '''read a yaml file and return 
    Args:
       path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e : empty file

    Returns:
        ConfigBox: config box type    
     '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully") 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file : {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories :list, verbose=True):
    """ Create list of directories
    Args:
    path_to_directories (list): list of directories to create
    ignore_log(bool, optional): ignore if multiple directories is to be created. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory at : {path} created successfully")

@ensure_annotations
def save_json(path_to_json :Path, data :dict):
    """save a json file
    Args:
    path_to_json (str): path like input
    data (dict): data to save in json file
    """
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path_to_json}")
        

@ensure_annotations
def load_json(path_to_json :Path)->ConfigBox:
    """
    Args:
        path_to_json (str): path like input
    returns:
    ConfigBox: data as class attribute instead of dict"""

    with open(path_to_json) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully at: {path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path_to_bin :Path):
    """save a binary file"""
    joblib.dump(value=data, filename=path_to_bin) 
    logger.info(f"binary file saved at: {path_to_bin}")

@ensure_annotations
def load_bin(path_to_bin :Path)->Any:
    """load a binary file"""
    data = joblib.load(path_to_bin) 
    logger.info(f"binary file loaded successfully at: {path_to_bin}") 

    return data

@ensure_annotations
def get_size(path_to_bin :Path)->str:
    """get the size in kb"""
    size_in_kb = round(os.path.getsize(path_to_bin)/1024)
    return f"{size_in_kb} kb"

def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeimageintobase64(cropped_image_path):
    with open(cropped_image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read())
    return encoded_image