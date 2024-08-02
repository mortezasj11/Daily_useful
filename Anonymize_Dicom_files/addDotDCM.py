import os
import re
import argparse

def add_dcm_extension(filename):
    """Add .dcm extension to the filename."""
    return filename + '.dcm'

finding_dcm_organized = False

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Anonymize DICOM files in a directory.")
    parser.add_argument("--input_dir", type=str, default="/Data/Mori_surgery_cohort/34.949692/DICOM", help="Path to the input directory containing DICOM files.")
    args = parser.parse_args()
    path = args.input_dir

    for dcm in os.listdir(path):
        file_path = os.path.join(path, dcm)
        # Check if the file has a long numeric extension
        if os.path.isfile(file_path):
            # Rename the file by adding .dcm extension
            new_filename = add_dcm_extension(dcm)
            new_file_path = os.path.join(path, new_filename)
            os.rename(file_path, new_file_path)