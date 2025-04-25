from functools import wraps
from time import time
import yaml
import json
import os

def is_video(ext: str):
    """
    Returns true if ext exists in
    allowed_exts for video files.

    Args:
        ext:

    Returns:

    """

    allowed_exts = ('.mp4', '.webm', '.ogg', '.avi', '.wmv', '.mkv', '.3gp')
    return any((ext.endswith(x) for x in allowed_exts))


def tik_tok(func):
    """
    keep track of time for each process.
    Args:
        func:

    Returns:

    """
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time()
            print("time: {:.03f}s, fps: {:.03f}".format(end_ - start, 1 / (end_ - start)))

    return _time_it

def generate_idx_to_class(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    class_names = data['names']

    # Create an index for each class name
    idx_to_class = {str(idx): name for idx, name in enumerate(class_names)}

    # Save to json
    with open("idx_to_class.json", 'w') as f:
        json.dump(idx_to_class, f, indent=4)
    return idx_to_class

