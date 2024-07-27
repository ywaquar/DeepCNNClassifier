import os
from tkinter import E
from box.exceptions import BoxValueError
import yaml
from deepClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yeaml(path_to_yaml : Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str) : path like inpit

    Raises:
        ValueError: if yaml file is empty
        e : empty file

    Returns:
    
    """
