# Tests Documentation

Below you will find details about the functions and modules of the project.

## Unitary Tests

### `Create mock input folder with files`

```python
def mock_input_folder(tmpdir):
    """
    Fixture to create mock input folder with sample Excel files for testing.
    """
```

### `Create mock output folder`

```python
@pytest.fixture
def mock_output_folder(tmpdir):
    """
    Fixture to create a mock output folder for testing.
    """
```

### `Extract test`

```python
def test_extract(mock_input_folder):
    """
    Test the extraction of data from the input folder.
    """
```

### `Extract test with no files`

```python
def test_extract_no_files(tmpdir):
    """
    Test extraction functionality with an empty input folder.
    """
```

### `Transform test`

```python
def test_transform():
    """
    Test the transformation of dataframes.
    """
```

### `Transform test with empty list`

```python
def test_transform_empty_list():
    """
    Test the transformation functionality with an empty list.
    """
```

### `No permission output folder`

```python
def test_load_no_permission(tmpdir):
    """
    Test the load functionality with a protected output folder.
    """
```

### `Load test`

```python
def test_load(mock_output_folder):
    """
    Test the load functionality.
    """
```

## Integration Tests

### `Test the complete pipeline`

```python
def test_integration():
     """
     Integration test to check the full consolidate_excels functionality.

     This test simulates a real-world scenario by creating a temporary directory
     with a sample Excel file. The test then checks if the consolidation function
     works as expected.
     """
```