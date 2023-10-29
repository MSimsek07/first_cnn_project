import os
# using box for exceptions
from box.exceptions import BoxValueError
# To read the yaml file using yaml
import yaml
from cnnClassifier import logger
import json
import joblib
#
from ensure import ensure_annotations

from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# purpose of using "@ensure_annotations" is


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns
    function return type is ConfigBox
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty!")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    creates list of directories

    Args:
        path_to_directories (list): list of directories
        ignore_log(bool, optional): ignore multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.mkdirs(path, exists_ok=True)
        if verbose:
            logger.info(f"directory created at {path}")

# during the model evalution we need to save model metrics as json


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    saves json file
    Args:
        path (Path): path to save json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    loads json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes isntead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    saves binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to save binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    loads binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    gets size in KB
    Args:
        path (Path): path to file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decode_image(img_string, file_name):
    img_data = base64.b64decode(img_string)
    with open(file_name, "wb") as f:
        f.write(img_data)
        f.close()


def encode_image(cropped_image_path):
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())
