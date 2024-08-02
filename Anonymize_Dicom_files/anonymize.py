import os
import pydicom
import argparse

def anonymize_dicom(dataset):

    tags_to_modify = {
            (0x0010, 0x0010): 'Anonymized',     # Patient's Name
            (0x0010, 0x0020): '000000',         # Patient ID
            (0x0010, 0x0030): '19000101',       # Patient's Birth Date
            (0x0010, 0x0040): 'O',              # Patient's Sex
            (0x0010, 0x1010): '',               # Patient's Age
            (0x0010, 0x1040): '',               # Patient's Address
            (0x0010, 0x2154): '',               # Patient's Telephone Numbers
            (0x0008, 0x0090): 'Anonymized',     # Referring Physician's Name
            (0x0008, 0x0092): '',               # Referring Physician's Address
            (0x0008, 0x0094): '',               # Referring Physician's Telephone Numbers
            (0x0008, 0x1050): 'Anonymized',     # Performing Physician's Name
            (0x0008, 0x1052): '',               # Performing Physician Identification Sequence
            (0x0010, 0x4000): '',               # Patient Comments
            (0x0032, 0x4000): '',               # Study Comments
            (0x0010, 0x21B0): '',               # Additional Patient History
            (0x0020, 0x4000): '',               # Image Comments
            (0x0020, 0x4001): '',               # Frame Comments
            (0x0008, 0x0020): '19000101',       # Study Date

            # Study and Series Information
            (0x0020, 0x0010): '00000',   # Study ID
            (0x0008, 0x1030): 'Anonymized Study Description',  # Study Description
            (0x0008, 0x103E): 'Anonymized Series Description',  # Series Description
            (0x0008, 0x0020): '19000101',       # Study Date
            (0x0008, 0x0021): '19000101',       # Series Date
            (0x0008, 0x0022): '19000101',       # Acquisition Date
            (0x0008, 0x0023): '19000101',       # Content Date
            (0x0008, 0x0030): '000000',         # Study Time
            (0x0008, 0x0031): '000000',         # Series Time
            (0x0008, 0x0032): '000000',         # Acquisition Time
            (0x0008, 0x0033): '000000',         # Content Time
        }
    for tag, value in tags_to_modify.items():
        if tag in dataset:
            dataset[tag].value = value
        # else:
        #     dataset.add_new(tag, 'LO', value)

    dataset.remove_private_tags()


    # for tag in tags_to_remove:
    #     if tag in dataset:
    #         del dataset[tag]

    # dataset.PatientName = "Anonymized"
    # dataset.PatientID = "000000"
    return dataset

def anonymize_files_in_directory(input_dir, output_dir, only_one_dir=None):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.dcm'):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, relative_path)

                if only_one_dir and not relative_path.startswith(only_one_dir):
                    continue

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                # Read the DICOM file
                dataset = pydicom.dcmread(input_file_path)
                # Anonymize the dataset
                anonymized_dataset = anonymize_dicom(dataset)
                # Save the anonymized DICOM file
                anonymized_dataset.save_as(output_file_path)
                print(f"Anonymized and saved: {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anonymize DICOM files in a directory.")
    parser.add_argument("--input_dir", type=str, default="/Data/Mori_surgery_cohort", help="Path to the input directory containing DICOM files. Default is 'input'.")
    parser.add_argument("--output_dir", type=str, default="/Data/Mori_surgery_cohort_ananymized", help="Path to the output directory to save anonymized DICOM files. Default is 'output'.")
    parser.add_argument("--only_one_dir", type=str, default=None, help="The only path to consider.")
    args = parser.parse_args()
    anonymize_files_in_directory(args.input_dir, args.output_dir, args.only_one_dir )



# # Patient Information
# (0x0010, 0x0010),  # Patient's Name
# (0x0010, 0x0020),  # Patient ID
# (0x0010, 0x0030),  # Patient's Birth Date
# (0x0010, 0x0040),  # Patient's Sex
# (0x0010, 0x1010),  # Patient's Age
# (0x0010, 0x1040),  # Patient's Address
# (0x0010, 0x2154),  # Patient's Telephone Numbers

