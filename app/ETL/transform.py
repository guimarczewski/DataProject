"""module with all the necessary transformations to consolidate the input data."""

import pandas as pd


def transforma_em_um_unico(all_data):
    """
    function to consolidate data from Excel files.

    type: all_data: list
    """
    if not all_data:
        raise ValueError("No data to transform")
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
    return consolidated_df