"""Test integration"""

import os
import shutil
import tempfile

import pandas as pd

from app.ETL import pipeline_completa


def test_integration():
     """
     Integration test to check the full consolidate_excels functionality.

     This test simulates a real-world scenario by creating a temporary directory
     with a sample Excel file. The test then checks if the consolidation function
     works as expected.
     """
     # Create a temporary folder to simulate the real environment
     with tempfile.TemporaryDirectory() as tmpdirname:
         # Configure input and output folders
         input_folder = os.path.join(tmpdirname, "input")
         output_folder = os.path.join(tmpdirname, "output")
         os.makedirs(input_folder)

         # Create a real Excel file for testing
         sample_data = pd.DataFrame({"A": list(range(1, 11)), "B": list("abcdefghij")})
         sample_file_path = os.path.join(input_folder, "sample.xlsx")
         sample_data.to_excel(sample_file_path, index=False)

         # Execute the consolidate_excels function
         pipeline_complete(input_folder, output_folder, "consolidated.xlsx")

         # Check if the output file exists and has the expected content
         output_file_path = os.path.join(output_folder, "consolidated.xlsx")
         assert os.path.exists(output_file_path)

         loaded_data = pd.read_excel(output_file_path)
         pd.testing.assert_frame_equal(loaded_data, sample_data)