# # Study and Series Information
# (0x0020, 0x000D),  # Study Instance UID
# (0x0020, 0x000E),  # Series Instance UID
# (0x0020, 0x0010),  # Study ID
# (0x0008, 0x1030),  # Study Description
# (0x0008, 0x103E),  # Series Description
# (0x0008, 0x0020),  # Study Date
# (0x0008, 0x0021),  # Series Date
# (0x0008, 0x0022),  # Acquisition Date
# (0x0008, 0x0023),  # Content Date
# (0x0008, 0x0030),  # Study Time
# (0x0008, 0x0031),  # Series Time
# (0x0008, 0x0032),  # Acquisition Time
# (0x0008, 0x0033),  # Content Time

# # Referring and Performing Physicians
# (0x0008, 0x0090),  # Referring Physician's Name
# (0x0008, 0x0092),  # Referring Physician's Address
# (0x0008, 0x0094),  # Referring Physician's Telephone Numbers
# (0x0008, 0x1050),  # Performing Physician's Name
# (0x0008, 0x1052),  # Performing Physician Identification Sequence

# # Institution Information
# (0x0008, 0x0080),  # Institution Name
# (0x0008, 0x0081),  # Institution Address
# (0x0008, 0x1010),  # Station Name
# (0x0008, 0x1040),  # Institutional Department Name

# # Device Information
# (0x0008, 0x0070),  # Manufacturer
# (0x0008, 0x1090),  # Manufacturer Model Name
# (0x0018, 0x1000),  # Device Serial Number
# (0x0018, 0x1020),  # Software Versions

# # Operator Information
# (0x0008, 0x1070),  # Operator's Name
# (0x0008, 0x1072),  # Operator Identification Sequence

# # Protocol Information
# (0x0018, 0x1030),  # Protocol Name
# (0x0008, 0x1032),  # Procedure Code Sequence
# (0x0040, 0x0009),  # Scheduled Procedure Step ID
# (0x0040, 0x0007),  # Scheduled Procedure Step Description
# (0x0040, 0x1001),  # Requested Procedure ID
# (0x0032, 0x1060),  # Requested Procedure Description

# # Comments and Descriptions
# (0x0010, 0x4000),  # Patient Comments
# (0x0032, 0x4000),  # Study Comments
# (0x0010, 0x21B0),  # Additional Patient History

# # Overlay and Curve Data
# (0x6000, 0x3000),  # Overlay Data
# (0x5000, 0x3000),  # Curve Data

# # Image and Frame Data
# (0x0020, 0x4000),  # Image Comments
# (0x0020, 0x4001),  # Frame Comments



# tags_to_remove = [
#     (0x0010, 0x0010), (0x0010, 0x0020), (0x0010, 0x0030), (0x0010, 0x0040),
#     (0x0010, 0x1010), (0x0010, 0x1040), (0x0010, 0x2154), 
#     (0x0010, 0x1000),
#     (0x0010, 0x1001), (0x0010, 0x1090), (0x0010, 0x2160), (0x0010, 0x2180),
#     (0x0010, 0x21B0), (0x0010, 0x4000), (0x0020, 0x000D), (0x0020, 0x000E),
#     (0x0020, 0x0010), (0x0008, 0x1030), (0x0008, 0x103E), (0x0008, 0x0020),
#     (0x0008, 0x0021), (0x0008, 0x0022), (0x0008, 0x0023), (0x0008, 0x0030),
#     (0x0008, 0x0031), (0x0008, 0x0032), (0x0008, 0x0033), (0x0008, 0x0090),
#     (0x0008, 0x0092), (0x0008, 0x0094), (0x0008, 0x1050), (0x0008, 0x1052),
#     (0x0008, 0x0080), (0x0008, 0x0081), (0x0008, 0x1010), (0x0008, 0x1040),
#     #(0x0008, 0x0070), (0x0008, 0x1090), (0x0018, 0x1000), (0x0018, 0x1020),
#     (0x0008, 0x1070), (0x0008, 0x1072), (0x0018, 0x1030), (0x0008, 0x1032),
#     (0x0040, 0x0009), (0x0040, 0x0007), (0x0040, 0x1001), (0x0032, 0x1060),
#     (0x0032, 0x4000), (0x6000, 0x3000), (0x5000, 0x3000), (0x0020, 0x4000),
#     (0x0020, 0x4001)
# ]