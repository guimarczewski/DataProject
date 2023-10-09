# API Documentation

Below you will find details about the functions and modules of the project.

## `Consolidator` module

### `extract`

```python
def extract(input_folder: str) -> list:
    """
    Function to extract data from Excel files.

    Args:
        input_folder (str): Path of folder containing Excel files.

    Returns:
        list: List containing pandas DataFrames.
    """
```

### `transform`

```python
def transform(data: list) -> pd.DataFrame:
    """
    Function to transform a list of DataFrames into a single consolidated DataFrame.

    Args:
        data (list): List containing DataFrames for consolidation.

    Returns:
        DataFrame: Consolidated DataFrame.
    """
```

### `load`

```python
def load(df: pd.DataFrame, output_folder: str, filename: str) -> None:
    """
    Function to save a DataFrame into an Excel file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        output_folder (str): Directory where the file will be saved.
        filename (str): Excel file name.

    Returns:
        None
    """
```

### `consolidate_excels`

```python
def consolidate_excels(input_folder: str, output_folder: str, filename: str) -> None:
    """
    Function to consolidate multiple Excel files into a single file.

    Args:
        input_folder (str): Folder containing Excel files.
        output_folder (str): Folder where the consolidated file will be saved.
        filename (str): Name of the consolidated Excel file.

    Returns:
        None
    """