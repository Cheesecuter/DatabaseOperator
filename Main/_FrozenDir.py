# This file is provided for freezing the required file path when the program is packaged
import os
import sys


# This function is responsible for freezing the file path.
def app_path():
    if hasattr(sys, "frozen"):
        return os.path.dirname(os.path.dirname(sys.executable))
    return os.path.dirname(os.path.dirname(__file__))
