"""extract module needed to consolidate input data."""

import glob
import os

import pandas as pd


def extract_excel(input_folder):
    """
    function to extract data from Excel files.

    type: input_folder: str
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    all_data = [pd.read_excel(file) for file in files]
    return all_data