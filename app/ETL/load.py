"""module with all the necessary transformations to consolidate the input data."""

import os


def load_em_um_novo_excel(df, output_folder, output_file_name):
    """
    Carga: Saves a DataFrame to an Excel file.

    type: df: pd.DataFrame
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_excel(
        os.path.join(output_folder, output_file_name), index=False
    )